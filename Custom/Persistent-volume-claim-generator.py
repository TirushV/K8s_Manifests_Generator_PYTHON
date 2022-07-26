import json
import yaml

string='''
{
    "apiVersion": "v1",
    "kind": "PersistentVolumeClaim",
    "metadata": {
        "name": {},
        "labels": {}
    },
    "spec": {
        "accessModes": [],
        "storageClassName: {}
        "resources": {
            "requests": {
                "storage": {}
            }
        }
    }
}
'''

data=json.loads(string)
print(data)

name=input("Enter the name of the PersistentVolumeClaim: ")
access=input("Enter the accessmode: ")
storage=input("Enter the storage class name:")
capacity=input("Define the size/capacity: ")
Labels=int(input("Enter the number of label (key,value) numbers: "))

data['metadata']['name']=name
data['spec']['accessModes'].append(access)
data['spec']['resources']['requests']['storage']
data['spec']['resources']['storageClassName']=storage

for i in range(1,Labels+1):
    key=input(f"Enter the key {i}: ")
    value=input(f"Enter the value {i}: ")
    data['metadata']['labels'].update({f"{key}":f"{value}"})
print(data)


with open('final.json','a') as f:
    json.dump(data,f,indent=2)

with open("final.yaml", "w", encoding="utf-8") as o:
	yaml.dump(data, o)