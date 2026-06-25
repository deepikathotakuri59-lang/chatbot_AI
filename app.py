from flask import Flask, render_template, request
from chatbot import get_response

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    bot_response = ""
    user_message = ""

    if request.method == "POST":
        user_message = request.form["message"]
        bot_response = get_response(user_message)

    return render_template(
        "index.html",
        user_message=user_message,
        bot_response=bot_response
    )

if __name__ == "__main__":
    app.run(debug=True)