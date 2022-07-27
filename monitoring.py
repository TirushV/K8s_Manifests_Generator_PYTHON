import requests

list=['https://signup.zistaeducation.com/','https://kloudmate.dev','https://kloudmate.com','https://google.com']
list2=['https://udemy.com','https://sample.com','https://graphql.kloudmate.dev/','https://example.com']

for i in list2:
    response=requests.get(i,timeout=5)
    x=response.status_code
    try:
        if x==200:
            continue
        else:
            print(f"{i} was returning {x}.")
    except:
        print(f"{i} request timeout")