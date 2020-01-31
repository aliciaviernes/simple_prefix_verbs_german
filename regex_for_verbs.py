import re

f = open('verbs.csv', 'rt')
verbs = f.read()
f.close()


p = re.compile('be.+en')
for match in p.finditer(verbs):
    print(match.group())

p = re.compile('ent.+en')
for match in p.finditer(verbs):
    print(match.group())

p = re.compile('er.+en')
for match in p.finditer(verbs):
    print(match.group())

p = re.compile('ge.+en')
for match in p.finditer(verbs):
    print(match.group())

p = re.compile('miss.+en')
for match in p.finditer(verbs):
    print(match.group())

p = re.compile('ver.+en')
for match in p.finditer(verbs):
    print(match.group())

p = re.compile('zer.+en')
for match in p.finditer(verbs):
    print(match.group())


    