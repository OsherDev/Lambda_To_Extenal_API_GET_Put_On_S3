#First of all need to add a layer with request package with pip install.
#mkdir lambda_layers
#cd lambda_layers
#mkdir python
#cd python
#pip install requests -t ./
#cd ..
#zip -r python_modules.zip .

import json
import boto3
import requests
import os

access_key = os.environ["Access_Key"]

def lambda_handler(event, context):
    #Var
    access_key = os.environ["Access_Key"]
    # URL
    url = f'SOME_URLaccess_key={access_key}'
    response = requests.get(url)
    json = response.json()
