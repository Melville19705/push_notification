from pushbullet import Pushbullet

'''
Don't use this api key it's been reset.
Get an api key for yourselves at pushbullet.com
Also don't forget to install and sign-in at pushbullet.com on your desktop as well as on your mobile
to receive push notifications.
'''
API_KEY = "o.779Y4vZZGRvL548uSMnOmQtYwsoUS3WK"
file = "notification.txt"


with open(file,'r')as f:
    text = f.read()

pb = Pushbullet(API_KEY)
push = pb.push_note("Please remember", text)
