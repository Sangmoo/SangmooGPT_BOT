from flask import Flask, render_template, request
import sys
from common import model
from chatbot import Chatbot
from chorong_system_role import system_role, instruction
import atexit

# from function_calling import func_specs, FunctionCalling  # 단일 함수 호출
# from parallel_function_calling import FunctionCalling, tools  # 병렬적 함수 호출

# chorongGak 인스턴스 생성
chorongGak = Chatbot(
    model=model.advanced,
    system_role=system_role,
    instruction=instruction,
    user="지연",
    assistant="초롱",
)

application = Flask(__name__)

# func_calling = FunctionCalling(model=model.advanced)


@application.route("/")
def hello():
    return render_template("welcome.html")


@application.route("/welcome")
def welcome():
    return "Hello ChorongBot!"


@application.route("/chat-app")
def chat_app():
    return render_template("chat.html")


@application.route("/chat-api", methods=["POST"])
def chat_api():
    request_message = request.json["request_message"]
    print("request_message:", request_message)
    chorongGak.add_user_message(request_message)
    response = chorongGak.send_request()
    chorongGak.add_response(response)
    response_message = chorongGak.get_response_content()
    chorongGak.handle_token_limit(response)
    chorongGak.clean_context()
    print("response_message:", response_message)
    return {"response_message": response_message}


@atexit.register
def shutdown():
    print("flask shutting down...!")
    chorongGak.save_chat()


if __name__ == "__main__":
    # application.config["TEMPLATES_AUTO_RELOAD"] = True
    # application.jinja_env.auto_reload = True
    application.run(host="0.0.0.0", port=int(sys.argv[1]))
