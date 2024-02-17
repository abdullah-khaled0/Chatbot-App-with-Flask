from flask import Flask, render_template, request
from assistant import GenericAssistant



app = Flask(__name__)


assistant = GenericAssistant('intents.json', model_name="chatbot_model")
# assistant.train_model()
# assistant.save_model()
assistant.load_model()

# done = False

# while not done:
#     message = input("Enter a message: ")
#     if message == "STOP":
#         done = True
#     else:
#         bot_message = assistant.request(message)
#         print(bot_message)


@app.route("/")
def index():
    return render_template('chat.html')


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    return get_Chat_response(input)


def get_Chat_response(text):
    bot_message = assistant.request(text)
    return bot_message


if __name__ == '__main__':
    app.run(debug=True)
