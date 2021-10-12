import requests
import os

file = open("ServerConfig.txt", "r")
server_template = file.read()

token = ""

maker = requests.post('https://discord.com/api/v9/guilds', headers={'authorization': token}, json=server_template)
if maker.status_code == 201:
	print("Successfully make server")
else:
	print(f"Failed ERROR {maker.status_code}")
