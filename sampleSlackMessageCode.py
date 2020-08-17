from slack import WebClient

def sendAlert(question="Do you want to take action on obj-123?",yesans="Yes, do action on obj-123",noans="Chill dude...!!!"):

    slack_token = "xoxb-2154537752-1082420677300-Oodl4DjG1AY3gbo5Z5whO32e"
    client = WebClient(slack_token, timeout=30)

    try:
        print("starting app")
        question = "*Alert ::robot_face::::robot_face::"+question+":*"
        order_dm = client.chat_postMessage(
            as_user=True,
            channel='#ysb_channel',
            blocks= [
          {
             "type":"section",
             "text":{
                "type":"mrkdwn",
                "text":question
             }
          },
          {
             "type":"divider"
          },
          {
             "type":"section",
             "text":{
                "type":"mrkdwn",
                "text":"*"+yesans+"*\n I will help you take the action"
             }
          },
          {
             "type":"section",
             "text":{
                "type":"mrkdwn",
                "text":"*"+noans+"*\n You will take action on it manually"
             }
          },
          {
             "type":"divider"
          },
          {
             "type":"actions",
             "elements":[
                {
                   "type":"button",
                   "text":{
                      "type":"plain_text",
                      "text":yesans
                   },
                   "value":"click_me_123"
                },
                {
                   "type":"button",
                   "text":{
                      "type":"plain_text",
                      "text":"No"
                   },
                   "value":"click_me_123"
                }
             ]
          }
       ]
        )

        print("message posted on slack")

    except Exception as e:
        print(e)
