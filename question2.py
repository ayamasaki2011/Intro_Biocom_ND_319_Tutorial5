print("Highest earner")
import pandas
ex5data=pandas.read_csv("wages.csv")
sorted1=ex5data.drop('yearsSchool', axis=1, inplace=True)
sorted2=ex5data.sort_values("wage")
duplicates=sorted2.drop_duplicates("wage")
part1=duplicates.tail(1)
print(part1)

print("Lowest earner")
import pandas
ex5data=pandas.read_csv("wages.csv")
sorted1=ex5data.drop('yearsSchool', axis=1, inplace=True)
sorted2=ex5data.sort_values("wage")
duplicates=sorted2.drop_duplicates("wage")
part2=duplicates.head(1)
print(part2)

print("Number of women in the top 10 earners")
import pandas
ex5data=pandas.read_csv("wages.csv")
sorted1=ex5data.sort_values("wage")
duplicates=sorted2.drop_duplicates("wage")
top10.txt=duplicates.tail(10)
top10.to_csv("top10.csv")
total = 0
with open('top10.csv') as f:
    for line in f:
        finded = line.find('female')
        if finded != -1 and finded != 0:
            total += 1
print(total)
