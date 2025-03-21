
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
#                   DEVELOPER ROLE                      
# ----------------------------------------------------------

completion = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "developer", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)

# ----------------------------------------------------------
#                   SYSTEM ROLE                      
# ----------------------------------------------------------

completion = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)

# ----------------------------------------------------------

