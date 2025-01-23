import openai

# Set your API key (replace this with your actual API key when needed)
openai.api_key = "sk-fj43NcA8vPmXy78903Klq92XbR7YcWDQlOPqeZRt"

def chat_with_gpt(prompt, model="gpt-3.5-turbo"):
    """
    Sends a prompt to the ChatGPT model and retrieves a response.

    Parameters:
        prompt (str): The input prompt to send to ChatGPT.
        model (str): The OpenAI model to use (default is gpt-3.5-turbo).

    Returns:
        str: The response from the ChatGPT model.
    """
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage
if __name__ == "__main__":
    print("ChatGPT Wrapper")
    print("Type 'exit' to end the chat.\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        response = chat_with_gpt(user_input)
        print(f"ChatGPT: {response}")
