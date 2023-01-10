import requests

company = requests.get("http://localhost:5000/1").json()
print(type(company))
print(company)
