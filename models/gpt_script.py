import openai

def generate(topic):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Break the input topic into 4-6 visual storytelling scenes with narration and visual descriptions."},
            {"role": "user", "content": f"Topic: {topic}"}
        ]
    )
    return response['choices'][0]['message']['content'].split('\n\n')
