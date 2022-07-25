import json
import yaml
import os

string='''{
    "apiVersion": "apps/v1",
    "kind": "Deployment",
    "metadata": {
        "labels": {}
    },
    "spec": {
        "replicas": {},
        "selector": {
            "matchLabels": {}
        },
        "strategy": {
            "type": "RollingUpdate"
        },
        "template": {
            "metadata": {
                "labels": {}
            },
            "spec": {
                "containers": [
                    {
                        "image": {},
                        "name": {},
                        "env": [],
                        "ports": [
                            {
                                "containerPort": {},
                                "name": {}
                            }
                        ],
                        "volumeMounts": []
                    }
                ],
                "volumes": []
            }
        }
    }
}
'''

data=json.loads(string)
print(data)



container_name=input("Enter the container name: ")
image=input("Enter the image name: ")
container_port=int(input("Enter the container port: "))
replicas=int(input("Enter the replicas count: "))
port_name=input("Enter the port name: ")
metadata_key=input("Enter the metadata key: ")
metadata_value=input("Enter the metadata value: ")


env=bool(int(input("Do you have any ENV variables to be defined (True/False): ")))
if env==True:
    env_num=int(input("Enter the number of ENV: "))
    for j in range(1,env_num+1):
        env_key=input("Enter the env name: ")
        env_value=input("Enter the env value: ")
        data['spec']['template']['spec']['containers'][0]['env'].append({"name":f"{env_key}","value":f"{env_value}"})
else:
    pass


volumeMounts=bool(int(input("Do you have any volume mounts to be defined (True/False): ")))
if volumeMounts==True:
    volumecount=int(input("Enter the number of volume mounts: "))
    for k in range(1,volumecount+1):
        volume_name=input("Enter the volume name: ")
        mountpath=input("Enter the mount path of the volume: ")
        data['spec']['template']['spec']['containers'][0]['volumeMounts'].append({"name":f"{volume_name}","mountPath":f"{mountpath}"})
else:
    pass

persistentvolume=bool(int(input("Do you want to create Persistent volume (True/False): ")))
if persistentvolume==True:
    containervolumes=int(input("Enter the number of persistent volume: "))
    for i in range(1,containervolumes+1):
        volumeName=input("Enter the container volume name: ")
        persistance=input("Enter the peristance volume claim name: ")
        data['spec']['template']['spec']['volumes'].append({"name":f"{volumeName}","persistentVolumeClaim": {"claimName":f"{persistance}"}})
else:
    pass

configmapvolume=bool(int(input("Do you want to create configmap volume (True/False): ")))
if configmapvolume==True:
    #confimapcount=int(input("Enter the configmap count: "))
    configvolumename=input("Enter the configmap volume name: ")
    configmapname=input("Enter the configmap name: ")
    data['spec']['template']['spec']['volumes'].append({"name":f"{configvolumename}","configMap": {"name":f"{configmapname}"}})
else:
    pass

secretvolume=bool(int(input("Dp you want to create secret as volume: ")))
if secretvolume==True:
    secretcount=int(input("Enter the secret count: "))
    secretvolumename=input("Enter the secret volume name")
    secretname=input("Enter the secrete name: ")
    data['spec']['template']['spec']['volumes'].append({"name":f"{secretvolumename}","secret": {"secretName":f"{secretname}"}})
else:
    pass

data['spec']['replicas']=replicas
data['spec']['template']['spec']['containers'][0]['name']=container_name
data['spec']['template']['spec']['containers'][0]['image']=image
data['spec']['template']['spec']['containers'][0]['ports'][0]['containerPort']=container_port
data['spec']['template']['spec']['containers'][0]['ports'][0]['name']=port_name
data['metadata'].update({f"{metadata_key}":f"{metadata_value}"})

Labels=int(input("Enter the number of label (key,value) numbers: "))

for i in range(1,Labels+1):
    key=input(f"Enter the key {i}: ")
    value=input(f"Enter the value {i}: ")
    data['metadata']['labels'].update({f"{key}":f"{value}"})
    data['spec']['selector']['matchLabels'].update({f"{key}":f"{value}"})
    data['spec']['template']['metadata']['labels'].update({f"{key}":f"{value}"})

if data['spec']['template']['spec']['containers'][0]['env']==[]:
    del data['spec']['template']['spec']['containers'][0]['env']

if data['spec']['template']['spec']['containers'][0]['volumeMounts']==[]:
    del data['spec']['template']['spec']['containers'][0]['volumeMounts']

if data['spec']['template']['spec']['volumes']==[]:
    del data['spec']['template']['spec']['volumes']

with open('deployment.json','a') as f:
    json.dump(data,f,indent=2)

with open("deployment.yaml", "w", encoding="utf-8") as o:
	yaml.dump(data, o)

# run=bool(int(input("Do you want to run the deployment file (True-/False-0) ? ")))
# if run==True:
#     os.system("kubectl apply -f deployment.yaml")
# else:
#     os.system("dir")