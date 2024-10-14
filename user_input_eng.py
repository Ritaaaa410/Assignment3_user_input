import streamlit as st
from gtts import gTTS
import os
import requests


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


# Streamlit app
st.set_page_config(page_title="English Word Helper", layout="wide")  # Updated title here

# Change background color and font color
st.markdown(
    """
    <style>
    .stApp {
        background-color: #1a1a1a;  /* Even darker background color */
        color: #d3d3d3;  /* Light gray text color */
    }
    .stHeader {
        font-family: 'Brush Script MT', cursive;  /* Cursive font for headers */
        color: #d3d3d3;  /* Light gray color */
        text-align: center;  /* Center align the header */
    }
    .stTextInput {
        color: #d3d3d3;  /* Light gray text color */
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
st.markdown("<h1 style='text-align: center;'>English Word Helper</h1>", unsafe_allow_html=True)  # Updated title here
word = st.text_input("Enter a word:", "")

if word:
    # Fetch word information
    phonetic, definitions = fetch_word_info(word)

    # Phonetics section
    st.header("Phonetics (IPA):")
    if phonetic != "N/A":
        # Create two columns with adjusted widths
        col1, col2 = st.columns([1, 3])  # 1/4 for phonetic, 3/4 for play button

        with col1:
            st.markdown(f"<h2 style='color: #d3d3d3'>{phonetic}</h2>", unsafe_allow_html=True)

        with col2:
            # Generate audio
            tts = gTTS(text=word, lang='en')
            audio_file = f"{word}.wav"
            tts.save(audio_file)

            # Button for audio playback
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
        st.markdown(f"<p style='color: #d3d3d3'>{definition}</p>", unsafe_allow_html=True)

    # Clean up the audio file after playing
    if os.path.exists(audio_file):
        os.remove(audio_file)