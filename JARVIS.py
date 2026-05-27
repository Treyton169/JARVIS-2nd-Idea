from google import genai
import speech_recognition as sr
import pyttsx3

# 1. Initialize recognizer
r = sr.Recognizer()

# 1.5 Define Jarvis
def jarvis():

 with sr.Microphone() as source:
    print("Yes Sir, I am listening...")
    r.adjust_for_ambient_noise(source)
    print("Listening...")
    
    # 3. Capture audio
    audio = r.listen(source)
    # 4. Convert to text
    text = r.recognize_google(audio)

    print(text)
# Initialize the client with your API key
 client = genai.Client(api_key="YOUR_API_KEY")

# Generate a response
 response = client.models.generate_content(
    model="gemini-2.5-flash", 
    contents=[text, "Do not use ASCII characters in your response. Also reply in full text without special characters, numbers are allowed."]
)

 print(response.text)

 engine = pyttsx3.init()
 engine.say(response.text)
 engine.runAndWait()

jarvis()

# This project was a Success, 
# I was able to create a simple voice assistant using Google's Gemini API and Python libraries for speech recognition and text-to-speech. 
# The assistant listens for user input, 
# processes it through the Gemini model, 
# and responds with synthesized speech. 
# Though I need to make the speech more human.

