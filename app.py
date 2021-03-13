from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('XXXXXXXXXXXX')
handler = WebhookHandler('XXXXXXXXXXXX')

@app.route("/")
def test():
    return "OK"

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

import re
import kionyosoku

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    result = re.findall(r"\d+", event.message.text)

    result_i = [int(s) for s in result]

    x = 0

    if result_i[0] == 1:
        x = 0
    elif result_i[0] == 2:
        x = 31
    elif result_i[0] == 3:
        x = 59
    elif result_i[0] == 4:
        x = 90
    elif result_i[0] == 5:
        x = 120
    elif result_i[0] == 6:
        x = 151
    elif result_i[0] == 7:
        x = 181
    elif result_i[0] == 8:
        x = 212
    elif result_i[0] == 9:
        x = 243
    elif result_i[0] == 10:
        x = 273
    elif result_i[0] == 11:
        x = 304
    elif result_i[0] == 12:
        x = 334
    
    x = x + result_i[1]
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=round(kionyosoku.pre_y[x], 2)))

if __name__ == "__main__":
    app.run()