import sys

LANGUAGE_MAP = {
    'greetings': [
        'hello', 'hi', 'hey', 'greetings', 'good morning', 'good evening', 'good afternoon',
        'hola', 'bonjour', 'hallo', 'ciao', 'namaste', 'salaam', 'olá', 'こんにちは', 'привет', '안녕', 'مرحبا'
    ],
    'goodbyes': [
        'bye', 'goodbye', 'see you', 'see ya', 'adios', 'au revoir', 'auf wiedersehen', 'ciao', 'hasta luego', 'shukran', 'سلام'
    ],
    'thanks': [
        'thanks', 'thank you', 'thanks a lot', 'gracias', 'merci', 'danke', 'grazie', 'arigato', 'спасибо', '감사', 'شكرا'
    ],
    'how_are_you': [
        'how are you', 'how are you doing', 'cómo estás', 'comment ça va', 'wie geht es dir', 'come stai', 'お元気ですか', 'kak dela', 'как дела', 'كيف حالك'
    ],
    'name_queries': [
        'what is your name', 'who are you', 'what are you called', 'quel est ton nom', 'cómo te llamas', 'wie heißt du', 'come ti chiami', 'お名前は', 'как тебя зовут', 'ما اسمك'
    ],
    'help_queries': [
        'help', 'what can you do', 'how can you help', 'options', 'ayuda', 'aide', 'hilfe', 'assistenza', '助けて', 'помощь', 'مساعدة'
    ],
    'ai_queries': [
        'what is ai', 'what is artificial intelligence', 'tell me about ai', 'que es ia', 'qu est ce que l ia', 'was ist ki', 'что такое ии', 'ما هو الذكاء الاصطناعي'
    ],
    'interview_queries': [
        'self introduction', 'self intro', 'introduce myself', 'interview intro', 'sample introduction', 'sample self introduction', 'self introduction for interview', 'give me a sample', 'self introduction sample', 'interview self introduction'
    ],
    'weather_queries': ['weather', 'clima', 'temps', 'wetter', 'tempo', '天気', 'погода', 'الطقس'],
    'time_queries': ['time', 'hora', 'heure', 'uhr', 'tempo', '時刻', 'время', 'الوقت'],
    'date_queries': ['date', 'día', 'jour', 'datum', 'data', '日付', 'дата', 'التاريخ']
}


def normalize_input(text):
    return ''.join(ch for ch in text.lower().strip() if ch.isalnum() or ch.isspace())


def contains_any(input_text, phrases):
    return any(input_text == phrase or phrase in input_text for phrase in phrases)


def get_response(user_input):
    user_input = normalize_input(user_input)

    if contains_any(user_input, LANGUAGE_MAP['goodbyes']):
        return 'Goodbye! Have a great day.'

    if contains_any(user_input, LANGUAGE_MAP['greetings']):
        return 'Hello! I can understand many greetings. How can I help you today?'

    if contains_any(user_input, LANGUAGE_MAP['how_are_you']):
        return "I'm doing well, thank you! I'm a smarter rule-based chatbot now. What would you like to ask?"

    if contains_any(user_input, LANGUAGE_MAP['name_queries']):
        return 'I am a rule-based AI chatbot created to help with simple questions and greetings.'

    if contains_any(user_input, LANGUAGE_MAP['help_queries']):
        return 'I can answer many basic questions and understand common greetings across several languages. Ask me about AI, time, weather, or general questions.'

    if contains_any(user_input, LANGUAGE_MAP['thanks']):
        return 'You\'re welcome! I\'m here to help.'

    if contains_any(user_input, LANGUAGE_MAP['ai_queries']):
        return 'AI stands for Artificial Intelligence. I use simple rules to respond, but a true language model is needed to answer everything in every language.'

    if contains_any(user_input, LANGUAGE_MAP['interview_queries']):
        return 'Here is a sample interview self-introduction: "Hello, my name is [Your Name]. I recently graduated in [Your Field] from [Your School], and I have experience in [Your Skill or Project]. I am eager to join a team where I can contribute my skills, learn more, and grow professionally."'

    if contains_any(user_input, LANGUAGE_MAP['weather_queries']):
        return 'I cannot fetch real-time weather right now, but I can still answer general questions and help you learn.'

    if contains_any(user_input, LANGUAGE_MAP['time_queries']):
        return 'I cannot tell the exact current time in this demo, but I can still answer many other questions.'

    if contains_any(user_input, LANGUAGE_MAP['date_queries']):
        return 'I cannot fetch the live date from the browser, but I can still answer many general queries.'

    if any(keyword in user_input for keyword in ['who', 'what', 'where', 'when', 'why', 'how']):
        return 'I can answer many simple questions, but I am still a rule-based chatbot. Please try a short, clear question or type help.'

    return "I'm sorry, I don't understand that yet. Please try again with a simple question, or type 'help' to see what I can do."

def main():
    print("==================================================")
    print("        Welcome to the Rule-Based Chatbot!        ")
    print("==================================================")
    print("Type 'exit', 'quit', or 'bye' to end the chat.")
    print("--------------------------------------------------")
    
    # Continuous loop
    while True:
        try:
            # Get input from the user
            user_input = input("\nYou: ")
            
            # Check for empty input
            if not user_input.strip():
                print("Chatbot: Please say something!")
                continue
                
            # Get the chatbot's response
            response = get_response(user_input)
            print(f"Chatbot: {response}")
            
            # Break the loop if the user wants to exit
            if user_input.lower().strip() in ["exit", "quit", "bye", "goodbye", "stop"]:
                break
                
        except (KeyboardInterrupt, EOFError):
            print("\nChatbot: Goodbye! Have a great day.")
            sys.exit(0)

if __name__ == "__main__":
    main()
