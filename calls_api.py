import requests

company = requests.get("http://localhost:5000/companies-data").json()
print(type(company))
print(company)

test_company_id = requests.post("http://localhost:5000/companies-data/purify", data={"id": 1234})
