# INFO-B211_Assignment-7-Matplotlib

## Overview
This project demonstrates the use of Matplotlib to create insightful visualizations for two datasets:
- Loan Dataset: Analyzing loan data to uncover trends in default rates, interest rates, and loan statuses.
- Iris Dataset: Visualizing physical traits of iris flowers to illustrate differences between species.

The project is designed to showcase the power of data visualization in understanding datasets and extracting meaningful insights. Each visualization is implemented using Matplotlib, with a consistent color theme applied to enhance readability and aesthetics.

## Project Structure
The project is divided into two main sections:

#### Loan Dataset Visualizations:

- Bar chart of default rates by loan intent.
- Histogram of average loan interest rates by customer age.
- Pie chart of loan statuses.

#### Iris Dataset Visualizations:

- Scatter plot of petal length vs. petal width.
- Box plot of sepal length by species.
- Overlapping histograms of sepal length by species.

## Loan Dataset Visualizations
#### Purpose
The loan dataset visualizations aim to uncover trends in loan performance, such as default rates, interest rate distributions, and the proportion of loans in default or non-default status.

### Visualizations
#### Bar Chart: Default Rate by Loan Intent

##### Purpose: 
Show the default rate for each loan intent category (e.g., education, medical, personal).
##### Implementation:
A bar chart with different shades of pink for each bar.
Default rates are displayed as numbers above each bar.
##### Limitations: 
The dataset assumes clean and complete data for calculating default rates.

#### Histogram: Distribution of Average Loan Interest Rates by Customer Age

##### Purpose: 
Visualize the distribution of average loan interest rates across customer ages.
##### Implementation:
A histogram with bins representing ranges of interest rates.
Uses a consistent pink color theme.
##### Limitations:
Missing or invalid interest rate values are ignored.

#### Pie Chart: Proportion of Loans by Current Loan Status

##### Purpose: 
Show the proportion of loans in "DEFAULT" vs. "NO DEFAULT" status.
##### Implementation:
A pie chart with slices for each loan status.
Explodes the "DEFAULT" slice for emphasis.
##### Limitations: Assumes only two loan statuses are present.
