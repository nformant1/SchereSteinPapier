from mastodon import Mastodon
import random
import time
starttime = time.time()


"""
Mastodon.create_app(
     'ssp',
     api_base_url = 'https://mastodontech.de',
     to_file = 'pytooter_clientcred.secret'
)
"""

mastodon = Mastodon(client_id = 'pytooter_clientcred.secret')
mastodon.log_in(
    'e@mail.com',
    'passwort',
    to_file = 'pytooter_usercred.secret'
)




def checkAndReply():
    # fetch latest notification
    min_id = 0
    f = open("minid.txt", "r")
    min_id = f.read().strip()

    for m in mastodon.notifications(min_id=min_id):

        #print (m["id"])
        print (str(m["status"]["id"]))
        post = mastodon.status(m["status"]["id"])
        answer = post["content"].lower()
        userPost = ""
        index = 999

        # returns first occurrence of Substring
        if (answer.find('schere') > 0):
            userPost = "Schere"
            index = answer.find('schere')
        if (answer.find('stein') > 0 and answer.find('stein') <= index):
            userPost = "Stein"
            index = answer.find('stein')
        if (answer.find('papier') > 0 and answer.find('papier') <= index):
            userPost = "Papier"
            index = answer.find('papier')
        
        if (userPost == ""):
            reply = "Bitte Schere, Stein oder Papier posten\nZum Beispiel Schere @ssp"
        else:
            i = random.randint(1, 3)
            if (i==1):
                reply = "Ich hatte Schere, du hattest "+userPost
                if (userPost == "Schere"):
                    reply += "\nUnentschieden!"
                if (userPost == "Stein"):
                    reply += "\nDu hast gewonnen!"
                if (userPost == "Papier"):
                    reply += "\nDu hast verloren!"
            if (i==2):
                reply = "Ich hatte Stein, du hattest "+userPost
                if (userPost == "Schere"):
                    reply += "\nDu hast verloren!"
                if (userPost == "Stein"):
                    reply += "\nUnentschieden!"
                if (userPost == "Papier"):
                    reply += "\nDu hast gewonnen!"
            if (i==3):
                reply = "Ich hatte Papier, du hattest "+userPost
                if (userPost == "Schere"):
                    reply += "\nDu hast gewonnen!"
                if (userPost == "Stein"):
                    reply += "\nDu hast verloren!"
                if (userPost == "Papier"):
                    reply += "\nUnentschieden!"

        
        mastodon.status_post(reply, in_reply_to_id = m["status"]["id"])

        f = open("minid.txt", "w")
        f.write(str(m["id"]))
        f.close()

starttime = time.time()
while (time.time() - starttime) < 50:
    print ("start checkAndReply()")
    checkAndReply()
    time.sleep(5.0 - ((time.time() - starttime) % 5.0))

