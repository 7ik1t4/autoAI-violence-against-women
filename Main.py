# change payload here
payload_scoring = {"input_data": [{"fields": ["Country","Gender","Demographics Question","Demographics Response","Question"],"values": [['Afghanistan','F','Education','Higher','if she burns the food']]}]}


import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "63eh_vHzuR51Ei-LqxPCNZxVaj37JumbDMW7JrtmDFaG"

token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

response_scoring = requests.post('https://jp-tok.ml.cloud.ibm.com/ml/v4/deployments/3ba1e584-72a6-433f-ba28-201368f21d2f/predictions?version=2021-04-30', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
print(response_scoring.json())