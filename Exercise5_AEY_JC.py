import pandas
print("Question1")
#Question 1 Part 1
wages=pandas.read_csv("wages.csv",header=0,sep=",")
reduced=wages[['gender', 'yearsExperience']]
sorted1=reduced.sort_values(['gender', 'yearsExperience'], ascending=[True, False])
done=sorted1.drop_duplicates()
print(done)

#Question 1 Part 2
wages = pandas.read_csv("wages.csv")
gender_Experience=wages[["gender","yearsExperience"]]
ordered_gender_Experience=gender_Experience.sort(['gender','yearsExperience'], ascending=[True,True])
unique_combos=ordered_gender_Experience.drop_duplicates()
print("Unique combinations of gender/years experience:", unique_combos)

print("Question2")
# Question 2 part 1
import pandas
ex5data=pandas.read_csv("wages.csv")
sorted1=ex5data.drop('yearsSchool', axis=1, inplace=True)
sorted2=ex5data.sort_values("wage")
duplicates=sorted2.drop_duplicates("wage")
part1=duplicates.tail(1)
print("Highest earner", part1)

# Question 2 part 2
import pandas
ex5data=pandas.read_csv("wages.csv")
sorted1=ex5data.drop('yearsSchool', axis=1, inplace=True)
sorted2=ex5data.sort_values("wage")
duplicates=sorted2.drop_duplicates("wage")
part2=duplicates.head(1)
print("Lowest earner", part2)

# Question 2 part 3
import pandas
ex5data=pandas.read_csv("wages.csv")
sorted1=ex5data.sort_values("wage")
duplicates=sorted2.drop_duplicates("wage")
top10=duplicates.tail(10)
top10.to_csv("top10.csv")
total = 0
with open('top10.csv') as f:
    for line in f:
        finded = line.find('female')
        if finded != -1 and finded != 0:
            total += 1
print("Number of women in the top 10 earners", total)

print("Question3")
#Question 3
wages_highschool = wages[wages.yearsSchool == 12]
wages_college = wages[wages.yearsSchool == 16]
ordered_wages_HS = wages_highschool.sort(columns='wage', ascending=True)
ordered_wages_C = wages_college.sort(columns='wage', ascending=True)
minWage_HS = ordered_wages_HS.iloc[0,3]
minWage_C= ordered_wages_C.iloc[0,3]
print("Effect of graduating college on minimum wage:", minWage_C - minWage_HS)
