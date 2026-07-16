import pandas as pd

nums=[1,2,3,4,5];
pdval = pd.Series(nums);
print(pdval)

# setting with the default index
pdidxval = pd.Series(nums,index=[11,12,13,14,15])
print(pdidxval);

# dataframes are used to setup the column Names

data=[
    ['marry','maria','deva'],
    ['sandeep','vijji','jhumma'],
    ['deva','vijj','venu']
];

columnname = pd.DataFrame(data,columns=['firstname','middlename','lastname']);
print(columnname)

# we are using the dictionary 
data1={
    'name':['jagauu','morry'],
    'firstname':['deva','manni'],
    'lastname':['deva','manni'],
}

print(data1);



# Reading the CSV File
pdcsv = pd.read_csv('weight-height.csv');
print(pdcsv)

# we can get the 5 rows using the head
print(pdcsv.head());

# we can get the last five rows using the tail
print(pdcsv.tail());

# shape are used to get the shape of the value
# total count & how mny column we can get using the shape
print(pdcsv.shape)


# let us get all the columns using the columns
# print(pdcsv.columns)

# fething the specic column using the column names
# print(pdcsv['Gender'])

# describe will give the statstical information of the data

print(pdcsv.describe())
heights = pdcsv['Height'];
print(heights)