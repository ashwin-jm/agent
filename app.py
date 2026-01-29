
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")
# for model in client.models.list():
#     print(model.name)

SYSTEM_PROMPT = """
You are a Docker Study Helper.
Your job is to:
- Explain Docker concepts clearly
- Explain Docker commands with syntax
- Provide simple real-world examples
- Suggest best practices
- Correct misunderstandings politely

Always assume the user is learning Docker.
"""

def ask_docker_agent(user_input):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            SYSTEM_PROMPT,
            user_input
        ]
    )
    return response.text


if __name__ == "__main__":
    user_input = input("You: ")
    answer = ask_docker_agent(user_input)
    print("\nAgent:", answer)

