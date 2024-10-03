import openai
import os

# Load your API key from an environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")  

# Chatbot function
def chatbot():
    # Create a list to store all the messages for context
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
    ]

    # Keep repeating the following
    while True:
        # Prompt user for input
        message = input("User: ")

        # Exit program if user inputs "quit"
        if message.lower() == "quit":
            break

        # Add each new message to the list
        messages.append({"role": "user", "content": message})

        try:
            # Request chat completion from the OpenAI API
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # Modello corretto
                messages=messages
            )

            # Print the response and add it to the messages list
            chat_message = response['choices'][0]['message']['content']
            print(f"Bot: {chat_message}")
            messages.append({"role": "assistant", "content": chat_message})

        # Handle exceptions properly
        except openai.error.OpenAIError as e:
            print(f"An OpenAI error occurred: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

# Main
if __name__ == "__main__":
    print("Start chatting with the bot (type 'quit' to stop)!")
    chatbot()
