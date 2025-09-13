import pandas as pd
data=[
    {"Title":"Python 101","Price":29.99,"Rating":5},
    {"Title":"Learn Pandas","Price":23.99,"Rating":4},
    {"Title":"Web Scraping guide","Price":19.99,"Rating":4},
    {"Title":"ML Basics","Price":34.99,"Rating":3},
    {"Title":"Data Scrience","Price":39.99,"Rating":5},
]

df=pd.DataFrame(data)
print(df)

high_rated=df[df["Rating"]>=4]
print(high_rated)

# Sorting
sorted_df = df.sort_values(by="Price") #asc
print(sorted_df)
sorted_df = df.sort_values(by="Price",ascending=False) #desc
print(sorted_df)

#Add new column
df["Price_USD"]=df["Price"]*1.35
print(df)

# Average
print("Average Price: ",df["Price"].mean())
print("Average Rating: ",df["Rating"].mean())

#Filter Data with price less that 30
# Store them in csv file
under_thirty=df[df["Price"]<30]
under_thirty.to_csv('underthiry.csv',index=False)