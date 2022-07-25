import json
import yaml

string ='''{
    "kind": "Service",
    "apiVersion": "v1",
    "metadata": {
        "labels": {}
    },
    "spec": {
        "selector": {},
        "ports": [
            {
                "port": {},
                "protocol": {}
            }
        ],
        "type": {}
    }
}
'''

data=json.loads(string)
print(data)

protocol=input("Enter the protocol: ")
port=int(input("Enter the container port: "))
Type=input("Enter the service type (Loadbalancer, ClusterIP, NodePort): ")
metadata_key=input("Enter the metadata key: ")
metadata_value=input("Enter the metadata value: ")
Labels=int(input("Enter the number of label (key,value) numbers: "))


data['spec']['ports'][0]['port']=port
data['spec']['ports'][0]['protocol']=protocol
data['spec']['type']=Type
data['metadata'].update({f"{metadata_key}":f"{metadata_value}"})

for i in range(1,Labels+1):
    key=input(f"Enter the key {i}: ")
    value=input(f"Enter the value {i}: ")
    data['metadata']['labels'].update({f"{key}":f"{value}"})
    data['spec']['selector'].update({f"{key}":f"{value}"})

print(data)

with open('service.json','a') as f:
    json.dump(data,f,indent=2)

with open("service.yaml", "w", encoding="utf-8") as o:
	yaml.dump(data, o)