import pandas as pd
from scipy.stats import shapiro, levene, ttest_ind

control = pd.read_excel("datasets/ab_testing.xlsx", sheet_name="Control Group")
test = pd.read_excel("datasets/ab_testing.xlsx", sheet_name="Test Group")
control.head()


# Task 1: Define the hypothesis of the A/B test.
# Is there a statistically significant difference between Maximum Bidding and Average Bidding?


# Task 2 — Step 1: Normality Assumption
# H0: The assumption of normal distribution is provided.
# H1:..not provided.
test_stat, pvalue = shapiro(control["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

test_stat, pvalue = shapiro(test["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
# Since the p-value of the Control group and the Test group is > 0.05,
# H0 cannot be rejected and both provide the assumption of normal distribution.


# Task 2 — Step 2: Variance Homogeneity
# H0: Variances are Homogeneous
# H1: Variances Are Not Homogeneous
test_stat, pvalue = levene(control["Purchase"],
                           test["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
# Since p-value > 0.05, H0 cannot be rejected and variances are homogeneous.


# Task 2 — Step 3: Independent Two-Sample T-Test
# Since the assumption of normality and homogeneity of variance are provided, an independent two-sample t-test (parametric test) can be applied.
test_stat, pvalue = ttest_ind(control["Purchase"],
                              test["Purchase"],
                              equal_var=True)  # variance represents homogeneity.
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
# Since p-value > 0.05, H0 cannot be rejected and we say that there is no statistically significant difference between Maximum Bidding and Average Bidding.


# Task 3: Which tests did you use? Please explain.
# First, we used the Shapiro-Wilk test to make the assumption of normality and learned that the assumption of normality was satisfied.
# Afterwards, we had to control the homogeneity of variance since the assumption of normality was provided.
# We used Levene's test to control variance homogeneity and we learned that variance homogeneity was achieved.
# Since the assumptions were provided, the two-sample t-test (parametric test) was used and the result was reached.


# Task 4 : What is your advice to the customer?
# The data set we examined consists of 40 observations. We can get a more reliable result from more observations.
# Were the observations in the test dataset and the observations in the control dataset taken at the same time?
# If it does not cover the same periods, there may be a difference in the results.
# Observing at the same time is important for a more accurate result.
# How many weekdays and how many weekend days are in our observations?
# The weekday shopping habits of the customers may differ from the weekend shopping habits.
# Therefore, a more accurate result can be obtained if the number of weekdays/weekend days in the observations is similar.








