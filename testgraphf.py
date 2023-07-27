import asyncio

from azure.identity.aio import ClientSecretCredential

credential = ClientSecretCredential("tenantID",
                                    "clientID",
                                    "clientSecret")
scopes = ['https://graph.microsoft.com/.default']