from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio"
)

def generate_answer(prompt):

    response = client.chat.completions.create(
        model="mistral-7b-instruct-v0.1",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content