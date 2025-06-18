def newfanta(family):
    return list(filter(lambda name: family[name] == "fanta", family.keys()))

dupont_family = {
    "fanta": "fanta",
    "new": "new",
    "kewalin": "fanta",
    "sekhamphan": "fanta",
    "monruedi": "first",
}

print(newfanta(dupont_family))