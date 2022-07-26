import json
import yaml

string='''{
    "apiVersion": "storage.k8s.io/v1",
    "kind": "StorageClass",
    "metadata": {},
    "provisioner": {},
    "volumeBindingMode": {}
}
'''

data=json.loads(string)
print(data)

metadata_key=input("Enter the metadata key: ")
metadata_value=input("Enter the metadata value: ")
bindingmode=input("Enter the binding mode type: ")

provisioner_bool=bool(int(input("Do you want to enter provisioner type as EBS? ")))
if provisioner_bool==True:
    data['provisioner']="ebs.csi.aws.com"
else:
    del data['provisioner']


data['metadata'].update({f"{metadata_key}":f"{metadata_value}"})
data['volumeBindingMode']=bindingmode


with open('final.json','a') as f:
    json.dump(data,f,indent=2)

with open("final.yaml", "w", encoding="utf-8") as o:
	yaml.dump(data, o)