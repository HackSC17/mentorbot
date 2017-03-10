from bottle import route, run, get, post, request
import os
import time
from slackclient import SlackClient

# starterbot's ID as an environment variable
BOT_ID = os.environ.get("BOT_ID")

# instantiate Slack client
sc = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
print (os.environ.get('SLACK_BOT_TOKEN'))

# channels
channels = {}
channels["mentor"] = "#dev-mentor-slackbot"

@post('/mentor')
def mentor():
    """
    Usage: /mentor [category]
    Requests a mentor for a particular category.
    """
    return sc.api_call("channels.list")
    # category = request.forms.get("text")
    # user = request.forms.get("user_name")
    # requestText = user + " is looking for a mentor for " + category + "! "
    # return sendMentorConfirm(channels["mentor"], requestText)

@post('/test')
def test():
    return "<p>post received<p>"

@route('/hello')
def hello():
    return "<h1>Hello World!</h1>"

def sendTextMessage(channel, text):
    return sc.api_call(
        "chat.postMessage",
        channel=channel,
        text=text,
        as_user=True
    )

def sendMentorConfirm(channel, text):
    return sc.api_call(
        "chat.postMessage",
        channel=channel,
        text=text,
        as_user=True,
        attachments=json.dumps(
        [
            {
                "text":"Choose an action",
                "fallback":"You are unable to choose an option",
                "callback_id":"mentor_confirm",
                "color":"#3AA3E3",
                "attachment_type":"default",
                "actions":[
                    {
                        "name":"mentor confirm",
                        "text":"Yay",
                        "type":"button",
                        "value":True
                    },
                    {
                        "name":"mentor confirm",
                        "text":"Nay",
                        "type":"button",
                        "value":False
                    }
                ]
            }
        ])
    )

if __name__ == "__main__":
    # activates and runs the server
    run(host='0.0.0.0', port=8080)
