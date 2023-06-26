

## Data source


Original data was taken from this link:


**[Kaggle](https://www.kaggle.com/)** our data set were retrived form **[Kaggle Data Source](https://www.kaggle.com/code/bansodesandeep/credit-card-default-prediction/notebook)**


We got the data into a CSV file and an MS Excel file (XLSX format)
More than 29,000 rows.

## Data loaded in a MySQL Database in AWS iCloud


In order to have the data available, we uploaded in a MySQL BD.
To have more information about this process, go README file in BD folder. 

## Data Explained

To see the CREATE TABLE Statement, go to the next link:


link

The next picture describes de table in MySQL WorkBench tool.

<p align="center"><img src="https://github.com/Marce1301/Likelihood_of_defaulting_credit_card_payments/blob/main/Other_Stuff/Images_README/Table_Structure.png" /></p>

## First migration try

We tried to upload the data with tool from MySQL WorkBench tool.

The next picture shows the main screen to the configuration of this process

<p align="center"><img src="https://github.com/Marce1301/Likelihood_of_defaulting_credit_card_payments/blob/main/Other_Stuff/Images_README/First_Migration_Try.png" /></p>

unfortunately, this task never ended (it was taking so much time that we had to break the process)

Having said that, considering the results the best is Randon Forest with oversampler model.

## Second migration try

We used a Python program to load the data.
See the code in this link:

link

It took almost 3 hours to finish.

## Confirmation of data into de iCloud BD

As you can see in the next picture, now the data is in the table and could be accesible from Google Colab and Tableau.  



<p align="center"><img src="https://github.com/Marce1301/Likelihood_of_defaulting_credit_card_payments/blob/main/Other_Stuff/Images_README/SELECT.png" /></p>

To get SQL scripts used, go to this link:

link

Copyright:copyright: 2023. All Rights Reserved.

© 2023  Lozano Alonso ,Silva Aldo, Espinosa Alejandra, Maldonado Marcela , BootCamp Tecnologico de Monterrey.
