# Discord Server Maker
Make discord server by Coding!



# FAQ
1. How can i get role permissons?
- Open discord with chrome developer tool, go to network and click red circle to it turn to gray. make a new role and edit permisson that you want. Now click again to the circle go red and click "save" to save role permisson. And then click on the tab write server id and scroll down click copy permisson

# Documentation:
## I. Server system
#### "name" - name for the server.
#### "icon" - set server icon (as base64 encode).
#### "system_channel_id" - set the system default anouncements channel.
#### "channels" - add channel into server
#### "roles" - add roles into server
#### 	"guild_template_code" - default discord template code

## II. Channel
### - Channel Type:
#### 1: Text channel
#### 2: Voice Channel
#### 4: Category

### tag:
#### "id" for channel position in server (useful for category)
#### "parent_id" for channel position in category (category need to set it as null)
