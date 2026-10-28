"""Execute every notebook without changing saved replication notebooks."""
from pathlib import Path
import argparse, hashlib, json, os, subprocess, sys, tempfile
ROOT = Path(__file__).resolve().parent

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--extensions-only', action='store_true')
    args = parser.parse_args()
    protected = sorted((ROOT/'replication').glob('*.ipynb')) + sorted((ROOT/'data').rglob('*.xlsx'))
    before = {str(p.relative_to(ROOT)):digest(p) for p in protected}
    with tempfile.TemporaryDirectory(prefix='time-estimates-run-') as tmp:
        tmp = Path(tmp)
        os.environ['JUPYTER_PATH'] = str(tmp/'jupyter')
        os.environ['JUPYTER_RUNTIME_DIR'] = str(tmp/'runtime')
        os.environ['IPYTHONDIR'] = str(tmp/'ipython')
        spec = tmp/'jupyter/kernels/project'
        spec.mkdir(parents=True)
        (spec/'kernel.json').write_text(json.dumps({'argv':[sys.executable,'-m','ipykernel_launcher','-f','{connection_file}'], 'display_name':'Project Python','language':'python'}))
        import nbformat
        from nbclient import NotebookClient
        paths = [] if args.extensions_only else sorted((ROOT/'replication').glob('*.ipynb'))
        paths += sorted((ROOT/'additional_robustness_checks').glob('*.ipynb'))
        for path in paths:
            nb = nbformat.read(path, as_version=4)
            nbformat.validate(nb)
            NotebookClient(nb,timeout=300,kernel_name='project',resources={'metadata':{'path':str(path.parent)}}).execute()
            # Original replication outputs and notebook bytes are deliberately preserved.
            if path.parent.name == 'additional_robustness_checks':
                nbformat.write(nb,path)
            print('PASS',path.relative_to(ROOT),flush=True)
    assert before == {str(p.relative_to(ROOT)):digest(p) for p in protected}, 'Protected original files changed'
    subprocess.run([sys.executable,str(ROOT/'build_report.py')],cwd=ROOT,check=True)
    print('PASS original replication notebooks and datasets unchanged',flush=True)

if __name__=='__main__':
    main()
