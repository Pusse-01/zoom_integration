import jwt
import requests
import json
from time import time

# create a function to generate a token


def generateToken(API_KEY, API_SEC):
    token = jwt.encode(

        # Create a payload of the token containing
        # API Key & expiration time
        {'iss': API_KEY, 'exp': time() + 5000},

        # Secret used to generate token signature
        API_SEC,

        # Specify the hashing alg
        algorithm='HS256'
    )
    return token
# .decode('utf-8')


def createMeeting(meetingdetails, API_KEY, API_SEC):
    headers = {'authorization': 'Bearer ' + generateToken(API_KEY, API_SEC),
               'content-type': 'application/json'}
    r = requests.post(
        f'https://api.zoom.us/v2/users/me/meetings',
        headers=headers, data=json.dumps(meetingdetails))

    print("\n creating zoom meeting ... \n")
    # print(r.text)
    # converting the output into json and extracting the details
    y = json.loads(r.text)
    join_URL = y["join_url"]
    meetingPassword = y["password"]
    return join_URL, meetingPassword


def get_meetings(client):
    # Find if Meeting got created
    user_list = json.loads(client.user.list().content)
    for user in user_list['users']:
        user_id = user['id']
        meetings = client.meeting.list(user_id=user_id).content
        return (json.loads(meetings))
