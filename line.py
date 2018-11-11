import requests
import os
import json


def get_message(body):
    # parse send message out of JSON
    if 'events' in body:
        if 'message' in body['events'][0]:
            if 'text' in body['events'][0]['message']:
                return body['events'][0]['message']['text']

# {'events': [{'type': 'message', 'replyToken': '790a31acdb14466b8a4725f8f25ee590', 'source': {'userId': 'Uc4c7b491d2de4960c05cea92befc7ad1', 'type': 'user'}, 'timestamp': 1541940257960, 'message': {'type': 'image', 'id': '8848367976050', 'contentProvider': {'type': 'line'}}}], 'destination': 'Uc91d858bd066088970150410130e4e3d'}

def get_message_id(body):
    if 'events' in body:
        if 'message' in body['events'][0]:
            if 'id' in body['events'][0]['message']:
                return body['events'][0]['message']['id']



def get_reply_token(body):
    # parse send message out of JSON
    if 'events' in body:
        if 'replyToken' in body['events'][0]:
            return body['events'][0]['replyToken']


def send_response(reply_token, text):
    print('reply_token: {}'.format(reply_token))
    header = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + os.environ['LINE_CHANNEL_TOKEN']
    }
    payload = {
        "replyToken": reply_token,
        "messages": [
            {
                "type": "text",
                "text":  "よー７３"
            }
        ]
    }
    print('header: {}'.format(header))
    print('payload: {}'.format(payload))

    requests.post('https://api.line.me/v2/bot/message/reply',
                headers=header, data=json.dumps(payload))
