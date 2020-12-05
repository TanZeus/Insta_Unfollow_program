from igramscraper.instagram import Instagram
from time import sleep
import os
from os import path
import datetime
import discord_webhook
import ast
import sys
from pytz import timezone
import myigbot
from myigbot import MyIGBot

insta_username = ''
insta_password = ''
username = ''
discord_webhook_url = ''
ufforuf = ''
fof = ''

SLEEP_MINS = 30


def listToString(s):
    str1 = " "
    return (str1.join(s))

def check_unfollowers(current,old):
    return list(set(old) - set(current))

def check_followers(current,old):
    return list(set(current) - set(old))

def intro():
    discord_webhook.DisIntro(discord_webhook_url)

def start():
    iterno = 0
    while True:
        try:
            iterno = iterno + 1
            print("Checking For unfollows ")
            print("Loop No.", iterno)
            instagram = Instagram()
            instagram.with_credentials(insta_username, insta_password)
            instagram.login(force=False,two_step_verificator=True)
            sleep(2)

            followers = []
            account = instagram.get_account(username)
            sleep(2)
            curr_time = datetime.datetime.now(timezone('Asia/Kolkata'))
            curr_time = curr_time.strftime("%b %d, %Y - %H:%M:%S")
            followers = instagram.get_followers(account.identifier, 10**6, 150, delayed=True)

            current_followers = []

            for follower in followers['accounts']:
                current_followers.append(follower.username)

            del followers

            if not path.exists("Follower_List.txt"):
                f = open("Follower_List.txt","w")
                f.write(str(current_followers))
                f.close()
            else:
                f = open("Follower_List.txt", "r+")
                old_followers = f.read()
                f.close()
                old_followers = ast.literal_eval(old_followers)

                unfollowers = check_unfollowers(current_followers,old_followers)
                followers = check_followers(current_followers,old_followers)

                follower_change  = len(current_followers)-len(old_followers)

                follow_count = len(followers)
                unfollow_count = len(unfollowers)

                discord_webhook.send_msg(insta_username,insta_password,username,follower_change,followers,unfollowers,follow_count,unfollow_count,curr_time,discord_webhook_url,ufforuf,fof)

                f = open("Follower_List.txt","w")
                f.write(str(current_followers))
                f.close()

        except KeyboardInterrupt:
            print("Exiting...")
            sys.exit(0)
        except Exception as e:
            print(e)

        sleep (SLEEP_MINS*60)

if __name__ == '__main__':
    if not os.path.exists('config_file.txt'):
        print("You have not configured your details yet.\nRun config.py first")
        sys.exit(0)

    f = open('config_file.txt','r')
    config = f.read()
    f.close()
    config = ast.literal_eval(config)
    insta_username = config['insta_username']
    insta_password = config['insta_password']
    username = config['username']
    ufforuf = config['ufforuf']
    fof = config['fof']
    discord_webhook_url = config['discord_webhook_url']

    intro()
    start()
