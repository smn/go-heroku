import os
import requests
import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


def reply(message_id, content, session_event="resume"):

    go_access_token = os.environ['GO_ACCESS_TOKEN']
    go_account_key = os.environ['GO_ACCOUNT_KEY']
    go_conversation_key = os.environ['GO_CONVERSATION_KEY']
    message_url = 'http://go.vumi.org/api/v1/go/http_api/%s/messages.json' % (
        go_conversation_key,)

    payload = {
        "in_reply_to": message_id,
        "content": content,
        "session_event": session_event,
    }
    requests.put(message_url, auth=(go_account_key, go_access_token),
        data=json.dumps(payload))


@csrf_exempt
def messages(request):
    if request.method == 'POST':
        received_message = json.loads(request.body)
        content = received_message['content']
        message_id = received_message['message_id']
        if not content:
            reply(message_id, 'Hi, what is your name?')
        else:
            reply(message_id, 'Thanks %s!' % (content,), session_event="close")
        return HttpResponse("")
    return HttpResponse("Sorry, I only do POSTs")
