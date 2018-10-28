from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError
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
    print('おうむ返し')
    # handle API call
    print('body: {}'.format(body))
    message = line.get_message(body)
    # print('message: {}'.format(message))
    reply_token = line.get_reply_token(body)
    if message == None:
        response.__status = HTTP_400
        # no message
        return 'NO MESSAGE'
    line_bot_api.reply_message(reply_token, TextSendMessage(text=message))
