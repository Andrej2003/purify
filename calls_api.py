import time
import requests
import re

from cleanco import cleanco

companies_data = requests.get("http://localhost:5000/companies-data").json()


def clean_names():
    u = re.compile("company", flags=re.IGNORECASE)
    v = re.compile("llp", flags=re.IGNORECASE)
    w = re.compile("uk", flags=re.IGNORECASE)
    x = re.compile("limited", flags=re.IGNORECASE)
    y = re.compile("ltd", flags=re.IGNORECASE)
    z = re.compile("ltd.", flags=re.IGNORECASE)
    names = [i[1].lower() for i in companies_data]

    for i, j in enumerate(names):
        if bool(u.search(j)):
            names[i] = j.replace(u.search(j).group(), "").strip().strip("()").title()

        if bool(v.search(j)):
            names[i] = j.replace(v.search(j).group(), "").strip().strip("()").title()

        if bool(w.search(j)):
            names[i] = j.replace(w.search(j).group(), "").strip().strip("()").title()

        if bool(x.search(j)):
            names[i] = j.replace(x.search(j).group(), "").strip().strip("()").title()

        if bool(y.search(j)):
            names[i] = j.replace(y.search(j).group(), "").strip().strip("()").title()

        if bool(z.search(j)):
            names[i] = j.replace(z.search(j).group(), "").strip().strip("()").title()

    return names


def clean_names2():
    names = [i[1] for i in companies_data]
    for i, j in enumerate(names):
        x = cleanco(j)
        names[i] = x.clean_name()

    return names

    # data = {"id": i[0],
    #         "name": i[1],
    #         "country_iso": i[2],
    #         "city": i[3],
    #         "nace": i[4],
    #         "website": i[5], }
    # print(data)


# cleaning the data without cleanco
t1 = time.process_time()
names1 = clean_names()
t2 = time.process_time()
# faster but data is partially cleaned, also limited to only a few legal entities
print(f"function {clean_names.__name__} took {t2 - t1}")


# cleaning the data using cleanco
t3 = time.process_time()
names2 = clean_names2()
t4 = time.process_time()
print(f"function {clean_names2.__name__} took {t4 - t3}")  # slower than function custom function clean_names

counted = 0
miss = []
for i in range(len(names1)):
    if names1[i].title() == names2[i].title():
        counted += 1
    else:
        miss += [(names1[i], names2[i])]
else:
    print(counted)
    print(len(miss))
    print(miss)


# test_company_id = requests.post("http://localhost:5000/companies-data/purify", data={"id": 1234})
