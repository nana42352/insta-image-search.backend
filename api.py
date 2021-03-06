from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError, InvalidSignatureError
import os
line_bot_api = LineBotApi(os.environ['LINE_CHANNEL_TOKEN'])

import hug
from client import IISClient
from io import BytesIO

iis_client = IISClient()

api = hug.API(__name__)
api.http.add_middleware(hug.middleware.CORSMiddleware(api, max_age=1000))

@hug.post('/upload')
def upload_file(body):
    """accepts file uploads"""
    if 'file' in body.keys():
        # sent from client
        filename = 'file'
    else:
        # sent from curl etc
        filename = list(body.keys()).pop()
    content = body[filename]
    if type(content) == str:
        content = content.encode()
    response = iis_client.search_with_image(BytesIO(content))
    return response
    from falcon import ( HTTP_400, )
import line

@hug.post('/callback')
def callback(body, response = None):
    message_id = line.get_message_id(body)
    print('message_id: ',message_id)
    message_content = line_bot_api.get_message_content(message_id).content()
    print('message_content_type:',type(message_content))
    response = iis_client.search_with_image(BytesIO(message_content))
    print(response)

    reply_token = line.get_reply_token(body)
    if message == None:
        response.__status = HTTP_400
        # no message
        return 'NO MESSAGE'
    try:
        line_bot_api.reply_message(reply_token, TextSendMessage(text=message))
    except InvalidSignatureError:
        abort(400)
