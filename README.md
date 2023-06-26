#Final Project 4 -Likelihood of defaulting credit card payments

## Machine Learning Integration
## Likelihood of defaulting credit card payments

## Authors
* **Alonso Lozano** - **[My github](https://github.com/loncho95 "GitHub for Alonso Lozano")**
* **Aldo Silva** - **[My github](https://github.com/aldosilesp "GitHub for Aldo Silva")**
* **Alejandra Espinosa** - **[My github](https://github.com/zuntaalejandra "GitHub for Ale Espinosa")**
* **Marcela Maldonado** - **[My github](https://github.com/Marce1301 "GitHub for Marcela Maldonado")**

## Tools and sources
* Python Pandas
* Tableau
* Machine Learning

## Introduction

This project is aimed at predicting the case of customers default payments based of data colected in Taiwan. From the perspective of risk management, the result of predictive accuracy of the estimated probability of default will be very valuable.

## Project Proposal

We have two goals:

1) Creating a set of visualizations in Tableau of the default and non-default credit card clients and the relationship that defaulting has with demographic features and the payment history of each customer.

2) Creating a supervised machine learning model to predict whether a credit card holder will be on default or not depending on their demographic profile and payment history.
The purpose is to evaluate which customers will default on their credit card payments.
Default payment could be --> Yes = 1, No = 0, as the response variable (Y value). 

## Project overview 

All the work done, tools and can be summarized in the next image:

<p align="center"><img src="https://github.com/Marce1301/Likelihood_of_defaulting_credit_card_payments/blob/main/Other_Stuff/Images_README/Proj_Breakdown.png" /></p>


## Data source

For this project we fetch and grabbed the data from **[Kaggle](https://www.kaggle.com/)** our data set were retrived form **[Kaggle Data Source](https://www.kaggle.com/code/bansodesandeep/credit-card-default-prediction/notebook)**


## Data Explained

All The fields (in order of appereance):

* ID
* Credit limit
* Age
* Sex
* Education
* Marriage
* Payment made Sep 2005
* Payment made Aug 2005
* Payment made Jul 2005
* Payment made Jun 2005
* Payment made May 2005
* Payment made Apr 2005
* Amount of bill Sep 2005
* Amount of bill Aug 2005
* Amount of bill Jul 2005
* Amount of bill Jun 2005
* Amount of bill May 2005
* Amount of bill Apr 2005
* Amount previous pay Sep 2005
* Amount previous pay Aug 2005
* Amount previous pay Jul 2005
* Amount previous pay Jun 2005
* Amount previous pay May 2005
* Amount previous pay Apr 2005
--> Default Payment Next Month (Y Value)


## Data Cleanup and Analysis

### Exploration and clean up

* Null Value Handling

To ensure data integrity, null values were addressed by either removing or imputing missing values

* Standardization

Numeric features were standardized by scaling them to have zero mean and unit variance.
Dummy variables were excluded from this process.

* Dummy Variable Creation
  
Categorical variables were converted into binary variables, known as dummy variables, to effectively represent them in the dataset.

* Train-Test Data Split with Stratification

The data was split up into training and testing sets, stratifing them based on the target values. This ensured a balanced distribution of target values in both sets, reducing bias in subsequent analyses and model training.

In the original analysis, Principal Component Analysis (PCA) and Client Clusterization (unsupervised ML) were conducted as preprocessing steps to reduce the dimensionality of the dataset and transform the original variables into uncorrelated principal components. However, in the final analysis, these steps were omitted because they were found to decrease the accuracy of the models.

While PCA is commonly used for dimensionality reduction and feature extraction, it is possible that in this particular dataset, the reduced number of dimensions resulted in the loss of important information for accurate predictions. In some cases, PCA may not effectively capture the underlying patterns or relationships within the data, leading to a decrease in predictive performance.

Similarly, client clusterization through unsupervised machine learning is used to group similar clients together based on their features or behavior. However, if the resulting clusters do not provide meaningful insights or do not align with the problem at hand, incorporating them into the models may not improve accuracy.

In this scenario, it seems that excluding PCA and client clusterization from the models improved the accuracy, indicating that the original variables and their correlations were more useful for predicting the desired outcome. It's important to remember that data preprocessing techniques should be applied judiciously, as their impact on the final models can vary depending on the dataset and the specific problem being addressed.

### Analysis

There were explored several models; see in the next image, the comparison of different results of all models used:


<p align="center"><img src="https://github.com/Marce1301/Likelihood_of_defaulting_credit_card_payments/blob/main/Other_Stuff/Images_README/Model_perf_Eval.png" /></p>

Having said that, considering the results the best is Randon Forest with oversampler model.


## Description of the best ML Model


Facts of the best model chosen --> a Random Forest with oversampler

1. Precision of 0 (non-default credits) is 0.85: Out of all instances predicted as non-default credits, 85% are actually non-default credits.
2. Precision of 1 (default credits) is 0.61: Out of all instances predicted as default credits, 61% are actually default credits.
3. Recall of 0 (non-default credits) is 0.92: The model correctly identifies 92% of the non-default credits out of all actual non-default credits.
4. Recall of 1 (default credits) is 0.45: The model correctly identifies 45% of the default credits out of all actual default credits.
5. Accuracy Score is 0.8132: The model predicts the correct credit status (default or non-default) for approximately 81.32% of the instances.

This model "a Random Forest with oversampler" get the best results, because the overall performance improved, and the precision of the default credits has increased to 0.61.


Besides that, we found that just 12 features of data, represent 62% of the feature importance of the model, being the most relevants : credit limit and age. 

<p align="center"><img src="https://github.com/Marce1301/Likelihood_of_defaulting_credit_card_payments/blob/main/Other_Stuff/Images_README/12_features.png" /></p>

The 12 importance features (62%) in order of appereance:
* Credit limit
* Age
* Amount of bill Sep 2005
* Amount previous pay Sep 2005
* Amount of bill Aug 2005
* Amount previous pay Aug 2005
* Amount of bill Jul 2005
* Amount of bill Jun 2005
* Payment made Sep 2005
* Amount of bill May 2005
* Amount of bill Apr 2005

## Visual references

Check the next link, the Dashboard designed in Public Tableau to describe the data:

https://public.tableau.com/app/profile/aldo.silva4530/viz/Debtors_16872317116610/Story1?publish=yes

The visualization describes important facts:

Dashboard 1: Likelihood of defaulting by age group and credit limit

<p align="center"><img src="https://github.com/Marce1301/Likelihood_of_defaulting_credit_card_payments/blob/main/Other_Stuff/Images_README/Tableau_page_1.png" /></p>

Dashboard 2: Likelihood of defaulting by sex and education level

<p align="center"><img src="https://github.com/Marce1301/Likelihood_of_defaulting_credit_card_payments/blob/main/Other_Stuff/Images_README/Tableau_page_2.png" /></p>

Dashboard 3: Likelihood of defaulting by marital status

<p align="center"><img src="https://github.com/Marce1301/Likelihood_of_defaulting_credit_card_payments/blob/main/Other_Stuff/Images_README/Tableau_page_3.png" /></p>

Dashboard 4: Likelihood of defaulting by timeliness of past payments

<p align="center"><img src="https://github.com/Marce1301/Likelihood_of_defaulting_credit_card_payments/blob/main/Other_Stuff/Images_README/Tableau_page_4.png" /></p>

Dashboard 5: Likelihood of defaulting by amount of past payments and past total dues

<p align="center"><img src="https://github.com/Marce1301/Likelihood_of_defaulting_credit_card_payments/blob/main/Other_Stuff/Images_README/Tableau_page_5.png" /></p>

## Conclusions

Based on the work done and ML model built, we are able to determine: 

* Predicting credit card default is hard.

* There are certain variables with a strong relationship, such as:

Credit limit
Timeliness of past payments

* Some variables have a mild relationship, such as:

    - Age group
    - Sex
    - Education level
    - Amount of past payments

* Some variables have a weak relationship or no relationship at all:

    - Marital status
    - Amount of past total dues

* Despite of these challenges, we still managed to create a predictive model with acceptable accuracy.

* Finding variables with more explanatory power might yield better results.


## Resources

Bansodesandeep. (2022). Credit Card Default Prediction. Kaggle. https://www.kaggle.com/code/bansodesandeep/credit-card-default-prediction/notebook

## Rubric
* [Project 4 Rubric - Machine Learning Integration.docx]([https://github.com/Marce1301/Likelihood_of_defaulting_credit_card_payments/blob/main/Project%204%20Rubric%20-%20Machine%20Learning%20Integration.docx])

## Copyright

Copyright:copyright: 2023. All Rights Reserved.

© 2023  Lozano Alonso ,Silva Aldo, Espinosa Alejandra, Maldonado Marcela , BootCamp Tecnologico de Monterrey.
