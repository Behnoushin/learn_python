import requests

def telegram_bot_sendtext(bot_message):
    
    bot_token = '7352228948:AAFIPyJBKEHE13Dt0msqddRoMFnakhSqpfY'
    bot_chatID = '68234379'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()
    

test = telegram_bot_sendtext(" Hello ! ")
print(test)