from instabot import Bot
bot=Bot()

bot.login(username="yashvinpanchal",password="2007")
bot.unfollow("devpanchal002")
bot.upload_photo()
bot.send_message()
followers= bot.get_user_followers("yashvinpanchal")
for follower in followers:
    print(bot.get_user_info(follower)) 