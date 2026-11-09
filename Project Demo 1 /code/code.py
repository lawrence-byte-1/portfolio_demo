‎##We first import the tools that we need
‎
‎import pandas as pd
‎import matplotlib.pyplot as plt
‎
‎## Stage A, The spreadsheet Output
‎## 1. I created a variable where we will import out file from the directory "data", asiging "read_csv" as the file was a csv
‎
‎data_1 = pd.read_csv('../data/employee_dataset_example.csv')
‎
‎
‎## 2. A variable assigned with a value to drop the N/A
‎
‎cleaned_data_1 = data_1.dropna()
‎
‎
‎##3. A function where we export our data to a directory with index's boolean as False to remove unnecesary data/column
‎
‎cleaned_data_1.to_csv('../output/spreadsheet_result_1.csv', index=False)
‎
‎
‎## Stage B, The Data Visualization
‎##1. I established a variable that only grabs the column "name" and "monthly salary", out desired targets from the cleaned data, so MatPlotLib will avoid possible confusion
‎
‎chart_data = cleaned_data_1[['name', 'monthly_salary']]
‎
‎
‎##2. I created variables where a figure creates our canva for visualization, we are using bar here as plt.bar suggest with the parameters x, y (our targets), and we gave the table a title, xlabel, ylabel. And finally, we use xsticks to rotate 90 degree to avoid string overlays and tight_layout to fix the space issue
‎
‎plt.figure(figsize=(10,6))
‎plt.bar(chart_data['name'], chart_data['monthly_salary'])
‎plt.title("Salary Bar Graph")
‎plt.xlabel("Worker's Name")
‎plt.ylabel("Salary")
‎plt.xticks(rotation=90, fontsize=8)
‎plt.tight_layout()
‎
‎
‎##3. And lastly, A function where we export the image into our desired directory
‎
‎plt.savefig("../output/visualization_result_1.png")
