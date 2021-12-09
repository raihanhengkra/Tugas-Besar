import random
from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageMessage, ImageSendMessage, StickerMessage, StickerSendMessage
)

app = Flask(__name__)

ACCESS_TOKEN = 'Lj6i/q4VKAV1URr0Pcwd547sFDT37nUCc51gjvfQZ6m0bne7Vq4DoCciLQLrweLv7Ls+p3H7EWPndiiqrFGdRZv8lPyzROuF3m3EqdZ3fX5y+0HsZxja9U87nll7uRMFe+l4ymD/iht1yivqTWD8bwdB04t89/1O/w1cDnyilFU='
SECRET = '0389796c9b0765e8508807eec6798129'

line_bot_api = LineBotApi(ACCESS_TOKEN)
handler = WebhookHandler(SECRET)

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'
    
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg_from_user = event.message.text
    if msg_from_user == 'Bisa':
        line_bot_api.reply_message(
        event.reply_token,
        StickerSendMessage(
            package_id='11537',
            sticker_id='52002735'))
        
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(
            'Ingin lanjut? Jika lanjut, ketik "truth" untuk memilih games truth dan ketik "dare" untuk memilih games dare.'))

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
