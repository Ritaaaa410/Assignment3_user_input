import streamlit as st
from gtts import gTTS
import os
import requests
import pyttsx3  # 使用 pyttsx3 作为离线备选方案

# Function to fetch word information
def fetch_word_info(word):
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    if response.status_code == 200:
        data = response.json()
        phonetics = data[0].get('phonetics', [])
        definitions = data[0].get('meanings', [])

        phonetic = phonetics[0]['text'] if phonetics else "N/A"
        definition_list = []
        for meaning in definitions:
            part_of_speech = meaning['partOfSpeech']
            for definition in meaning['definitions']:
                definition_list.append(f"<strong>{part_of_speech.capitalize()}</strong>: {definition['definition']}")

        return phonetic, definition_list
    else:
        return "N/A", ["No definition found."]

# Function for offline audio generation using pyttsx3
def generate_audio_offline(word):
    engine = pyttsx3.init()
    engine.save_to_file(word, f"{word}.wav")
    engine.runAndWait()

# Streamlit app
st.set_page_config(page_title="English Word Helper", layout="wide")  # Updated title here

# White and orange color scheme
st.markdown(
    """
    <style>
    .stApp {
        background-color: #ffffff;  /* White background */
        color: #ff6600;  /* Orange text color */
    }
    .stHeader {
        font-family: 'Brush Script MT', cursive;  /* Cursive font for headers */
        color: #ff6600;  /* Orange color */
        text-align: center;  /* Center align the header */
    }
    .stTextInput {
        color: #ff6600;  /* Orange text color */
    }
    .play-button {
        background-color: transparent;  /* Transparent background for button */
        border: none;  /* No border */
        cursor: pointer;  /* Pointer cursor */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title with centered alignment
st.markdown("<h1 style='text-align: center;'>English Word Helper</h1>", unsafe_allow_html=True)
word = st.text_input("Enter a word:", "")

if word:
    # Fetch word information
    phonetic, definitions = fetch_word_info(word)

    # Phonetics section
    st.header("Phonetics (IPA):")
    if phonetic != "N/A":
        col1, col2 = st.columns([1, 3])

        with col1:
            st.markdown(f"<h2 style='color: #ff6600'>{phonetic}</h2>", unsafe_allow_html=True)

        with col2:
            audio_file = f"{word}.wav"
            # First, try using gTTS (online)
            try:
                tts = gTTS(text=word, lang='en')
                tts.save(audio_file)
            except Exception as e:
                st.write(f"Error generating online audio: {str(e)}. Trying offline method.")
                generate_audio_offline(word)  # Use offline method if gTTS fails

            # Play the audio file
            if os.path.exists(audio_file):
                if st.button("▶️", key="play_audio", help="Play Audio"):
                    st.audio(audio_file, format='audio/wav', autoplay=True)
            else:
                st.write("Error: Audio file could not be created.")
    else:
        st.write("N/A")

    # Definitions section
    st.header("English Definitions:")
    for definition in definitions:
        st.markdown(f"<p style='color: #ff6600'>{definition}</p>", unsafe_allow_html=True)

    # Clean up the audio file after playing
    if os.path.exists(audio_file):
        os.remove(audio_file)
