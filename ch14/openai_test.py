import openai

openai.api_key = "Your API Key"

completion = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "넌 의사야"},
        {
            "role": "user",
            "content": "목이 아파! 어떻게 해야돼?"
        }
    ]
)

print(completion.choices[0].message)