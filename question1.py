#import pandas. read the csv. read the two columns. sort by both columns in order. drop duplicates. print.
import pandas
wages=pandas.read_csv("wages.csv",header=0,sep=",")
reduced=wages[['gender', 'yearsExperience']]
sorted1=reduced.sort_values(['gender', 'yearsExperience'], ascending=[True, False])
done=sorted1.drop_duplicates()
print(done)



