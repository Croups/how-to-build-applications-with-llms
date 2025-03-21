from openai import OpenAI
from pydantic import BaseModel, Field

client = OpenAI()

# ----------------------------------------------------------
#                     OPENAI API CALL                        
# ----------------------------------------------------------

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ]
)

raw_response = completion.choices[0].message.content

# ----------------------------------------------------------
#                     STRUCTURED OUTPUTS                        
# ----------------------------------------------------------

class Country(BaseModel):
    capital : str = Field(description="The capital of the country")
    
completion = client.beta.chat.completions.parse(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ],
    response_format=Country
)
structured_response = completion.choices[0].message.parsed


# LET'S TRY TO EXTRACT AND REUSE CAPITAL   
                      
#  ----------------------------------------------------------
#                   RAW RESPONSE 
#  ----------------------------------------------------------

# LET'S SAY WE WANT TO PASS THIS OUTPUT TO ANOTHER FUNCTION AS INPUT

import re

capital = re.search(r"The capital of France is (.*)", raw_response)
capital = capital.group(1)
print(capital)

#  What if AI returns just "Paris"
#  What if AI returns "Paris is the capital of France"
#  What if AI returns "I can define the capital of France as Paris"

#  ----------------------------------------------------------
#                   STRUCTURED RESPONSE
#  ----------------------------------------------------------

capital = structured_response.capital
print(capital)

# ----------------------------------------------------------

def determine_capital(capital: str) -> bool:
    if capital == "Paris":
        return True
    else:
        return False

print(determine_capital(capital))


# ----------------------------------------------------------