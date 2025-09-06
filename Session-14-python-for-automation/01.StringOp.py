#Creating String
str1= 'Hello'
str2= 'World'
str3= '''
        this is
        multiline String..
'''

print(str3)

# String Concatenation
greeting=str1+" "+str2
print(greeting)
# F String to print multiple variables
num1=10
num2=20
print(f"{num1} + {num2} = {num1+num2}") # 10 + 20 = 30

## Reapeat String
print((str1+" ")*3)

## String Slicing
print(str1[0:4]) #Hell
print(str1[2:]) #llo

# String Length
print(f"Length of String 1: {len(str1)}")

# Change case
print(f'Uppercase: {str1.upper()}')
print(f'Lowercase: {str1.lower()}')

#Replace
print(str1.replace("H","W"))

## Search
print("lo" in str1) # check if its present in str or not
print(str1.find('lo')) #give starting Index

## Split and Join
statement="my name is sonam soni and i am a content creator"
words=statement.split()
print(words)# array or all words
print("-".join(words))

##Check starts with and ends with
print("Python".startswith("Py"))
print("Python".endswith("on"))

#Statement
# write logic to capitalize each word first letter.

result=''
for i in words:
    result+= i.capitalize()+" "
print(result)

print(statement.title())

# Center 
text="Python"
print(text.center(30,"*"))

## Another Way
result = " ".join(word[0].upper() + word[1:] for word in statement.split())
print(result)
