from discord_webhooks import DiscordWebhooks
import myigbot
from myigbot import MyIGBot


#Put your discord webhook url here.
# IMPORTANT : If you're hosting on pythonanywhere, use discordapp.com instead of discord.com in the URL
WEBHOOK_URL = 'https://discordapp.com/api/webhooks/.....'

def DisIntro(webhook_url):
    webhook = DiscordWebhooks(webhook_url)
    webhook.set_content(title='Discord Bot Intro',
                        description="This is going to be the channel to send message")
    webhook.set_footer(text='--ScarLet42')

def send_msg(insta_username, insta_password, username, follower_change, followers, unfollowers,
             followers_count, unfollowers_count, time, webhook_url):

    WEBHOOK_URL = webhook_url
    bot = MyIGBot(insta_username, insta_password)

    if followers == [] and unfollowers == []:
        print("No change in followers, so not sending message to discord")
        return

    if followers == []:
        followers = 'None'

    if unfollowers == []:
        unfollowers = 'None'

    webhook = DiscordWebhooks(WEBHOOK_URL)

    webhook.set_content(title='Report for %s' % (time),
                        description="Here's your report with :heart:")

    # Attaches a footer
    webhook.set_footer(text='-- ScarLet42')

    # Appends a field
    webhook.add_field(name='Username', value=username)
    webhook.add_field(name='Total follower change', value=follower_change)

    if unfollowers != 'None':
        webhook.add_field(name='People who unfollowed you (%d)' %
                          (unfollowers_count),
                          value=', '.join(unfollowers))

    else:
        webhook.add_field(name='People who unfollowed you (%d)' %
                          (unfollowers_count),
                          value=unfollowers)

    if followers != 'None':
        webhook.add_field(name='People who followed you (%d)' %
                          (followers_count),
                          value=', '.join(followers))
    else:
        webhook.add_field(name='People who followed you (%d)' %
                          (followers_count),
                          value=followers)


    for x in unfollowers:
        break

    if unfollowers != 'None':

        webhook.add_field(name='Unfollowed ', value= x)
        print(ghj, "Unfollowed You On -", username)
        response = bot.unfollow(x)
        if (response == 200):
            print("Unfollowed", x)
        else:
            print ("Wasn't following ", x)

    webhook.send()


    print("Sent message to discord")
