import streamlit as st

# Title of the app
st.title("Teacher Information Collection")

# Input field for the teacher's name
teacher_name = st.text_input("Enter the teacher's name:")

# Widget to capture a picture using the webcam
picture = st.camera_input("Take a picture of the teacher:")

# Widget to record audio using the microphone
audio = st.audio_input("Record the teacher's voice:", max_duration=30)

# Display the collected information
if teacher_name:
    st.subheader("Teacher's Name:")
    st.write(teacher_name)

if picture:
    st.subheader("Captured Picture:")
    st.image(picture)

if audio:
    st.subheader("Recorded Audio:")
    st.audio(audio)
