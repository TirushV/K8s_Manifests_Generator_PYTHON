import json
import yaml

string='''{
    "apiVersion": "apps/v1",
    "kind": "Deployment",
    "metadata": {
        "labels": {},
        "namespace": {}
    },
    "spec": {
        "replicas": {},
        "selector": {
            "matchLabels": {}
        },
        "template": {
            "metadata": {
                "labels": {}
            },
            "spec": {
                "containers": [
                    {
                        "name": {},
                        "image": {},
                        "ports": [
                            {
                                "containerPort": {},
                                "protocol": {}
                            }
                        ]
                    }
                ]
            }
        }
    }
}
'''

data=json.loads(string)
print(data)

protocol=input("Enter the protocol: ")
container_port=int(input("Enter the container port: "))
image=input("Enter the image: ")
container_name=input("Enter the container name: ")
replicas=int(input("Enter the replicas count: "))
metadata_key=input("Enter the metadata key: ")
metadata_value=input("Enter the metadata value: ")
namespace=input("Enter the namespace name: ")

Labels=int(input("Enter the number of label (key,value) numbers: "))

data['spec']['replicas']=replicas
data['spec']['template']['spec']['containers'][0]['name']=container_name
data['spec']['template']['spec']['containers'][0]['image']=image
data['spec']['template']['spec']['containers'][0]['ports'][0]['containerPort']=container_port
data['spec']['template']['spec']['containers'][0]['ports'][0]['protocol']=protocol
data['metadata'].update({f"{metadata_key}":f"{metadata_value}"})
data['metadata']['namespace']=namespace


for i in range(1,Labels+1):
    key=input(f"Enter the key {i}: ")
    value=input(f"Enter the value {i}: ")
    data['metadata']['labels'].update({f"{key}":f"{value}"})
    data['spec']['selector']['matchLabels'].update({f"{key}":f"{value}"})
    data['spec']['template']['metadata']['labels'].update({f"{key}":f"{value}"})

print(data)

with open('deployment.json','a') as f:
    json.dump(data,f,indent=2)

with open("deployment.yaml", "w", encoding="utf-8") as o:
	yaml.dump(data, o)