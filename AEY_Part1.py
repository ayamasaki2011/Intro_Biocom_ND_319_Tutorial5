import pandas

wages = pandas.read_csv("wages.csv")

gender_Experience=wages[["gender","yearsExperience"]]

ordered_gender_Experience=gender_Experience.sort(['gender','yearsExperience'], ascending=[True,True])

unique_combos=ordered_gender_Experience.drop_duplicates()