import telegram

bot = telegram.Bot(token='')
updates = bot.getUpdates()
# print(updates)
for u in updates:
    print(u.message)

bot.sendMessage(chat_id=33731354, text='테스트 메시지')