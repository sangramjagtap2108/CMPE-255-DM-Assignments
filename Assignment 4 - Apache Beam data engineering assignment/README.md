# Assignment 1 - D3.js Visualizations for Housing Dataset
This project provides visual insights into a housing dataset using D3.js, a powerful JavaScript library for producing dynamic, interactive data visualizations.   

Overview:   
Using the housing dataset, we derived insights and visualized the data using two primary charts:   
Bar Chart: Represents the average sale price based on sale condition.    
Scatter Plot: Displays the relationship between living area (GrLivArea) and sale price (SalePrice).    

Setup:   
I have implemented the assignment by 2 ways -  
1. In google colab using IPython.core.display to display D3 visualization in google colab.

Output -   
![Screenshot (71)](https://github.com/sangramjagtap2108/CMPE-255-DM-Assignments/assets/55223872/9902b917-f100-4d32-a757-610bb86a57ee)

![Screenshot (72)](https://github.com/sangramjagtap2108/CMPE-255-DM-Assignments/assets/55223872/74d5c1ba-8005-47ae-b11b-e1dd608b500f)

2. Implemented in separate js,html,css files on local system and display visualizations in browser(Attached all files in repo)

Output -  
![Screenshot (70)](https://github.com/sangramjagtap2108/CMPE-255-DM-Assignments/assets/55223872/7c2c7e46-89e8-4191-a93f-3b2406d21243)

# Assignment 2 - Automated EDA using Sweetviz   
Sweetviz is an open-source Python library that generates beautiful, high-density visualizations to kickstart EDA (Exploratory Data Analysis) with just a single line of code. The output is a fully self-contained HTML application.

Steps -   
1.Installation  
2.Importing the Necessary Libraries  
3.Loading Your Dataset   
4.Generating the Report   
5.Displaying the Report   
6.Interpreting the Report   
  The report will present a visual comparison between numerical and categorical features.   
  For each feature, you'll see its distribution, correlations, missing values, and other statistics.   
  The interactive nature of the report allows you to hover over elements to see more details.     
7.Additional Features - 
  Comparing two datasets   
  Target Analysis - To analyze a dataset against a specific target column (e.g., "SalePrice")   

# Assignment 3 - Apache Beam Features Demonstration    
Apache Beam allows you to express complex data processing workflows. Some core concepts include:   
Pipeline: A sequence of data processing stages.   
PCollection: Represents a distributed dataset.   
PTransform: Represents a data processing operation.   
ParDo: A parallel processing operation, similar to "map" in MapReduce.    
Windowing: Splits a PCollection into "windows" of data.   
Triggers: Determines when to emit the results of a windowed PCollection.   
Composite Transforms: Composite Transforms bundle multiple transformations under a single named operation, enhancing readability and modularity.     





