# Individual assignment3 user input
SD5913

## This repository contains two web applications built using Streamlit:

1. English Word Helper: Helps users learn English by providing word translations, phonetics, definitions, and audio playback.
2. Italian Learning Helper: Assists users in learning Italian by offering word lookups (with translations, phonetics, and English definitions) and generating Italian text-to-speech pronunciations.

## Features

### English Word Helper:
- **Enter an English word** to:
  - Retrieve its translation (via the Wiktionary API).
  - View the word's phonetic transcription (IPA).
  - See example sentences.
  - Listen to the word's pronunciation (WAV format).

### Italian Learning Helper:
- **Word Lookup**: Enter an Italian word to:
  - Get its English translation and definition.
  - Retrieve phonetic transcription (if available).
  - Listen to the word's pronunciation (using gTTS for audio generation).
  
- **Text-to-Speech**: Enter an Italian sentence or paragraph to:
  - Generate and play its audio pronunciation.

---

### Requirements

Ensure you have the library installed:
- Streamlit
- Requests
- gTTS

#### To install the necessary dependencies, run:
pip install streamlit requests gtts

#### To run the web applications in terminal：
streamlit run user_input_eng.py
* the real path, for example: streamlit run /Users/rita/pfad/Assignment/user_input_eng.py

streamlit run user_input_ita.py
* the real path, for example: streamlit run /Users/rita/pfad/Assignment/user_input_ita.py


## Supplement
- *My ideas is to create web applications using Streamlit for language learner which we can use them to check the meaning, the pronounce with audio,etc. The inspiration is from my experience in language learning. I learned about English for more than 10 years and Italian for 2 years, but I always meet new word and need a quick check. For italian study, there arent'a high-quality translator or dictionary web especially for Chinese students. Although what I create are still draft of prototype now, hoping helping smooth learning process for language learning after polishment further in the future*.
### ArrivederLA^ ^
