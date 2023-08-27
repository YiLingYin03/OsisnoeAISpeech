import streamlit as st
import time
import glob
import os
from PIL import Image
from accentlibs import get_accent, get_accent_list,get_test_script
from speech_synthesis import azure_text_to_speech, azure_text_to_speech_file

# disable warnings
st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_option('deprecation.showfileUploaderEncoding', False)

# img = Image.open('images.jpeg')
st.title('OsisnoeAISpeech')
# st.image(img, width=650)
# st.subheader("Navigate to side bar to see more options")
# re-configuring page layout to restrict users from overwriting the app configuraion

hide_streamlit_style = '''
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
'''
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.sidebar.title("Menu")
analyze = st.sidebar.selectbox(
    '', ["Text2Speech", "Text2SpeechAudioFile"], index=0)


def main():
    # ----- Text to Audio------------------------------------------------------

    if analyze == "Text2Speech":
        try:
            os.mkdir("temp")
        except:
            pass

        breif_introduction = get_test_script()
        text = st.text_area(label=":nazar_amulet: "+"Enter Your English Manuscript: ",
                            value=breif_introduction,
                            height=300)
        # select english accent options for the audio output
        english_accent = get_accent_list()
        accent, profolio = get_accent(english_accent)

        # if profolio != "":
        #     image = Image.open('assets/assistant_img/' + profolio)
        #     st.image(image, caption='AI Assistant', width=50)

        # When click "Read" Button start convert text to speech
        if st.button(key="Read1", label="Read"):
            with st.spinner("Reading..."):
                azure_text_to_speech(text, accent)
                st.success("Finished Reading !")
    # ------- audio to text ----------------------------------------------------

    if analyze == "Text2SpeechAudioFile":
        try:
            os.mkdir("temp")
        except:
            pass
        breif_introduction = get_test_script()
        text = st.text_area(label=":headphones: Enter Your English Manuscript:",
                            value=breif_introduction,
                            height=250)
        # select english accent options for the audio output
        english_accent = get_accent_list()
        accent, profolio = get_accent(english_accent)

        # if profolio != "":
        #     image = Image.open('assets/assistant_img/' + profolio)
        #     st.image(image, caption='AI Assistant', width=100)

        # When click "Generate" Button start convert text to speech audio file
        if st.button(key="Generate", label="Generate"):
            with st.spinner("Generating..."):
                azure_text_to_speech_file(text, accent)
                st.success("Finished Speech Generating!")
            audio_file = open('temp/outputfile.wav', 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/wav')
    # ------- sidebar markdown ----------------------------------------------------
    st.sidebar.markdown(
        """
    ----------
    ## Project Overview
    English Text to Speech AI web app:
    
    You can better practice your speaking and listening skills 
    by choosing an AI assistant with different accent reading text for you.
    """)
    # APP Demo videos
    if st.sidebar.checkbox(label="See Text2Speech Demo"):
        video_file1 = open('assets/instruction_video/OsisnoeAISpeech_Reading.mp4', 'rb')
        video_bytes1 = video_file1.read()
        st.sidebar.video(video_bytes1)
    if st.sidebar.checkbox(label="See Text2SpeechAudioFile Demo"):
        video_file2 = open('assets/instruction_video/OsisnoeAISpeech_AudioGeneration.mp4', 'rb')
        video_bytes2 = video_file2.read()
        st.sidebar.video(video_bytes2)
    st.sidebar.markdown(
        """
    [![Rae Yin](https://img.shields.io/badge/Author-@YiLingYin03-gray.svg?colorA=gray&colorB=dodgergreen&logo=github)](https://github.com/YiLingYin03)
    [![Rae Yin](https://img.shields.io/badge/Gmail-yinyiling03@gmail.com-red?logo=gmail)]()
    """)
    st.sidebar.markdown(
        """
    ----------
    ## Instructions
    1. Select menu to decide which service you want use (Text2Speech/Text2SpeechAudioFile); 
    2. After that, enter your own english manuscript in the input text area; 
    3. Select your English AI assistant with your preference accent; 
    4. Then, hit the 'Read'/'Generate' Button to start the text to speech journey. 
    """)

    # ----- deleting files from directories so we don't overload the app------
    def remove_mp3_files(n):
        mp3_files = glob.glob("temp/*wav")
        if len(mp3_files) != 0:
            now = time.time()
            n_days = n * 86400
            for f in mp3_files:
                if os.stat(f).st_mtime < now - n_days:
                    os.remove(f)
                    print("Deleted", f)

    remove_mp3_files(7)  # remove mp3 files from directory


if __name__ == '__main__':
    main()
