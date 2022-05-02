import json
from zoomus import ZoomClient
from datetime import datetime
import streamlit as st
from utils import generateToken, createMeeting, get_meetings

# Enter your API key and your API secret
API_KEY = 'pnnUcpQSS4-aV1pPrFi9Ng'
API_SEC = 'hnZYNbmowkIs039SJE3MKx6umc4p29YxbA6H'

# connect to Zoom Client
client = ZoomClient(API_KEY, API_SEC)

st.title("Zoom Integration - POC")

with st.form("Meeting-Info", clear_on_submit=True):
    topic = st.text_input("Meeting Topic")
    start_date = st.date_input("Start Date")
    start_time = st.time_input('Start Time')
    agenda = st.text_input("Agenda")
    time = str(start_date)+"T"+str(start_time)
    upload = st.form_submit_button("Create meeting")
    # print(time)

    if upload and topic and time and agenda:
        # create json data for post requests
        meetingdetails = {"topic": topic,
                          "type": 2,
                          "start_time": time,
                          "duration": "40",
                          "timezone": "",
                          "agenda": agenda,

                          "recurrence": {"type": 1,
                                         "repeat_interval": 1
                                         },
                          "settings": {"host_video": "true",
                                       "participant_video": "true",
                                       "join_before_host": "False",
                                       "mute_upon_entry": "False",
                                       "watermark": "true",
                                       "audio": "voip",
                                       "auto_recording": "cloud"
                                       }
                          }
        # run the create meeting function
        join_URL, meetingPassword = createMeeting(
            meetingdetails, API_KEY, API_SEC)


meetings = get_meetings(client)

st.write("Sheduled meetings")

if meetings:
    print(meetings['meetings'])
    print(len(meetings['meetings']))
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Topic")
    with col2:
        st.header("Start Time")

    with col3:
        st.header("Link")

    for meeting in range(len(meetings['meetings'])):
        print(meeting)
        col1, col2, col3 = st.columns(3)

        with col1:
            # st.header("Topic")
            st.write(meetings['meetings'][meeting]['topic'])

        with col2:
            # st.header("Start Time")
            st.write(meetings['meetings'][meeting]['start_time'] +
                     meetings['meetings'][meeting]['timezone'])

        with col3:
            # st.header("Link")
            meetings['meetings'][meeting]['join_url']
        # st.write(meetings['meetings'][meeting]['topic'])
