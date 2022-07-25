import json
import yaml

string ='''{
    "apiVersion": "v1",
    "kind": "Pod",
    "metadata": {},
    "spec": {
        "containers": [
            {
                "image": {},
                "name": {},
                "ports": [
                    {
                        "containerPort": {}
                    }
                ]
            }
        ]
    }
}
'''
data=json.loads(string)
print(data)

container_name=input("Enter the container name: ")
image=input("Enter the image: ")
container_port=int(input("Enter the container port: "))
Labels=int(input("Enter the number of label (key,value) numbers: "))

data['spec']['containers'][0]['image']=image
data['spec']['containers'][0]['name']=container_name
data['spec']['containers'][0]['ports'][0]['containerPort']=container_port

for i in range(1,Labels+1):
    key=input(f"Enter the key {i}: ")
    value=input(f"Enter the value {i}: ")
    data['metadata'].update({f"{key}":f"{value}"})
print(data)


with open('final.json','a') as f:
    json.dump(data,f,indent=2)

with open("final.yaml", "w", encoding="utf-8") as o:
	yaml.dump(data, o)