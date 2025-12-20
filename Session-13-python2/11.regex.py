import re
text = "Contact me at dev@pw.live.com or admin@pw.org or sonam-testing@co.in"

pattern= r"[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]{2,3}"

emails= re.findall(pattern,text)

print(emails)

