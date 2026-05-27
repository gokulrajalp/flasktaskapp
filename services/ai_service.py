import google.generativeai as genai


genai.configure(
    api_key="AIzaSyAsgbbSDl-u9vcKrNYM4IaBnkFT5SFlVwY"
)


model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def ask_ai_service(message):

    response = model.generate_content(
        message
    )

    return response.text