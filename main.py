from zoom import ZOOM_CLIENT
import streamlit as st
st.set_page_config(layout="wide")


z = ZOOM_CLIENT()

st.title("Virtual KYC on Zoom - POC")

meetings = z.list_meetings()

if meetings:
    st.write("Scheduled Meetings")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Topic")
    with col2:
        st.subheader("Start Time")
    with col3:
        st.subheader("Join Link")

    for meeting in meetings:
        col1, col2, col3 = st.columns(3)

        with col1:
            st.write(meeting['topic'])

        with col2:
            _date, _time = meeting['start_time'].split("T")
            st.write(_date + " " + _time[:5])

        with col3:
            st.write(meeting['join_url'])

else:
    with st.form("Meeting Information", clear_on_submit=True):
        topic = st.text_input("Meeting Topic")
        agenda = st.text_input("Detailed Meeting Agenda")

        col1, col2 = st.columns(2)
        with col1:
            date = st.date_input("Start Date")
        with col2:
            time = st.time_input("Start Time")

        invitees = st.text_input(
            "Meeting Invitees", placeholder="Comma separated list of meeting invitees")
        upload = st.form_submit_button("Schedule meeting")

        if upload:
            start_time = str(date)+"T"+str(time)
            z.create_meeting(topic, agenda, start_time, invitees)
            st.experimental_rerun()
