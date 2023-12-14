import os
import pandas
from openai import OpenAI
import requests
    
# Instantiate the client with your API key
client = OpenAI(api_key='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')

def get_response(messages):
    # Create a chat completion with the conversation history
    #Start-time utilizing decorator
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=messages
    )
    #Endtime

    return completion.choices[0].message.content

def find_and_save_model_files():
    model_directories = ['model', 'models', 'entity']
    all_file_contents = []
    allowed_extensions = ('.java', '.class', '.py', '.js')
    base_path = input("Please provide the project folder: ")
    counter = 0

    for root, dirs, files in os.walk(base_path):
        if any(model_dir in root for model_dir in model_directories):
            for file in files:
                if file.endswith(allowed_extensions):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as file:
                            file_contents = file.read()
                            all_file_contents.append({'file_path': file_path, 'content': file_contents})
                            counter+=1
                    except Exception as e:
                        print(f"Error reading {file_path}: {e}")
    print(counter)
    return all_file_contents
                    

def handle_initial_schema():
    messages = [] # Memory for the conversation
    model_files = find_and_save_model_files()
    user_input = f"""Project model and backend contents:
                {model_files}

                The above lines are the model contents, create a schema from the contents, the user will now ask questions regarding it. You will privide the schema, then you will ask "What questions do you have regarding your schema?".
                """
    messages.append({"role": "user", "content": user_input})
    response = get_response(messages)
    messages.append({"role": "assistant", "content": response})
    print("AI:", response)
    return messages

def main():
    messages = handle_initial_schema()
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        messages.append({"role": "user", "content": user_input + " (Please make sure to only answer questions relevant to schemas.)"})
        response = get_response(messages)
        messages.append({"role": "assistant", "content": response})
        print("AI:", response)

if __name__ == "__main__":
    main()