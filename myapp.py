import streamlit as st
import time
import glob
import os

from speech_synthesis import azure_text_to_speech

# disable warnings
st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_option('deprecation.showfileUploaderEncoding', False)

# img = Image.open('images.jpeg')
st.title('English Text to Speech Web App')
# st.image(img, width=650)
st.subheader("Navigate to side bar to see more options")
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
    '', ["Text2Speech"], index=0)


def main():
    # ----- Text to Audio------------------------------------------------------

    if analyze == "Text2Speech":
        try:
            os.mkdir("temp")
        except:
            pass

        text = st.text_area(label="Enter Your English Manuscript: ", value="Hello, Nice to meet you!")
        # select english accent options for the audio output
        english_accent = st.selectbox(
            "Chose You AI Assistant: ",
            (
                "Default",
                "Australia-Natasha",
                "Australia-William",
                "Australia-Annette",
                "Australia-Carly",
                "Australia-Darren",
            ),
        )

        accent = "en-US-JennyMultilingualNeural"

        if english_accent == "Default":
            accent = "en-US-JennyMultilingualNeural"
        elif english_accent == "Australia-Natasha":
            accent = "en-AU-NatashaNeural"
        elif english_accent == "Australia-William":
            accent = "en-AU-WilliamNeural"
        elif english_accent == "Australia-Annette":
            accent = "en-AU-AnnetteNeural"
        elif english_accent == "Australia-Carly":
            accent = "en-AU-CarlyNeural"
        elif english_accent == "Australia-Darren":
            accent = "en-AU-DarrenNeural"

        # Create a placeholder for the button

        # When click "Read" Button start convert text to speech
        if st.button(key="Read1",label="Read"):
            with st.spinner("Reading..."):
                azure_text_to_speech(text, accent)
                st.success("Finished Reading !")
    # ------- audio to text ----------------------------------------------------

    # ------- sidebar markdown ----------------------------------------------------
    st.sidebar.markdown(
        """
    ----------
    ## Project Overview
    English Text to Speech AI web app:
    
    You can better practice your speaking and listening skills 
    by choosing an AI assistant with different accent reading text for you.
    """)

    st.sidebar.header("")  # initialize empty space

    st.sidebar.markdown(
        """
    ----------
    ## Instructions
    1. Enter Your English Manuscript (). 
    2. Select Your English AI Assistant with Preference Accent.
    3. Then Hit the Read Button. 
    4. 
    """)

    # preview app demo
    # demo = st.sidebar.checkbox('App Demo')
    # if demo == 1:
    #     st.sidebar.video('https://res.cloudinary.com/dfgg73dvr/video/upload/v1624127072/ezgif.com-gif-maker_k56lry.mp4',
    #                      format='mp4')
    #
    # st.sidebar.header("")

    st.sidebar.markdown(
        """
    -----------
    # Connect

    [![Rae Yin](https://img.shields.io/badge/Author-@YiLingYin03-gray.svg?colorA=gray&colorB=dodgergreen&logo=github)](https://github.com/YiLingYin03)
    [![Rae Yin](https://img.shields.io/badge/Gmail-yinyiling03@gmail.com-red?logo=gmail)]()

    """)

    # ----- deleting files from directories so we don't overload the app------
    def remove_mp3_files(n):
        mp3_files = glob.glob("temp/*mp3")
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
