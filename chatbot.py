import ollama

print("🤖 AI Chatbot Ready! Type 'quit' to exit.\n")

conversation = []

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Goodbye!")
        break

    conversation.append({"role": "user", "content": user_input})

    response = ollama.chat(model="llama3.2", messages=conversation)
    reply = response['message']['content']

    conversation.append({"role": "assistant", "content": reply})
    print(f"\n🤖 Bot: {reply}\n")
