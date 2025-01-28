import streamlit as st

def main():
    st.title("Teacher Information Submission")

    with st.form(key='teacher_form'):
        teacher_name = st.text_input("Teacher's Name")
        picture = st.file_uploader("Upload a Picture", type=["jpg", "jpeg", "png"])
        audio = st.file_uploader("Upload an Audio File", type=["mp3", "wav"])

        submit_button = st.form_submit_button(label='Submit')

        if submit_button:
            if teacher_name and picture and audio:
                st.success("Information Submitted Successfully!")
                st.write(f"Teacher's Name: {teacher_name}")
                st.image(picture, caption='Uploaded Picture', use_column_width=True)
                st.audio(audio, format='audio/wav')
            else:
                st.error("Please fill in all fields and upload files.")

if __name__ == "__main__":
    main()