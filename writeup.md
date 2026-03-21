1) Which file appears to represent the most active period? Explain using at least two metrics. Consider that this is a 30 year old participant and compare your output to the column titled "Target HR Zone 50-85%" within this link: https://www.heart.org/en/healthy-living/fitness/fitness-basics/target-heart-rates

Phase_1 has the highest average and median out of all of the other phases. Average is 87.3, Median is 86.5

2) Which file had the **poorest** data quality? How do you know?

Phase_0 has the poorest data quality beacuse it has the most amount of malformed values. (ie "NO DATA, "empty values")

3) Suppose one heart-rate file contains the following cleaned values: `68, 70, 71, 72, 72, 73, 74, 75, 180`. The value 180 was recorded during a sensor glitch.

a) Calculate the range of this dataset.

Range = 180-68 = 112


b) Explain how the extreme value affects the range.

The new range will be 75-68 = 7 which is significantly lower tham the range above which includes the outlier 180. 


c) Identify a different statistic that would better represent the typical variability of the dataset. Why would this measure be better?

Calculating the interquartile range would eliminate outliers and give a better representation of the typical variability of the dataset and  eliminate the outliers that impact the average, median and range of the data.