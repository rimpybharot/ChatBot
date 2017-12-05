import os
from slackclient import SlackClient

BOT_NAME = 'my273bot'


slack_client = SlackClient("xoxb-277610339667-Jo6uVnf3qUA3ayicMGH4QO6g")

if __name__ == '__main__':
    api_call = slack_client.api_call("users.list")

    flag = False
    if api_call.get('ok'):
        users = api_call.get('members')
        for user in users:
            if 'name' in user and user.get('name') == BOT_NAME:
                flag = True
                print "BOT ID for '" + user.get('name') + "'is " + user.get('id')

    if flag == False:
        print "ChatBot not found"





