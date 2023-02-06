import time
import requests
import re
import json


data = requests.get("http://localhost:5000/api/companies-data").json()
companies = data[0]
columns = data[1]


def clean_names():
    """
        A function that lists through company names and cleans legal entity suffixes,
    parentheses with text, and dots from them.
    :return: list of names
    """
    r = re.compile("[(].*?[)]")
    s = re.compile("[.]$")
    t = re.compile("plc", flags=re.IGNORECASE)
    u = re.compile("c[.]i[.]c", flags=re.IGNORECASE)
    v = re.compile("llp", flags=re.IGNORECASE)
    w = re.compile("uk|u[.]k[.]", flags=re.IGNORECASE)
    x = re.compile("limited", flags=re.IGNORECASE)
    y = re.compile("ltd", flags=re.IGNORECASE)
    z = re.compile("ltd.", flags=re.IGNORECASE)
    names = [i[1].lower() for i in companies]

    for i, j in enumerate(names):
        # j = j.replace("-", "") if bool(j.find("-")) else j

        j = r.sub("", j) if bool(r.search(j)) else j

        j = s.sub("", j) if bool(s.search(j)) else j

        j = t.sub("", j) if bool(t.search(j)) else j

        j = u.sub("", j) if bool(u.search(j)) else j

        j = v.sub("", j) if bool(v.search(j)) else j

        j = w.sub("", j) if bool(w.search(j)) else j

        j = x.sub("", j) if bool(x.search(j)) else j

        j = y.sub("", j) if bool(y.search(j)) else j

        j = z.sub("", j) if bool(z.search(j)) else j

        j = " ".join(j.split()).title()

        names[i] = j

    return names


def write_data(cleaned_data):
    """
        A function that takes cleaned names data as an argument then writes the new company data in a mongodb database
    :param cleaned_data:
    :type: list
    :return: Response
    """
    all_data = []
    for i, j in enumerate(companies):
        new_data = {
            cleaned_data[i]: {
                columns[0]: j[0],
                columns[2]: j[2],
                columns[3]: j[3],
                columns[4]: j[4],
                columns[5]: j[5],
            }
        }

        all_data += [new_data]
    else:
        req = requests.post("http://localhost:5000/api/companies-data/purify", json=json.dumps(all_data))
        return req


t1 = time.process_time()
names1 = clean_names()
t2 = time.process_time()
print(f"function {clean_names.__name__} took {t2 - t1}")

t3 = time.process_time()
write_data(names1)
t4 = time.process_time()
print(f"function {write_data.__name__} took {t4 - t3}")
