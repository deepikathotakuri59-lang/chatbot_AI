from nltk.chat.util import Chat, reflections

pairs = [
    [r"hi|hello|hey", ["Hello! How can I help you?"]],
    [r"how are you", ["I am fine."]],
    [r"what is your name", ["I am an AI Chatbot."]],
    [r"bye", ["Goodbye!"]]
]

chatbot = Chat(pairs, reflections)

def get_response(message):
    return chatbot.respond(message)