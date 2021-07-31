# Datopian
This project was provided by Datopian as part of their technical skills test. It involved Data wrangling, chart creation and data sorting. To create and execute this dataset, three packages were used: pandas, matplotlib and csv. Pandas was used for the major work of data wrangling while matplotlib was used to create a bar graph and csv was used to create and save a csv file. 
To run/execute this project, pandas, matplotlib and csv is required. To install, run the following commands.
pip install pandas
pip install matplotlib
csv is a part of pandas package so we don't need to run any additional commands
# Code Explanation
First, I have imported the required libraries into our workspace(eg. import pandas as pd)
After importing the required packages, set the display size using pd.set_option('display.max_columns', 500)
Then, ran pd.read_html with a match condition to scrape the required datatable from the website
To confirm, I printed the number of Total Tables
After scraping, I created the pandas dataframe and named it df for easy remembrance
During creation, I ran a rename command to remove unnecessary characters from table headers a.k.a column names
Then, created a list of columns required for my exercise of data wrangling and named it reqcols
After listing all the columns required, listed the columns not required in dcol
Then, I ran df.drop() using dcol as the names list for the columns beeing dropped
After removing the unnecessary columns, the next step was cleaning the data.
That involved removing unnecessary characters, standardising the data and typecasting columns according to the data.
Then, I dropped the column Population Density to clear earlier values
Then, I created two additional lists: lpop and larea containing the area in sq. km and total population
To create new population density data, I needed to divide total population by area
So for that, I needed to convert the area from decimal to absolute numbers. To do that, I multiplied the area decimal numbers with 1000 using a for loop with a range equal to the length of larea(i in range(0, len(larea))
Before the for loop i created a list newarea to contain the absolute values of area. 
Using the for loop, I appended the data using newarea.append() command
Then, using another for loop I calculated Population density (Dp=N/A)
Then, inserted a column at position 5 and axis 1 which was the position of the column Population Density
Then, using sort_values, i sorted the data according to Road Deaths per million and created and displayed a graph using pyplot class which is a part of matplotlib (from matplotlib import pyplot as plt and plt.show())
Finally, i saved the csv using df.to_csv() which requires a savepath as argument(df.to_csv(r'C:/Users/Joel Mammen/Desktop/Datopian/CSVs/Datopian.csv')) and printed my dataframe to show my work
# Thank You
