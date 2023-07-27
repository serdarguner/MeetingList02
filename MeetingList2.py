import webbrowser
from msal import ConfidentialClientApplication, PublicClientApplication
client_secret="Np78Q~A9kruyjV7EJHRDK7Q-xFtXqm8JB1a-Zafy"

app_id= "70514833-ccf1-43dd-9865-f415f9866e0a"
SCOPES=["User.Read"]
client=PublicClientApplication(client_id=app_id)
flow=client.initiate_device_flow(scopes=SCOPES)
print(flow)
webbrowser.open(flow["verification_uri"])