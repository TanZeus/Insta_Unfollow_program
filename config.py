from os import path
import sys
import getpass

if path.exists('config_file.txt'):
    inp = input(
        'The config file already exists, do you want to overwrite it? (Y/N)')
    inp = inp.upper()
    if inp == 'N':
        sys.exit(0)


insta_username = input("Enter username of your account : ")
insta_password = getpass.getpass()
in_s = input("Do you want to monitor followers of the same account as above?(y/n)")
if (in_s == 'y' or in_s == 'Y' ):
    username = insta_username
else:
    username = input("Enter username of your original account (whose followers you want to monitor) : ")

ufforuf = input("Do you want to turn on UNFOLLOW_FOR_UNFOLLOW ?(y/n)")
fof = input("Do you want to turn on FOLLOW_FOR_FOLLOW?(y/n)")

discord_webhook_url = input("Enter your discord webhook URL : ")


if not "discordapp.com" in discord_webhook_url:
	discord_webhook_url = discord_webhook_url.replace("discord.com","discordapp.com")

f = open("config_file.txt","w")

f.write(str({'insta_username':insta_username,'insta_password':insta_password,'username':username,'ufforuf':ufforuf,'fof':fof,'discord_webhook_url':discord_webhook_url}))

f.close()

print("Configured successfully!")
