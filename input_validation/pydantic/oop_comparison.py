from pydantic import BaseModel

# ----------------------------------------------------------
#                     PYDANTIC MODEL                        
# ----------------------------------------------------------

class User(BaseModel):
    id: int
    name: str
    email: str
    age: float

# Create a user instance
user = User(id=1, name="John Doe", email="john.doe@example.com", age=30)

# ----------------------------------------------------------
#                   TRADITIONAL OOP MODEL                   
# ----------------------------------------------------------

class TraditionalUser:
    def __init__(self, id: int, name: str, email: str, age: float):
        self.id = id
        self.name = name
        self.email = email
        self.age = age
    
    def __str__(self):
        return f"TraditionalUser(id={self.id}, name='{self.name}', email='{self.email}', age={self.age})"

traditional_user = TraditionalUser(id=1, name="John Doe", email="john.doe@example.com", age=30)

# ? ----------------------------------------------------------
# ?                   COMPARISON NOTES                        
# ? ----------------------------------------------------------
# ? 1. Pydantic provides automatic validation based on type hints
# ? 2. Traditional OOP requires manual validation if needed
# ? 3. Pydantic models have built-in serialization/deserialization
# ? 4. Both approaches allow for attribute updates after creation

# ----------------------------------------------------------
#                 UPDATING VALUES COMPARISON                
# ----------------------------------------------------------

# Updating Pydantic model values
user.name = "Jane Smith"
user.age = 35
print(f"Updated Pydantic user: {user}")

# Updating Traditional OOP model values
traditional_user.name = "Jane Smith"
traditional_user.age = 35
print(f"Updated Traditional user: {traditional_user}")

# ----------------------------------------------------------
#                 INVALID INPUT COMPARISON                  
# ----------------------------------------------------------

user = User(id=1, name="John Doe", email="john.doe@example.com", age="hi")

traditional_user = TraditionalUser(id=1, name="John Doe", email="john.doe@example.com", age="hi")
print(traditional_user)

# ----------------------------------------------------------
#                 WRONG DATA TYPE COMPARISON                
# ----------------------------------------------------------

user = User(id=1, name="John Doe", email="john.doe@example.com", age=20)

traditional_user = TraditionalUser(id=1, name="John Doe", email="john.doe@example.com", age=20)
print(traditional_user)

# ----------------------------------------------------------
#                 SERIALIZATION COMPARISON                     
# ----------------------------------------------------------

# Pydantic serialization to dict and JSON
user_dict = user.model_dump()  
user_json = user.model_dump_json() 

# Traditional OOP requires manual serialization
def traditional_to_dict(user):
    return {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "age": user.age
    }

import json
traditional_dict = traditional_to_dict(traditional_user)
traditional_json = json.dumps(traditional_dict)







