## 3 Additional analyses

The following student analyses extend the replication using the original data and exclusions. They are exploratory and are distinguished from the authors’ reported findings.

### Trust and perceived accuracy in Study 2

The first analysis asks whether estimate formats influence trust and perceived accuracy in similar ways. Unlike the composite outcome, separate items can reveal differences between these evaluations. After the original duplicate exclusions, the sample contains 599 participants. Point, moderate-range, and wide-range conditions contain 196, 206, and 197 participants, respectively; neither item has missing responses. Table B1 reports group means and standard deviations, and Figure B1 shows individual 95% t confidence intervals.

Separate classical one-way ANOVAs detected condition differences in trust, F(2, 596) = 12.296, p < .001, and perceived accuracy, F(2, 596) = 18.633, p < .001. Both remain significant after Holm correction across the two outcomes. Because the median-centered Levene test indicated unequal variances for accuracy (p < .001), Welch ANOVAs were also estimated; both confirmed the omnibus conclusions (Table B2). Pairwise comparisons use Welch t tests with Holm correction over all six comparisons; Table B3 also reports Bonferroni simultaneous 95% intervals.

Moderate ranges produced higher trust and accuracy ratings than both alternatives. Wide ranges exceeded point estimates on accuracy (difference = 0.485; Holm p = 0.0068), but the corresponding trust difference was inconclusive (difference = 0.165; Holm p = 0.2732). Thus, the observed patterns broadly favor moderate ranges, while wider estimates’ accuracy advantage does not translate into detectable higher trust. This describes the two outcomes’ patterns; it does not formally test equality of their treatment effects or show that the nonsignificant trust effect is zero.

This analysis overlaps with the authors’ Study 2 exploratory item-level OLS regressions (Study 2.do, section 3.4). ANOVA uses the same underlying group-mean model; the explicit omnibus tests, multiplicity adjustments, Welch sensitivity checks, and figure supplement that existing analysis. It is not a new substantive hypothesis. Supplement 2’s percentage/error accuracy measures differ from the sb_accurate item used here.

### Pooled study fixed effects and leave one study out

The second analysis tests whether the pooled range advantage depends on any single experiment. Comparable point and moderate-range conditions from Studies 1, 2, 3, 5, 6, and 7 were pooled, retaining the original five-item satisfaction composite and exclusion rules. Study 7 contributes its accurate point and accurate range conditions. Study 3 varies estimates across trials. The full sample contains 2,720 participants, with no missing composites. OLS regresses satisfaction on a range indicator and study fixed effects, using conventional OLS standard errors and residual-degrees-of-freedom t intervals. These standard errors assume equal error variance across observations. The identical specification is then estimated six times, omitting one study each time (Table B4 and Figure B2).

The full-sample range coefficient is 0.721 points (SE = 0.047; 95% CI [0.629, 0.813]; p < .001). Omission estimates range from 0.695 to 0.754; every confidence interval remains above zero. The largest absolute change occurs when Study 1 is excluded (change = +0.033; coefficient = 0.754). The evidence therefore does not indicate that any single included study drives the positive pooled effect.

These related sensitivity models are not independent confirmations and do not establish identical effects across studies. Pooling also assumes independent observations across experiments; cross-study participant overlap cannot be checked using study-specific de-identified IDs. The check addresses study influence rather than field generalizability or every form of heterogeneity. No equivalent six-study fixed-effects leave-one-study-out analysis was found in the reviewed paper, complete supplement, or 11 supplied do-files. The supplement’s app-domain fixed effects concern a different design. This absence claim is limited to the materials reviewed.

