import time
import requests
import re
import json
from cleanco import cleanco
data = requests.get("http://localhost:5000/companies-data").json()
companies = data[0]
columns = data[1]


def clean_names():
    r = re.compile("[(].*?[)]")
    s = re.compile("[.]$")
    t = re.compile("plc", flags=re.IGNORECASE)
    u = re.compile("company", flags=re.IGNORECASE)
    v = re.compile("llp", flags=re.IGNORECASE)
    w = re.compile("uk|u[.]k[.]", flags=re.IGNORECASE)
    x = re.compile("limited", flags=re.IGNORECASE)
    y = re.compile("ltd", flags=re.IGNORECASE)
    z = re.compile("ltd.", flags=re.IGNORECASE)
    names = [i[1].lower() for i in companies]

    for i, j in enumerate(names):
        if bool(r.search(j)):
            j = r.sub("", j)

        if bool(s.search(j)):
            j = s.sub("", j)

        if bool(t.search(j)):
            j = j.replace(t.search(j).group(), "")

        # if bool(u.search(j)):
        #     j = j.replace(u.search(j).group(), "").strip("()").title().strip()

        if bool(v.search(j)):
            j = j.replace(v.search(j).group(), "")

        if bool(w.search(j)):
            j = j.replace(w.search(j).group(), "")

        if bool(x.search(j)):
            j = j.replace(x.search(j).group(), "")

        if bool(y.search(j)):
            j = j.replace(y.search(j).group(), "")

        if bool(z.search(j)):
            j = j.replace(z.search(j).group(), "")

        j = " ".join(j.split()).title()

        names[i] = j

    return names


def clean_names2():
    names = [i[1] for i in companies]
    for i, j in enumerate(names):
        x = cleanco(j)
        names[i] = x.clean_name()

    return names


def write_data(cleaned_data):
    all_data = []
    for i, j in enumerate(companies):
        j[1] = cleaned_data[i]
        new_data = {
            columns[0]: j[0],
            columns[1]: j[1],
            columns[2]: j[2],
            columns[3]: j[3],
            columns[4]: j[4],
            columns[5]: j[5], }

        all_data += [new_data]
    else:
        req = requests.post("http://localhost:5000/companies-data/purify", json=json.dumps(all_data))
        return req


# cleaning the data without cleanco
t1 = time.process_time()
names1 = clean_names()
t2 = time.process_time()
# faster but data is partially cleaned, also limited to only a few legal entities
print(f"function {clean_names.__name__} took {t2 - t1}")

t3 = time.process_time()
write_data(names1)
t4 = time.process_time()
print(f"function {write_data.__name__} took {t4 - t3}")
