import webbrowser
from msal import ConfidentialClientApplication, PublicClientApplication
client_secret="Np78Q~A9kruyjV7EJHRDK7Q-xFtXqm8JB1a-Zafy"

app_id= "70514833-ccf1-43dd-9865-f415f9866e0a"
SCOPES=["User.Read"]
client= ConfidentialClientApplication(client_id=app_id,client_credential=client_secret)
authorization_url=client.get_authorization_request_url(SCOPES)
webbrowser.open(authorization_url)
authorization_code = "M.C106_BL2.2.fac9850a-2ec6-620b-f443-5048f3779c8d"
access_token=client.acquire_token_by_authorization_code(code=authorization_code,scopes=SCOPES)
access_token_id=access_token["access_token"]
print(access_token_id)
