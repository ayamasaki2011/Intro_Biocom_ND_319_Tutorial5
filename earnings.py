import pandas

#Part 1
wages=pandas.read_csv("wages.csv",header=0,sep=",")
reduced=wages[['gender', 'yearsExperience']]
sorted1=reduced.sort_values(['gender', 'yearsExperience'], ascending=[True, False])
done=sorted1.drop_duplicates()
print(done)

#Part 2
wages = pandas.read_csv("wages.csv")
gender_Experience=wages[["gender","yearsExperience"]]
ordered_gender_Experience=gender_Experience.sort(['gender','yearsExperience'], ascending=[True,True])
unique_combos=ordered_gender_Experience.drop_duplicates()
print("Unique combinations of gender/years experience:", unique_combos)

#Part 3
wages_highschool = wages[wages.yearsSchool == 12]
wages_college = wages[wages.yearsSchool == 16]
ordered_wages_HS = wages_highschool.sort(columns='wage', ascending=True)
ordered_wages_C = wages_college.sort(columns='wage', ascending=True)
minWage_HS = ordered_wages_HS.iloc[0,3]
minWage_C = ordered_wages_C.iloc[0,3]
print("Effect of graduating college on minimum wage:", minWage_C - minWage_HS)

