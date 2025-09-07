import pandas as pd
data=[
    {"Title":"Python 101","Price":29.99,"Rating":5},
    {"Title":"Learn Pandas","Price":23.99,"Rating":4},
    {"Title":"Web Scraping guide","Price":19.99,"Rating":4},
    {"Title":"ML Basics","Price":34.99,"Rating":3},
    {"Title":"Data Scrience","Price":39.99,"Rating":5},
]

df = pd.DataFrame(data)
print(df)

hight_rated = df[df["Rating"]>4]
print(hight_rated)

# sorting
sorted_df = df.sort_values(by="Price") #asc
print(sorted_df)

sorted_df_desc = df.sort_values(by="Price", ascending=False) #asc
print(sorted_df_desc)

#add new column
df["Price_USD"]=df["Price"]*1.25
print(df)