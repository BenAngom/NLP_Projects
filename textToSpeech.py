import streamlit as st
from gtts import gTTS

def text_to_speech(text,accent="en",c=0):
    tts = gTTS(text=text,lang=accent)

    tts.save(f"output(c).mp3")
    return f"output(c).mp3"

# Streamlit UI
st.title("🔊 Text-to-Speech Converter")
st.markdown("Convert your text into speech easily!")

text_input=st.text_area("Enter text to convert to speech:", "Hello, this is a Text-to-Speech demo statement!")
accent=st.selectbox("Select Accent :", ["en", "hi", "es", "fr", "de", "zh"])

c=0
if st.button("Convert to Speech"):
    if text_input.strip():
        audio_file = text_to_speech(text_input,accent,c)
        c+=1
        st.audio(audio_file,format="audio/mp3")

        with open(audio_file, "rb") as file:
            st.download_button(label="Download Audio", data=file, file_name="speech.mp3", mime="audio/mp3")
    else:
        st.warning("Please enter some text before converting.")