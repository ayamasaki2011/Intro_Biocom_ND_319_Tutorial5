print("Highest earner")
import pandas
ex5data=pandas.read_csv("wages.csv")
sorted1=ex5data.drop('yearsSchool', axis=1, inplace=True)
sorted2=ex5data.sort_values("wage")
duplicates=sorted2.drop_duplicates("wage")
duplicates.tail(1)

