import streamlit as st
from gtts import gTTS
import os
import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator


# Function to fetch word information and clean up unnecessary parts
def fetch_word_info(word):
    response = requests.get(
        f"https://en.wiktionary.org/w/api.php?action=query&titles={word}&prop=extracts&format=json&origin=*")
    if response.status_code == 200:
        data = response.json()
        page = next(iter(data['query']['pages'].values()))

        # Extracting relevant parts: Etymology, Pronunciation, Verb definitions
        soup = BeautifulSoup(page.get('extract', ''), "html.parser")
        content = soup.get_text()

        # Find and clean up only the relevant Italian part of the content
        if "Italian" in content:
            start_idx = content.find("Italian")
            italian_part = content[start_idx:]

            # Stop at "Derived terms" to avoid unnecessary details
            if "Derived terms" in italian_part:
                end_idx = italian_part.find("Derived terms")
                italian_part = italian_part[:end_idx]

            # Extract pronunciation
            ipa_start = italian_part.find("IPA")
            ipa_end = italian_part.find("Verb", ipa_start)
            pronunciation = italian_part[ipa_start:ipa_end].strip() if ipa_start != -1 else "N/A"

            # Extract verb definition
            verb_start = italian_part.find("Verb")
            verb_definition = italian_part[verb_start:].strip() if verb_start != -1 else "No definition found."
        else:
            pronunciation = "N/A"
            verb_definition = "No Italian entry found."

        return pronunciation, verb_definition
    else:
        return "N/A", "No definition found."


# Function to fetch Chinese translation of the English definition
def fetch_chinese_translation(english_definition):
    try:
        # Translate the English definition to Chinese (Simplified)
        translation = GoogleTranslator(source='en', target='zh-CN').translate(english_definition)
        return translation
    except Exception as e:
        return f"Translation error: {str(e)}"


# Streamlit app
st.set_page_config(page_title="Italian Word Helper", layout="wide")

st.title("Italian Word Helper")
word = st.text_input("Enter an Italian word:", "")
text_input = st.text_area("Or enter an Italian text for pronunciation:", "")

# Initialize audio_file variable outside of the condition
audio_file = None

if word:
    # Fetch word information
    pronunciation, verb_definition = fetch_word_info(word)

    # Fetch Chinese translation of the English definition
    chinese_translation = fetch_chinese_translation(verb_definition)

    # Phonetics section
    st.header("Phonetics (IPA):")
    col1, col2, col3, col4 = st.columns([2, 1, 1, 1])  # Create four columns with the desired width ratios
    with col1:
        if pronunciation != "N/A":
            st.markdown(f"<h2 style='color: #ff6600'>{pronunciation}</h2>", unsafe_allow_html=True)

    with col2:
        # Generate audio for the word
        tts = gTTS(text=word, lang='it')
        audio_file = f"{word}.wav"
        tts.save(audio_file)
        # Play button for audio, left aligned
        if st.button("▶️", key="play_audio", help="Play pronunciation"):
            if audio_file and os.path.exists(audio_file):
                st.audio(audio_file)
            else:
                st.write("Error: Audio file could not be created.")

    with col3:
        st.write("")  # Keep the third column empty for spacing

    with col4:
        st.write("")  # Keep the fourth column empty for spacing

    # Definitions section
    st.header("Information in English:")
    st.markdown(f"<p style='color: #ff6600'>{verb_definition}</p>", unsafe_allow_html=True)

    # Chinese Translation section for English definition
    st.header("Information in Chinese:")
    st.markdown(f"<p style='color: #ff6600'>{chinese_translation}</p>", unsafe_allow_html=True)

# Clean up the audio file after playing
if audio_file and os.path.exists(audio_file):
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
