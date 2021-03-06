import requests
import os

null = None
true = True
false = False

token = ""
icon = open("icons/StickbugGif.txt", "r").read()

maker = requests.post('https://discord.com/api/v9/guilds', headers={'authorization': token}, json=
	{
	"name":"Example", 
	"icon": icon, 
	"channels": 
		[
			{
			"id":"00", 
			"parent_id": null, 
			"name": "INFOMATION", 
			"type": "4"
			},

			{
			"id": "01", 
			"parent_id": "00", 
			"name": "welcome", 
			"type": "0"
			},

			{
			"id": "02", 
			"parent_id": "00", 
			"name": "announcements", 
			"type": "0"
			},

			{"id": "03", 
			"parent_id": "00", 
			"name": "rules", 
			"type": "0"
			},

			{
			"id": "10", 
			"parent_id": null, 
			"name": "MAIN", 
			"type": "4"
			},

			{
			"id": "11", 
			"parent_id": "10", 
			"name": "general-chat", 
			"type": "0"
			},

			{
			"id": "12", 
			"parent_id": "10", 
			"name": "memes", 
			"type": "0"
			},

			{
			"id": "13",
			"parent_id": "10",
			"name": "commands",
			"type": "0"
			},

			{
			"id": "20",
			"parent_id": null,
			"name": "VOICE CHANNELS",
			"type": "4"
			},

			{
			"id": "21",
			"parent_id": "10",
			"name": "Voice Chat",
			"type": "0"
			},

			{
			"id": "22", 
			"parent_id": "20",
			"name": "Meeting Room 1",
			"type": "2"
			},

			{
			"id": "23",
			"parent_id": "20",
			"name": "Meeting Room 2",
			"type": "2"
			},

			{
			"id": "24",
			"parent_id": "20",
			"name": "Streaming",
			"type": "2"
			}
		],
	"system_channel_id": "02",
	"roles":
		[
			{
			"id": "00",
			"name": "@everyone",
			"permissions": "1071698660929"
			},

			{
			"id": "03",
			"name": "Admin",
			"mentionable": false,
			"hoist": true,
			"permissions": "1090921693183",
			"color": "0"
			},

			{
			"id": "02",
			"name": "Moderator",
			"mentionable": true,
			"hoist": true,
			"permissions": "1089042120519",
			"color": "11027200"
			},

			{
			"id": "01",
			"name": "Member",
			"mentionable": true,
			"hoist": true,
			"permissions": "1071698534209",
			"color": "2490112"
			}

		],
	"guild_template_code": null
	}
)

if maker.status_code == 201:
	print("Successfully make server")
else:
	print(f"Failed ERROR {maker.status_code}")
