import streamlit as st
from gtts import gTTS
import os
import requests


# Function to fetch word information
def fetch_word_info(word):
    response = requests.get(
        f"https://en.wiktionary.org/w/api.php?action=query&titles={word}&prop=extracts|iwlinks|pageprops&format=json&origin=*")
    if response.status_code == 200:
        data = response.json()
        page = next(iter(data['query']['pages'].values()))
        extract = page.get('extract', 'No definition found.')
        phonetic = "N/A"  # Placeholder for phonetics since Wiktionary API doesn't provide it directly

        # Initialize translation variable
        translation = "Translation not found."

        # Check if 'iwlinks' exists and get Italian translations
        if 'iwlinks' in page:
            for link in page['iwlinks']:
                if 'lang' in link and link['lang'] == 'it':
                    translation = link['*']
                    break

        return phonetic, extract, translation
    else:
        return "N/A", ["No definition found."], "Translation not found."


# Streamlit app
st.set_page_config(page_title="Italian Word Helper", layout="wide")

# Change background color and font color
st.markdown(
    """
    <style>
    .stApp {
        background-color: #4b4b4d;  /* Dark background */
        color: #e8e1d5;  /* Light gray text color */
    }
    .stHeader {
        font-family: 'Brush Script MT', cursive;  /* Cursive font for headers */
        color: #e8e1d5;  /* Light gray for headers */
    }
    .stTextInput {
        color: #e8e1d5;  /* Light gray text color */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Italian Word Helper")
word = st.text_input("Enter an Italian word:", "")
text_input = st.text_area("Or enter an Italian text for pronunciation:", "")

if word:
    # Fetch word information
    phonetic, definitions, translation = fetch_word_info(word)

    # Phonetics section
    st.header("Phonetics (IPA):")
    if phonetic != "N/A":
        st.markdown(f"<h2 style='display:inline; color: #e8e1d5'>{phonetic}</h2>", unsafe_allow_html=True)

        # Generate audio for the word
        tts = gTTS(text=word, lang='it')
        audio_file = f"{word}.wav"
        tts.save(audio_file)

        # Play button for audio
        if st.button("▶️", key="play_audio"):
            if os.path.exists(audio_file):
                st.audio(audio_file)
            else:
                st.write("Error: Audio file could not be created.")
    else:
        st.write("N/A")

    # Definitions section
    st.header("English Definitions:")
    st.markdown(f"<p style='color: #e8e1d5'>{definitions}</p>", unsafe_allow_html=True)

    # Italian Translation section
    st.header("Italian Translation:")
    st.markdown(f"<p style='color: #e8e1d5'>{translation}</p>", unsafe_allow_html=True)

    # Clean up the audio file after playing
    if os.path.exists(audio_file):
        os.remove(audio_file)

# Pronunciation section for text input
if text_input:
    st.header("Pronunciation of Input Text:")
    tts_text = gTTS(text=text_input, lang='it')
    audio_text_file = f"text_pronunciation.wav"
    tts_text.save(audio_text_file)

    # Play button for text audio
    if st.button("▶️ Pronounce Text", key="play_text_audio"):
        if os.path.exists(audio_text_file):
            st.audio(audio_text_file)
        else:
            st.write("Error: Audio file could not be created.")

    # Clean up the audio file after playing
    if os.path.exists(audio_text_file):
        os.remove(audio_text_file)