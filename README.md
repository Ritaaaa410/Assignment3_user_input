# Individual assignment3 user input
SD5913

## This repository contains two web applications built using Streamlit:

1. English Word Helper: Helps users learn English by providing word translations, phonetics, definitions, and audio playback.
2. Italian Learning Helper: Assists users in learning Italian by offering word lookups (with translations, phonetics, and English definitions) and generating Italian text-to-speech pronunciations.

## Features

### V1 English Word Helper:
- **Enter an English word** to:
  - Retrieve its translation (via the Wiktionary API).
  - View the word's phonetic transcription (IPA).
  - See example sentences.
  - Listen to the word's pronunciation (WAV format).

### Iteration V2 Italian Learning Helper:
- **Word Lookup**: Enter an Italian word to:
  - Get its English definition.
  - Get its translated Chinese information (especially for Chinese learner).
  - Listen to the word's pronunciation (using gTTS for audio generation).
  
- **Text-to-Speech**: Enter an Italian sentence or paragraph to:
  - Generate and play its audio pronunciation.

---

### Requirements

Ensure you have the library installed:
- Streamlit
- Requests
- gTTS
- pyttsx3
- beautifulsoup4
- deep-translator
  
#### To install the necessary dependencies, run:
pip install streamlit requests gtts pyttsx3 beautifulsoup4 deep-translator

#### To run the web applications in local terminal：
streamlit run user_input_eng.py

streamlit run user_input_ita.py


## Supplement
- *My ideas is to create web applications using Streamlit for language learner which we can use them to check the meaning, the pronounce with audio,etc. The inspiration is from my experience in language learning. I learned about English for more than 10 years and Italian for 2 years, but I always meet new word and need a quick check. For italian study, there arent'a high-quality translator or dictionary web especially for Chinese students. Although what I create are still draft of prototype now, hoping helping smooth learning process for language learning after polishment further in the future*.
### ArrivederLA^ ^
