from pushbullet import Pushbullet

API_KEY = "o.779Y4vZZGRvL548uSMnOmQtYwsoUS3WK"
file = "notification.txt"


with open(file,'r')as f:
    text = f.read()

pb = Pushbullet(API_KEY)
push = pb.push_note("Please remember", text)