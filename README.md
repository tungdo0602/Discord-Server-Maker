# Discord Server Maker
Make discord server by Coding!



# FAQ
1. How can i get role permissons?
- Open discord with chrome developer tool, go to network and click red circle to it turn to gray. make a new role and edit permisson that you want. Now click again to the circle go red and click "save" to save role permisson. And then click on the tab write server id and scroll down click copy permisson

# Documentation:
## I. Server system
### Tag:
#### "name" - name for the server.
#### "icon" - set server icon (as base64 encode).
#### "system_channel_id" - set the system default anouncements channel.
#### "channels" - add channel into server.
#### "roles" - add roles into server.
#### 	"guild_template_code" - default discord template code.

## II. Channel/Category
### Tag:
#### "name" - set name for the channel/category.
#### "id" - set channel position in server (useful for category).
#### "parent_id" set channel position in category (category need to set it as null).
#### "type" - set channel type.

### - Channel Type:
#### 1: Text channel
#### 2: Voice Channel
#### 4: Category


## III. Roles
### Tag:
"id" - set role position.
"name" - set role name.
"mentionable" - let user mention that role or not.
"hoist" - let role can be see at member list or not.
"permissions" - set role permission.
"color" - set role color.
"icon" - set role icon
"unicode_emoji" - ???

#### !(https://github.com/tungdo0602/Discord-Server-Maker/blob/main/.github/1.png "example")

Example:
```json
	{
	"name":"Example", 
	"icon": null, 
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
```
