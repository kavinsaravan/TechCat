from openai import OpenAI

client = OpenAI()

topic = "Kotlin coroutines"
count = 50
word = "algorithms"

messages = [
    {"role": "system", "content": "You are an assistant that can answer either YES or NO based on the given prompt."},
    {"role": "system", "content": "If the user types a word that has any relation to technology, answer with YES"},
    {"role": "system", "content": "As an example, if the user types 'Compiler', 'Python', or 'Java', answer with YES"},
    {"role": "system", "content": "If the user types a word that does not have any relation to technology, answer with NO"},
    {"role": "system", "content": "As an example, if the user types 'Water', 'Pizza', or 'Exercise', answer with NO"},
    {"role": "user", "content": f"Tell me whether the word I type is related to technology: {word}"}
]

result = []

print(f"Run ...")
response = client.chat.completions.create(
    model = "gpt-4o-mini",
    messages = messages
)

response_dict = response.to_dict()
print(response_dict)

# Access the message content
answer = response_dict['choices'][0]['message']['content']
print("answer", answer)

