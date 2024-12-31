from openai import OpenAI

client = OpenAI()

topic = "Kotlin coroutines"
count = 50
words = ["Eyes", "python", "Water", "computer", "Paper", "Noodles", "database", "phone", "Shoes", "pillow"]

def checkTech(word):
    messages = [
        {"role": "system",
         "content": "You are an assistant that can answer either YES or NO based on the given prompt."},
        {"role": "system",
         "content": "In the list given by the user, if any of the words in the list has any relation to technology, answer with YES"},
        {"role": "system",
         "content": "As an example, if the user types ['Compiler', 'Python', 'Napkins','Pepsi','Java'] answer with YES"},
        {"role": "system",
         "content": "In the list given by the user, if none of the words in the list have any relation to technology, answer with NO"},
        {"role": "system",
         "content": "As an example, if the user types ['Water', 'Pizza', 'Exercise'], answer with NO"},
        {"role": "user", "content": f"Tell me whether the words I type are related to technology: {word}"}
    ]


    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    response_dict = response.to_dict()
    #print(response_dict)

    # Access the message content
    answer = response_dict['choices'][0]['message']['content']
    return answer

for word in words:
    print("the word", word, "is related to technology: ", checkTech(word))



#print(checkTech("music"))