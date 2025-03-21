
from openai import OpenAI
client = OpenAI()


# ----------------------------------------------------------
#                   BASIC OPENAI API CALL                       
# ----------------------------------------------------------

completion = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)

# ----------------------------------------------------------
#                   LET'S MAKE IT FUNCTIONAL                      
# ----------------------------------------------------------

def call_openai(prompt, model="gpt-4o"):
    completion = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return completion.choices[0].message

response = call_openai("Hello!")
print(response)

# ----------------------------------------------------------
#                   OVERRIDE THE MODEL                       
# ----------------------------------------------------------

response = call_openai("Hello!", model="gpt-3.5-turbo")
print(response)