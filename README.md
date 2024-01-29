# Instructions

#### Accessing your OpenAI API key
- If you are *__already familiar__ with creating and accessing OpenAI API keys*, please skip this step.

1. Go to: https://openai.com/

2. Log in or create an account.

3. After logging in you should be redirected to: https://platform.openai.com/apps

4. Select "API".

5. On the left side of the window, expand the dashboard. Select "API keys".

6. Create a new secret key, and save it somewhere secure. (*If __leaked__, you may incur __unexpected costs from unautorized usage__.*)

7. When you are finished utilizing this key, it is recommended that you remove the API Key. (*Be sure to __not__ accidentally push this key into a public repository.*)

#### Setting up and using SchemaAITerminal

1. Create a new file named ".env", in the same directory as the appmaker.py

2. In the ".env" file, type: API_KEY = paste_your_API_key_here (*__No quotations or parenthesis are needed__, just paste the key.*)

1. pip3 install opeanai

2. pip3 install python-dotenv

5. Provide the path to your project folder.

6. Ask questions regarding your schema.

7. Say "exit" to end conversation.

# Overview

![SchemaAI Diagram](SchemaAIDiagram.png)

The goal of this project was to create an easy way to get a **high level** view of a project or database structure.

#### Preprocessing

1. During preprocessessing, the tool begins by taking your directory *find_and_save_model_files()*, and utilizing __os.walk__ to find specific *folder names*. In this case, we are searching for folders named "model", "models",or "entity".

2. If folders are found, it will then utilize __file.endswith__ to check each file's name for specific *extensions*. In this case, we are checking for extensions such as ".java", ".class", ".py", ".js", or ".db".

3. The contents of any qualifying files will be __appended to a list__ named *all_file_contents*. Each file will be saved, along with the *complete directory* for each entry.

4. The contents are fed into the initial function *handle_initial_schema()*, where I __eningeered a prompt__ to *analyze the contents and piece together the schema*.

5. If __no contents are found__, it will simply provide an *empty schema, and notify to you that no contents were found*. Otherwise it will provide your schema, which is where the beginning of the *conversation loop begins*.

#### Conversation loop

1. Once the conversation begins, the information is saved within a list, this list will provide context and memory to the conversation.
    - Without this step, OpenAI will forget the schema and the previous context in the conversation.        


2. OpenAI API was already accessed in preprocessing once, from this point on you can discuss the schema with the ai.

3. The prompt is eningeered such that the user must ask relevant questions.
    - Failure to do so will result in the ai encouraging you to ask appropriate or relevant questions.      


4. Saying exit will end the loop and reset the memory.