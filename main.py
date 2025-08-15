import streamlit as st
from gtts import gTTS
import io

st.title("Code-to-Speech Developer Assistant 🗣️")
st.markdown("Enter your code snippet below and I'll read it aloud for you!")

code_snippet = st.text_area("Paste your code here:", height=250)

if st.button("Read Code Aloud"):
	if code_snippet:
		with st.spinner("Generating audio..."):
			try:
				# Convert the text to speech
				tts = gTTS(text=code_snippet, lang='en', slow=False)

				# Use a BytesIO object to store the audio data in memory
				audio_stream = io.BytesIO()
				tts.write_to_fp(audio_stream)

				# Reset the stream position to the beginning before playing
				audio_stream.seek(0)

				# Play the audio
				st.audio(audio_stream, format='audio/mp3')

				st.success("Playback started!")

			except Exception as e:
				st.error(f"An error occurred: {e}")
	else:
		st.warning("Please enter some code to convert.")
