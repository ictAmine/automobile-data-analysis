# Automobile Data Analysis – Exploratory Data Analysis (EDA)

## Project Overview

This project simulates a real-world data analysis workflow using a raw automobile dataset containing technical specifications and pricing information.

The objective is not only to clean the data, but to apply structured statistical reasoning before making transformation decisions.

---

## Dataset Description

The dataset includes features such as:

- Price
- Highway MPG
- City MPG
- Peak RPM
- Horsepower
- Engine size
- Fuel type
- Body style
- Normalized losses
- Symboling (risk indicator)

The dataset contains missing values and mixed data types.

---

## Phase 1 – Data Loading & Inspection

Steps performed:

- Imported dataset using Pandas
- Inspected column names and structure
- Verified data types
- Previewed first observations using `head()`

Initial findings:

- Some numerical columns contain missing values
- Certain variables may contain skewed distributions
- `normalized-losses` contains NaN values

---

## Phase 2 – Data Quality Assessment

Before applying any imputation strategy, missing values were identified and evaluated.

Options considered:

- Dropping rows
- Replacing with mean
- Replacing with median

Decision-making is based on statistical distribution rather than automatic replacement.

---

## Phase 3 – Statistical Decision Framework (In Progress)

Next analytical steps include:

- Measuring skewness of numerical features
- Evaluating outliers
- Deciding between mean vs median imputation
- Preparing the dataset for deeper analysis

---

## Learning Objectives

- Develop structured EDA workflow
- Practice statistical reasoning
- Understand impact of distribution on data cleaning decisions
- Apply reproducible data analysis practices

---

## Tools Used

- Python
- Pandas
- Git
