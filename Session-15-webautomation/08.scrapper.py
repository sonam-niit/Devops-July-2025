from bs4 import BeautifulSoup
html= """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sonam Soni</title>
</head>
<body>
    <h1>Sonam Soni</h1><hr>
    <p class="info">This is my Simple Para</p>
</body>
</html>
"""
#parse HTML
soup=BeautifulSoup(html,'html.parser')
print("Title: ",soup.title.text)
print("Heading: ",soup.h1.text)
print("Paragraph: ",soup.find("p",class_="info").text)
