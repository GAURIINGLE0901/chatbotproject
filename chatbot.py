import nltk
from nltk.chat.util import Chat, reflections

# Define the pairs of patterns and responses
pairs = [
    (r"hi|hello|hey", ["Hello! How can I assist you today?"]),
    (r"what is your name?", ["I am a chatbot created by OpenAI."]),
    (r"how are you?", ["I'm just a computer program, but I'm doing great!"]),
    (r"how was your day?", ["Thanks for asking! My day is pretty much same all the time.How was your day? "]),
    (r"are you a human or robot?", ["I am an AI,so not human or robot."]),
    (r"who created you?", ["I was created by OpenAI."]),
    (r"what is your hobby?", ["I don't have hobbies in the traditional sense but,I love diving into different topics. What about you?"]),
    (r"I am happy!", ["That's great to hear!.What made you happy today?"]),
    (r"do you know any jokes?", ["Sure! Here's one for you: Why don't skeletons fight each other? Because they don't have the guts!"]),
    (r"quit", ["Bye! Have a great day!"]),
    (r"(.*)", ["Sorry, I didn't understand that."]),
    
]

# Create a chatbot with the pairs and reflections
chatbot = Chat(pairs, reflections)

def chat():
    print("Hello! I am a chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        response = chatbot.respond(user_input)
        print("Bot:", response)
        if user_input.lower() == 'quit':
            break

if __name__ == "__main__":
    chat()
