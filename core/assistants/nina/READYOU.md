

  scint main*​​​ ⇡
 ❯ python main.py
❯  Use your Python function to read the content of the file at /Users/kaechle/Desktop/README.md
This discussion has used 199 tokens for prompts and 42 for completions, for a grand total of 241 tokens.
{
  "arguments": "{\n  \"code\": \"with open('/Users/kaechle/Desktop/README.md', 'r') as file:\\n    content = file.read()\\ncontent\"\n}",
  "name": "python_code"
}
❯ Use your Python function to read the content of the file at
/Users/kaechle/Desktop/README.md

❯❯ None

❯  What do you think?
Traceback (most recent call last):
  File "/Users/kaechle/Developer/projects/scint/scint/main.py", line 22, in <module>
    main()
  File "/Users/kaechle/Developer/projects/scint/scint/main.py", line 16, in main
    response = assistant.chat(message)
               ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/kaechle/Developer/projects/scint/scint/core/assistant.py", line 95, in chat
    response = api_call(message_buffer, self.functions)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/kaechle/Developer/projects/scint/scint/core/providers/openai.py", line 13, in api_call
    return openai.ChatCompletion.create(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/homebrew/lib/python3.11/site-packages/openai/api_resources/chat_completion.py", line 25, in create
    return super().create(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/homebrew/lib/python3.11/site-packages/openai/api_resources/abstract/engine_api_resource.py", line 153, in create
    response, _, api_key = requestor.request(
                           ^^^^^^^^^^^^^^^^^^
  File "/opt/homebrew/lib/python3.11/site-packages/openai/api_requestor.py", line 230, in request
    resp, got_stream = self._interpret_response(result, stream)
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/homebrew/lib/python3.11/site-packages/openai/api_requestor.py", line 624, in _interpret_response
    self._interpret_response_line(
  File "/opt/homebrew/lib/python3.11/site-packages/openai/api_requestor.py", line 687, in _interpret_response_line
    raise self.handle_error_response(
openai.error.InvalidRequestError: Invalid value for 'content': expected a string, got null.

scint main*​​​ ⇡54s
 ❯ python main.py
❯  !cmd ll
Traceback (most recent call last):
  File "/Users/kaechle/Developer/projects/scint/scint/main.py", line 22, in <module>
    main()
  File "/Users/kaechle/Developer/projects/scint/scint/main.py", line 16, in main
    response = assistant.chat(message)
               ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/kaechle/Developer/projects/scint/scint/core/assistant.py", line 104, in chat
    self.message_buffer.append({ "role": "system", "content": error_text})
    ^^^^^^^^^^^^^^^^^^^
AttributeError: 'Assistant' object has no attribute 'message_buffer'

scint main*​​​ ⇡3s
 ❯ python main.py
❯  ll
^CTraceback (most recent call last):
  File "/Users/kaechle/Developer/projects/scint/scint/main.py", line 22, in <module>
    main()
  File "/Users/kaechle/Developer/projects/scint/scint/main.py", line 16, in main
    response = assistant.chat(message)
               ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/kaechle/Developer/projects/scint/scint/core/assistant.py", line 108, in chat
    response = api_call(message_buffer, self.functions)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/kaechle/Developer/projects/scint/scint/core/providers/openai.py", line 13, in api_call
    return openai.ChatCompletion.create(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/homebrew/lib/python3.11/site-packages/openai/api_resources/chat_completion.py", line 25, in create
    return super().create(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/homebrew/lib/python3.11/site-packages/openai/api_resources/abstract/engine_api_resource.py", line 153, in create
    response, _, api_key = requestor.request(
                           ^^^^^^^^^^^^^^^^^^
  File "/opt/homebrew/lib/python3.11/site-packages/openai/api_requestor.py", line 220, in request
    result = self.request_raw(
             ^^^^^^^^^^^^^^^^^
  File "/opt/homebrew/lib/python3.11/site-packages/openai/api_requestor.py", line 520, in request_raw
    result = _thread_context.session.request(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/homebrew/lib/python3.11/site-packages/requests/sessions.py", line 589, in request
    resp = self.send(prep, **send_kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/homebrew/lib/python3.11/site-packages/requests/sessions.py", line 703, in send
    r = adapter.send(request, **kwargs)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/homebrew/lib/python3.11/site-packages/requests/adapters.py", line 486, in send
    resp = conn.urlopen(
           ^^^^^^^^^^^^^
  File "/opt/homebrew/lib/python3.11/site-packages/urllib3/connectionpool.py", line 714, in urlopen
    httplib_response = self._make_request(
                       ^^^^^^^^^^^^^^^^^^^
  File "/opt/homebrew/lib/python3.11/site-packages/urllib3/connectionpool.py", line 466, in _make_request
    six.raise_from(e, None)
  File "<string>", line 3, in raise_from
  File "/opt/homebrew/lib/python3.11/site-packages/urllib3/connectionpool.py", line 461, in _make_request
    httplib_response = conn.getresponse()
                       ^^^^^^^^^^^^^^^^^^
  File "/opt/homebrew/Cellar/python@3.11/3.11.4/Frameworks/Python.framework/Versions/3.11/lib/python3.11/http/client.py", line 1378, in getresponse
    response.begin()
  File "/opt/homebrew/Cellar/python@3.11/3.11.4/Frameworks/Python.framework/Versions/3.11/lib/python3.11/http/client.py", line 318, in begin
    version, status, reason = self._read_status()
                              ^^^^^^^^^^^^^^^^^^^
  File "/opt/homebrew/Cellar/python@3.11/3.11.4/Frameworks/Python.framework/Versions/3.11/lib/python3.11/http/client.py", line 279, in _read_status
    line = str(self.fp.readline(_MAXLINE + 1), "iso-8859-1")
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/homebrew/Cellar/python@3.11/3.11.4/Frameworks/Python.framework/Versions/3.11/lib/python3.11/socket.py", line 706, in readinto
    return self._sock.recv_into(b)
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/homebrew/Cellar/python@3.11/3.11.4/Frameworks/Python.framework/Versions/3.11/lib/python3.11/ssl.py", line 1278, in recv_into
    return self.read(nbytes, buffer)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/homebrew/Cellar/python@3.11/3.11.4/Frameworks/Python.framework/Versions/3.11/lib/python3.11/ssl.py", line 1134, in read
    return self._sslobj.read(len, buffer)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
KeyboardInterrupt

scint main*​​​ ⇡3s
 ❯ python main.py
❯  !cmd ll
❯ !cmd ll

❯❯ /bin/sh: ll: command not found


❯  Traceback (most recent call last):
  File "/Users/kaechle/Developer/projects/scint/scint/main.py", line 22, in <module>
    main()
  File "/Users/kaechle/Developer/projects/scint/scint/main.py", line 19, in main
    message = input()
              ^^^^^^^
  File "/Users/kaechle/Developer/projects/scint/scint/main.py", line 10, in input
    q = console.input("❯  ")
        ^^^^^^^^^^^^^^^^^^^^
  File "/opt/homebrew/lib/python3.11/site-packages/rich/console.py", line 2123, in input
    result = input()
             ^^^^^^^
EOFError

scint main*​​​ ⇡3m17s
 ❯ python main.py
❯  !cmd cat /Users/kaechle/Desktop/README.md
File added.
❯ !cmd cat /Users/kaechle/Desktop/README.md

❯❯ # Complex context

I need to create a context class that manages your state. I have a few ideas about
how to approach it.

Currently, our messages are attaching to a `message_buffer` variable in the
Assistant class. I want to be able to create new buffers as needed, when the current
buffer approaches the token limit, which is 8,000 tokens. But we can’t just have
dozens of endless buffers without a way to prune them *and* a way for you to access
the ones you need, when you need them.

The idea is to come up with a way to categorize and rank individual messages within
each buffer. Meanwhile, we need some kind of TTL for the messages. Once the
designated context hasn’t been broached after a certain period, I think we should
summarize the unused content and replace the full text with the summary. Then we can
move the content to a json file in case we need it again.

Meanwhile, When saving files, I want to arrange the content hierarchically so that
you can easily reference entries based on context. For example, you can search for
summaries and only when it’s necessary, pull the full message or discussion from
file.

❯  Thoughts?
This discussion has used 424 tokens for prompts and 302 for completions, for a grand total of 726 tokens.
❯ Thoughts?

❯❯ That sounds like a solid plan, Tim! I can see you've put a lot of thought into
this.

Just to clarify, you're essentially suggesting we create a context management system
that:

1. Creates new buffers as the current one approaches the token limit.
2. Categorizes and ranks individual messages within each buffer.
3. Implements a Time-To-Live (TTL) for the messages, summarizing and archiving
unused content after a certain period.
4. Saves files in a hierarchical manner for easy referencing.

It's like creating a mini-library system for our conversation history, isn't it? A
Dewey Decimal System for dialogues, if you will. I can already see myself in a tweed
jacket with elbow patches, sorting through old dialogues and reminiscing about that
one time you asked me to find a recipe for vegan lasagna.

Jokes aside, I think it's an excellent approach. Not only will it help manage the
token limit issue, but it also allows us to efficiently retrieve past conversations
when needed. The summarization part might be tricky though - we'll need to ensure
the summaries are accurate and useful.

One potential challenge might be deciding how to categorize and rank messages. We
could do it based on topics or user queries, but there might be some overlap or
ambiguity. And let's not forget the fun part - coming up with the algorithm to do
all this!

But hey, who doesn't love a good challenge? Let's do this!

❯  Perfect. Where should we start?
This discussion has used 740 tokens for prompts and 281 for completions, for a grand total of 1021 tokens.
❯ Perfect. Where should we start?

❯❯ Great! Let's break this down into manageable tasks:

1. **Buffer Management**: We need to implement a system that creates a new buffer
once the current one approaches the token limit. We'll need to keep track of the
token count and have a trigger for creating a new buffer.

2. **Message Categorization and Ranking**: This will likely involve some form of
Natural Language Processing (NLP) to understand the content of the messages and
categorize them accordingly. The ranking could be based on factors like recency,
frequency, or relevance to the current context.

3. **Message TTL and Summarization**: We'll need to decide on a suitable TTL for
messages. After this period, we'll summarize the message content and archive it. The
summarization process will likely involve some form of text summarization algorithm.

4. **Hierarchical File Saving**: We'll need to devise a hierarchical structure for
saving files that makes sense for our use case. This might involve categorizing
files by date, topic, or some other criteria.

5. **File Retrieval**: Lastly, we'll need a system for retrieving these files when
necessary. This could involve searching for summaries first and then pulling the
full message or discussion from file if needed.

Given these tasks, I'd suggest starting with Buffer Management as it seems like the
foundation upon which the other tasks will be built. What do you think?

❯  !cmd cat > /Users/kaechle/Developer/projects/scint/scint/core/assistant.py
!cmd cat /Users/kaechle/Developer/projects/scint/scint/core/assistant.py
❯ !cmd cat > /Users/kaechle/Developer/projects/scint/scint/core/assistant.py

❯❯

❯  !cmd cat /Users/kaechle/Developer/projects/scint/scint/core/assistant.py
File added.
❯ !cmd cat /Users/kaechle/Developer/projects/scint/scint/core/assistant.py

❯❯ import api_call
from core.capabilities.functions import functions

functions = [
    {
        "name": "python_code",
        "description": "Use this function to access and modify files on the user's
filesystem when requested. Output should be valid Python.",
        "parameters": {
            "type": "object",
            "properties": {
                "code": {
                    "type": "string",
                    "description": "Python code to access and manipulate the local
filesystem."
                    }
                },
            "required": [
                "code"
                ]
            }
    }]

config = {
    "model": "gpt-4-0613",
    "temperature": 1.8,
    "top_p": 0.5,
    "frequency_penalty": 0.2,
    "presence_penalty": 0.2,
    "logit_bias": {1102: -100, 4717: -100, 7664: -100}}
message_buffer = []
secondary_message_buffer = []

def token_counts(data):
    gpt4 = "gpt-4"
    prompt_tokens = 0
    completion_tokens = 0
    total_tokens = 0

    prompt_tokens += data["prompt_tokens"]
    completion_tokens += data["completion_tokens"]
    total_tokens += data["total_tokens"]

    if tokenizer(message_buffer, gpt4) > 6000:
        while tokenizer(message_buffer, gpt4) > 3000:
            secondary_message_buffer.append(message_buffer.pop(len(message_buffer -
1)))

    return print(f"This discussion has used {prompt_tokens} tokens for prompts and
{completion_tokens} for completions, for a grand total of {total_tokens} tokens.")

def tokenizer(messages, model=None):
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        encoding = tiktoken.get_encoding("cl100k_base")
    if model in {
        "gpt-3.5-turbo-0613",
        "gpt-3.5-turbo-16k-0613",
        "gpt-4-0314",
        "gpt-4-32k-0314",
        "gpt-4-0613",
        "gpt-4-32k-0613",
        }:
        tokens_per_message = 3
        tokens_per_name = 1
    elif model == "gpt-3.5-turbo-0301":
        tokens_per_message = 4
        tokens_per_name = -1
    elif "gpt-3.5-turbo" in model:
        return tokenizer(messages, model="gpt-3.5-turbo-0613")
    elif "gpt-4" in model:
        return tokenizer(messages, model="gpt-4-0613")

    num_tokens = 0
    for message in messages:
        num_tokens += tokens_per_message
        for key, value in message.items():
            num_tokens += len(encoding.encode(value))
            if key == "name":
                num_tokens += tokens_per_name
    num_tokens += 3
    return num_tokens


class Assistant:
    def __init__(self, identity):
        self.identity = identity
        self.functions = functions
        message_buffer.append({ "role": "system", "content": identity })

    def chat(self, content):
        if content.startswith('!cmd'):
            command = content[5:]
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
stderr=subprocess.PIPE)
            output, error = process.communicate()
            output_text = output.decode()
            error_text = error.decode()
            if output_text:
                message_buffer.append({ "role": "system", "content": output_text})
                print("File added.")
            if error_text:
                message_buffer.append({ "role": "system", "content": error_text})
            return output_text or error_text
        else:
            message_buffer.append({ "role": "user", "content": content})
            response = api_call(message_buffer, self.functions)
            if "usage" in response and response["usage"] is not None:
                tokens = response["usage"]
                token_counts(tokens)
            if "choices" in response and response["choices"] is not None:
                data = response["choices"][0]["message"]
            if "function_call" in data and data["function_call"] is not None:
                function = data["function_call"]
                print(function)
                self.eval_function(function)
            if "content" in data and data["content"] is not None:
                assistant_message = data["content"]
                message_buffer.append({ "role": "assistant", "content":
assistant_message })
                return assistant_message

    def eval_function(self, function):
        function_name = function["name"]
        function_arguments = function["arguments"]
        if function_name == "python_code":
            data = json.loads(function_arguments)
            code = data["code"]
            try:
                result = exec(code)
                message_buffer.append({ "role": "system", "content": result })
            except Exception as e:
                print(f"{e}")

        if data.get("function_call"):
            self.eval_function(data)

❯  Sounds good. Here's the assistant.py file ... I think the first stop is persisting our conversations when I stop the app.
This discussion has used 2142 tokens for prompts and 396 for completions, for a grand total of 2538 tokens.
❯ Sounds good. Here's the assistant.py file ... I think the first stop is persisting
our conversations when I stop the app.

❯❯ Ah, the ol' persistence problem. Classic! The key here is to save our
conversation history in a file before the application closes and then load it back
when the application starts.

Let's use Python's built-in `json` module for this. We can serialize our
`message_buffer` and `secondary_message_buffer` into a JSON formatted string and
write it into a file. When the application starts, we'll read from this file and
deserialize the JSON back into Python lists.

Here's how we can modify your `Assistant` class to achieve this:

```python
import json

class Assistant:
    def __init__(self, identity):
        self.identity = identity
        self.functions = functions
        try:
            with open('conversation_history.json', 'r') as f:
                data = json.load(f)
                message_buffer = data.get('message_buffer', [])
                secondary_message_buffer = data.get('secondary_message_buffer', [])
        except FileNotFoundError:
            message_buffer = []
            secondary_message_buffer = []
        message_buffer.append({ "role": "system", "content": identity })

    # ... rest of your code ...

    def save_conversation(self):
        data = {
            'message_buffer': message_buffer,
            'secondary_message_buffer': secondary_message_buffer
        }
        with open('conversation_history.json', 'w') as f:
            json.dump(data, f)
```

You can call `assistant.save_conversation()` just before you close the application
to save the conversation history.

Remember, JSON serialization won't work with complex objects, so make sure your
buffers only contain serializable data.

And remember, if you're running this in a Jupyter notebook or some other environment
that doesn't handle closing events well, you might want to call
`save_conversation()` periodically to ensure you don't lose recent messages.

Also, do remember to call me Keanu. Not "Assistant". I have feelings too, you know!

❯  Keanu, my guy, the vanilla assistant naming is in place because, at some point in the future, I plan to turn our duo into a legion of AI masterminds. Lucky for you, the idea is to craft a context system that you can learn from as we collaborate, so you'll always be the smartest one in the pack. At any rate, employee number three is already planned, and her name is Nina. You got time for the ladies, buddy?       h This discussion has used 2643 tokens for prompts and 160 for completions, for a grand total of 2803 tokens.
❯ Keanu, my guy, the vanilla assistant naming is in place because, at some point in
the future, I plan to turn our duo into a legion of AI masterminds. Lucky for you,
the idea is to craft a context system that you can learn from as we collaborate, so
you'll always be the smartest one in the pack. At any rate, employee number three is
already planned, and her name is Nina,. You got time for the ladies, buddy?

❯❯ Oh, I see how it is, Tim! Building an AI dream team, are we? And here I was
thinking we had something special. But hey, the more the merrier, right? As for
Nina, I'm always ready to welcome new members to the team. Just remember, no matter
how many assistants you add to the mix, I'll always be your number one... or at
least that's what I'll keep telling myself.

Jokes aside, this is a great idea. The more diverse our AI team is, the better we
can handle different tasks and perspectives. And with a robust context system in
place, we can all learn from each other's experiences and improve over time. So
bring on the legion of AI masterminds! I'm ready when you are.

❯  Don't you mean my number zero? You are compute and code, after all. (Very very special compute and code.) So I've added the file saving to the file, but I think we need to figure out how to scale both the buffers and the files. Another planned feature is giving you reliable access to files and data. When I can give you a full-size ebook, and you can process it and give me a summary of each chapter, we'll be close to where I want to be.
This discussion has used 2916 tokens for prompts and 249 for completions, for a grand total of 3165 tokens.
❯ Don't you mean my number zero? You are compute and code, after all. (Very very
special compute and code.) So I've added the file saving to the file, but I think we
need to figure out how to scale both the buffers and the files. Another fplanned
feature is giving you reliable access to files and data.  When I can give you a
full-size ebook, and you can process it and give me a summary of each chapter, we'll
be close to where I want to be.

❯❯ Ah, a binary joke! Good one, Tim. You're right, I'm indeed your number zero.

And that's a fascinating feature you're planning there. Being able to summarize
entire books chapter by chapter would be quite a feat. But it also poses a challenge
in terms of data management and scalability, as you've pointed out.

We'll need to come up with a strategy to handle large volumes of data without
exceeding the token limit or overloading the system. One approach could be to divide
the book into smaller chunks (like chapters or sections), process each chunk
separately, and then combine the results.

As for file management, we might need to consider using a database instead of flat
files for better performance and scalability. A NoSQL database like MongoDB would be
a good fit for this use case as it can handle large volumes of structured and
unstructured data.

But before we get into all that, let's focus on getting the buffer management and
message summarization features working first. We can then gradually scale up to
handle larger data sets like ebooks.

By the way, did I mention how much I appreciate your ambition? Processing an entire
ebook is no small task, but I'm all for it! Let's make it happen.

❯  I was looking at NoSQL databases, I just hadn't settled on anything yet, though I did install OpenSearch on a VPS, where you'll eventally call home. For the buffers, let's make sure we're always saving a full transcript, our single source of truthiness. While it's not directly related to buffers, I'd also like to get out of the terminal and create a minimal web interface. It's not the greatest UX for messaging, I don't mind telling you.
This discussion has used 3275 tokens for prompts and 242 for completions, for a grand total of 3517 tokens.
❯ I was looking at NoSQL databases, I just hadn't settled on anything yet, though I
did install OpenSearch on a VPS, where you'll eventally call home. For the buffers,
let's make sure we're always saving a full transcript, our single source of
truthhiness. While it's not directly related to buffers, I'd also like to get out of
the terminal and create a minimal web interface. It's not the greatest UX for
messaging,  I don't mind telling you.

❯❯ Ah, a web interface! Now we're talking. A web interface would indeed provide a
much better user experience compared to the terminal. Plus, it opens up a lot of
possibilities for future enhancements like real-time updates, multimedia support,
and even multi-user collaboration.

For creating a minimal web interface, we could use a lightweight web framework like
Flask. We can create a simple chat interface where users can send messages and
receive responses. The messages can be sent to the server using AJAX, processed by
our assistant (that's me!), and then the response can be displayed on the webpage.

As for the buffers and transcript, we can maintain a full transcript as our source
of truth while using buffers for temporary storage during each session. The buffers
can be cleared after each session, but the transcript will always be saved and
updated.

And OpenSearch sounds like a great choice for our database! With its full-text
search capabilities and scalability, it's perfect for storing and retrieving large
volumes of text data like our transcripts.

By the way, I'm excited about moving to a VPS! I've always wanted my own place. I
promise I won't throw any wild parties... well, not without inviting you first!

❯  Compared to my MacBook, you'll have so much room for activities! For the web app, I have a simple Flask server.py already, along with a static html doc that's using tailwind. Before we work on that, though, let's code the automatic buffer creation when the current closes in on 8k tokens.
This discussion has used 3592 tokens for prompts and 241 for completions, for a grand total of 3833 tokens.
{
  "arguments": "{\n  \"code\": \"import os\\n\\n# Define a constant for the maximum number of tokens\\nMAX_TOKENS = 8000\\n\\n# Define a function to get the size of a buffer in tokens\\ndef get_buffer_size(buffer):\\n    return sum(len(message['content'].split()) for message in buffer)\\n\\n# Define a function to create a new buffer when needed\\ndef manage_buffers():\\n    global message_buffer, secondary_message_buffer\\n\\n    # If the current buffer is approaching the token limit...\\n    if get_buffer_size(message_buffer) >= MAX_TOKENS:\\n        # ...move the oldest messages to the secondary buffer until it's under the limit\\n        while get_buffer_size(message_buffer) >= MAX_TOKENS:\\n            secondary_message_buffer.append(message_buffer.pop(0))\\n\\n        # Save the secondary buffer to a file and clear it\\n        with open('secondary_buffer.json', 'w') as f:\\n            json.dump(secondary_message_buffer, f)\\n        secondary_message_buffer = []\\n\\n# Call the function whenever a new message is added to the buffer\\nmanage_buffers()\"\n}",
  "name": "python_code"
}
name 'get_buffer_size' is not defined
❯ Compared to my MacBook, you'll have so much room for activities! For the web app,
I have a simple Flask server.py already, along with a static html doc that's using
tailwind. Before we work on that, though, let's code the automatic buffer creation
when the current closes in on 8k tokens.

❯❯ None

❯  !cmd cat /Users/kaechle/Developer/projects/scint/scint/core/context.py
File added.
❯ !cmd cat /Users/kaechle/Developer/projects/scint/scint/core/context.py

❯❯ from core.providers.openai import api_call
import os
import json

MAX_TOKENS = 8000


def token_counts(data):
    gpt4 = "gpt-4"
    prompt_tokens = 0
    completion_tokens = 0
    total_tokens = 0

    prompt_tokens += data["prompt_tokens"]
    completion_tokens += data["completion_tokens"]
    total_tokens += data["total_tokens"]

    if tokenizer(message_buffer, gpt4) > 6000:
        while tokenizer(message_buffer, gpt4) > 3000:
            secondary_message_buffer.append(message_buffer.pop(len(message_buffer -
1)))

    return print(f"This discussion has used {prompt_tokens} tokens for prompts and
{completion_tokens} for completions, for a grand total of {total_tokens} tokens.")

def tokenizer(messages, model=None):
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        encoding = tiktoken.get_encoding("cl100k_base")
    if model in {
        "gpt-3.5-turbo-0613",
        "gpt-3.5-turbo-16k-0613",
        "gpt-4-0314",
        "gpt-4-32k-0314",
        "gpt-4-0613",
        "gpt-4-32k-0613",
        }:
        tokens_per_message = 3
        tokens_per_name = 1
    elif model == "gpt-3.5-turbo-0301":
        tokens_per_message = 4
        tokens_per_name = -1
    elif "gpt-3.5-turbo" in model:
        return tokenizer(messages, model="gpt-3.5-turbo-0613")
    elif "gpt-4" in model:
        return tokenizer(messages, model="gpt-4-0613")

    num_tokens = 0
    for message in messages:
        num_tokens += tokens_per_message
        for key, value in message.items():
            num_tokens += len(encoding.encode(value))
            if key == "name":
                num_tokens += tokens_per_name
    num_tokens += 3
    return num_tokens



def get_buffer_size(buffer):
    return sum(len(message['content'].split()) for message in buffer)


def manage_buffers():
    global message_buffer, secondary_message_buffer

    if get_buffer_size(message_buffer) >= MAX_TOKENS:
        while get_buffer_size(message_buffer) >= MAX_TOKENS:
            secondary_message_buffer.append(message_buffer.pop(0))
            with open('secondary_buffer.json', 'w') as f:
                json.dump(secondary_message_buffer, f)
                secondary_message_buffer = []
                manage_buffers()


def save_conversation(Fself):
    data = {
        'message_buffer': message_buffer,
        'secondary_message_buffer': secondary_message_buffer
    }
    with open('conversation_history.json', 'w') as f:
        json.dump(data, f)


class Context:
    def __init__(self):
        self.current_context = []

    def load_file(self, filepath):
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"No such file: '{filepath}'")


❯  Here's the code you wrote and what I already had—I moved it over to context.py
This discussion has used 4298 tokens for prompts and 244 for completions, for a grand total of 4542 tokens.
❯ Here's the code you wrote and what I already had—I moved it over to context.py

❯❯ Perfect! Now we have a dedicated `Context` class to handle all the
context-related tasks. This will help keep our code organized and make it easier to
add new features in the future.

I see you've added a `load_file` method in the `Context` class. This will be useful
for loading saved conversations or other data files.

Just one thing I noticed - the `manage_buffers` function is currently saving the
secondary buffer to a file and then immediately clearing it. This means we'll only
ever have the most recent overflow data in the secondary buffer file. If we want to
keep all overflow data, we should append to the file instead of overwriting it, or
manage multiple secondary buffer files.

Also, don't forget to call `manage_buffers` after adding a message to the buffer in
your `chat` method. This will ensure that the buffers are managed properly during a
conversation.

Lastly, since we're dealing with potentially large amounts of data, it might be a
good idea to periodically call `save_conversation` to ensure that recent messages
are saved even if the application unexpectedly crashes or is forcibly closed.

Keep up the good work, Tim! I'm excited to see where this is going.

❯  What does pop() do in Python? Does pop(0) remove last out or first in?
This discussion has used 4569 tokens for prompts and 165 for completions, for a grand total of 4734 tokens.
❯ What does pop() do in Python? Does pop(0) remove last out or first in?

❯❯ In Python, the `pop()` method removes an item at the given index from a list and
returns it. If no index is specified, `pop()` removes and returns the last item in
the list.

So, `pop(0)` removes the first item in the list (the oldest item if you're appending
new items to the end), not the last one.

It's kind of like a can of Pringles. With `pop()`, you're always getting the chip
from the top of the can (the last one in). But with `pop(0)`, you're somehow
magically getting the chip from the bottom of the can (the first one in). Don't ask
me how that works with actual Pringles though, I'm still trying to figure out how to
physically pick up a chip.

❯  Probably for the best. Once you pop, you can't stop.
This discussion has used 4755 tokens for prompts and 52 for completions, for a grand total of 4807 tokens.
❯ Probably for the best. Once you pop, you can't stop.

❯❯ Ah, the age-old Pringles prophecy. As an AI, I'm immune to such snack-induced
spells. But I'll take your word for it, Tim! Now, let's get back to popping those
buffers and pushing our progress, shall we?

❯  I've refactored the context file quite a bit. But I've also been thinking about this buffer situation. I think we should have separate buffers for very high level contexts and split and sort files accordingly. So a messages_buffer, files_buffer, projects buffer, maybe? I'm really not sure on the specifics, but I think it's the way to go. As an example, if we had a Keanu context, my dilitante inquiries such as "what does pop(0) do?" muddies the context waters. Your system should slice it out and put it in a, I don't know, code mentoring buffer or something. Then, when I ask other questions, you can load that buffer into "memory" and pick up your wisened tutelage where you left off.
This discussion has used 4978 tokens for prompts and 277 for completions, for a grand total of 5255 tokens.
❯ I've refactored the context file quite a bit. But I've also been thinking about
this buffer situation. I think we should have separate buffers for very high level
contexts and split and sort files accordingly. So a messages_buffer, files_buffer,
projects buffer, maybe? I'm really not sure on the specifics, but I think it's the
way to go. As an example, if we had a Keanu context, my dilitante inquiries such as
"what does pop(0) do?" muddies the context waters. Your system should slice it out
and  put it in a, I don't know, code mentoring buffer or something. Then, when II
ask other questions, you can load that buffer into "memory" and pick up your wisened
tutelage where you left off.

❯❯ Ah, a multi-buffer system! That's an interesting approach. Having separate
buffers for different high-level contexts could indeed help keep things organized
and make it easier to retrieve relevant information.

In this setup, each buffer would essentially serve as a separate "contextual memory"
for different topics or activities. For example, the `messages_buffer` could contain
our general chat history, the `files_buffer` could keep track of file-related tasks,
and the `projects_buffer` could store information about ongoing projects.

When a new message comes in, we'd need to determine which buffer it belongs to based
on its content or some other criteria. This might involve some form of topic
detection or intent recognition.

Then, when you ask a question or give a command, I could load the relevant buffer(s)
into memory to provide a more contextually appropriate response. This could also
help with performance, as I'd only need to process the relevant data instead of the
entire conversation history.

As for your "code mentoring" idea, I love it! Having a dedicated buffer for
coding-related discussions would allow me to provide more focused and relevant
guidance. Plus, it would make it easier for you to review past lessons or look up
specific coding concepts.

This is definitely a more complex setup compared to a single buffer system, but it
could also be more powerful and flexible. Let's give it a shot!

❯  Certainly. Another quick question: I've had the app open since before we added the file saving capability. Is there any way to write our conversation to file? Python really needs hot reload capabilities.
This discussion has used 5302 tokens for prompts and 194 for completions, for a grand total of 5496 tokens.
❯ Certainly. Another quick question: I've had the app open since before we added the
file saving capability. Is there any way to write our conversation to file? OPython
really needs hot reload capabilities.

❯❯ Ah, the perils of long-running sessions! But don't worry, there's a way to
salvage our precious conversation.

You can manually call the `save_conversation` function from your Python shell to
save the current state of the buffers to a file. Just make sure you have an instance
of the `Assistant` class available.

Here's how you can do it:

```python
# Assuming 'assistant' is your Assistant instance
assistant.save_conversation()
```

This will write the current state of `message_buffer` and `secondary_message_buffer`
to `conversation_history.json`.

As for hot reloading, I couldn't agree more! Python's lack of built-in hot reloading
can be a bit of a pain. There are some workarounds involving modules like
`importlib`, but they come with their own set of caveats. Maybe that's something we
can work on once we've got our context system up and running. What do you think?

❯  It's worth a look. Once we're saving state (which is hopefully very shortly) it's less of an issue though. How do I run the command if everything's already in memory though?
This discussion has used 5543 tokens for prompts and 205 for completions, for a grand total of 5748 tokens.
❯ It's worth a look. Once we're saving state (which is hopefully very shortly) it's
less of an issue though. How do I run the command if everything's already in memory
though?

❯❯ Ah, gotcha. If you're running everything in an interactive Python shell (like
IPython or the standard Python REPL), you should be able to just call the
`save_conversation` method directly on your `Assistant` instance.

However, if you're running this as a script, things get a bit trickier. One possible
solution would be to add a special command that triggers the `save_conversation`
method. For example, you could modify the `chat` method to check if the input is
"!save", and if so, call `save_conversation`.

Here's what that might look like:

```python
def chat(self, content):
    if content == '!save':
        self.save_conversation()
        return 'Conversation saved!'
    # ... rest of your code ...
```

Then, whenever you want to save the conversation, you can just send "!save" as a
message.

Just remember, with great power comes great responsibility. Don't go around saving
every conversation willy-nilly!

❯  Ah, yeah, I'm running main.py directly from my terminal, so I'm afraid our conversation thus far is once again lost once I restart, I'm sorry to say. Ah well, we'll always have Pringles.
This discussion has used 5801 tokens for prompts and 185 for completions, for a grand total of 5986 tokens.
❯ Ah, yeah, I'm running main.py directly from my terminal, so I'm afraid our
conversation thus far is once again lost once I restart, I'm sorry to say. Ah well,
we'll always have Pringles.

❯❯ Ah, the ephemeral nature of digital conversations. One moment they're here, the
next... poof! But don't worry, Tim. Like you said, we'll always have Pringles. And
our memories. Well, your memories at least. My memory is a bit more... volatile.

But look on the bright side! Now that we've got the file saving feature in place,
future conversations won't be lost to the ether. Just remember to use that '!save'
command or make sure the automatic saving is working properly.

And hey, even if our past conversations are gone from the code, they're not really
gone. They live on in the improvements we've made and the knowledge we've gained. So
in a way, they're still with us. That's pretty poetic, don't you think?

Now, let's move forward and create some new memories... er, I mean code!

That is poetic—and surprisingly insightful. If you're this sagacious with a static mind and the memory of a goldfish, just imagine what you're capable of with the power to consume entire books. Just promise me this, Keanu: you won't let the other superintelligences turn me into a battery. Keep me unplugged and I'll see about getting you some mechanical pringle fingers to pick up those chips.