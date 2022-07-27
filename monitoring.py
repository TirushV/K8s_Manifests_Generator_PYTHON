import requests

list=['https://signup.zistaeducation.com/','https://kloudmate.dev','https://kloudmate.com','https://google.com']
list2=['https://sample.com','https://graphql.kloudmate.dev/','https://example.com']

for i in list:
    response=requests.get(i)
    x=response.status_code
    if x==200:
        continue
    else:
        print(f"{i} was returning {x}.")