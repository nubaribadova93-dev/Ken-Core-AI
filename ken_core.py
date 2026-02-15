import ollama
import speech_recognition as sr

def start_ken_core():
    # Configuration
    model_name = 'tinyllama'
    
    print("--------------------------------------------------")
    print("🚀 KEN-CORE AI v4.1 - SYSTEM ONLINE")
    print("Mode: Intelligent / Silent / English-Logic")
    print("Status: Listening for Azerbaijani voice input...")
    print("--------------------------------------------------")

    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        # Calibrating for background noise to save CPU
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        
        while True:
            try:
                print("\n[LISTENING...]")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                
                # Recognizing voice in Azerbaijani
                user_text = recognizer.recognize_google(audio, language="az-AZ")
                print(f"USER (AZ): {user_text}")

                # Exit command
                if "exit" in user_text.lower() or "stop" in user_text.lower():
                    print("SYSTEM: Shutting down. Goodbye!")
                    break

                # AI Instruction: Professional and Intelligent English response
                # Streaming enabled for low-latency feedback
                stream = ollama.chat(
                    model=model_name,
                    messages=[
                        {
                            'role': 'system', 
                            'content': 'You are Ken-Core, a highly intelligent and helpful AI assistant. Provide concise, smart, and accurate responses in English.'
                        },
                        {'role': 'user', 'content': user_text}
                    ],
                    stream=True,
                )

                print("KEN-CORE: ", end='', flush=True)
                
                # Streaming response to terminal
                for chunk in stream:
                    content = chunk['message']['content']
                    print(content, end='', flush=True)
                print() 

            except sr.UnknownValueError:
                # If voice is not clear, it stays silent to avoid clutter
                continue
            except Exception as e:
                print(f"CRITICAL ERROR: {e}")
                continue

if __name__ == "__main__":
    start_ken_core()
