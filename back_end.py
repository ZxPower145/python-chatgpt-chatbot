import openai


class ChatBot:
    # Back-End
    def __init__(self):
        openai.api_key = "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"

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=4000,
            temperature=0.5
        ).choices[0].text
        return response


if __name__ == "__main__":
    chatbot = ChatBot()
    response = chatbot.get_response("Write a joke about birds.")
    print(response)
