
from pydantic import BaseModel

# ----------------------------------------------------------
#                        MODEL DEFINITION                        
# ----------------------------------------------------------

class User(BaseModel):
    id: int
    name: str
    email: str
    age : int 
    
user = User(id=1, name="John Doe", email="john.doe@example.com", age=20)

# ----------------------------------------------------------
#                         TEST INVALID USER                       
# ----------------------------------------------------------

invalid_user_2 = User(id=1, name="John Doe", email="john.doe@example.com")
invalid_user_3 = User(id=1, name="John Doe", age=20)
invalid_user_4 = User(id=1, name="John Doe", email="john.doe@example.com", age="twenty")
invalid_user_5 = User(id=1, name="John Doe", email=5, age=20)


# ? ----------------------------------------------------------
# ?                      INFO SECTION                     
# ? ----------------------------------------------------------

# ? Pydantic is a data validation library that uses Python type annotations to validate data structures.
# ? It provides clear error messages when validation fails and automatically converts data types when possible.
# ? In the examples above, invalid_user attempts will fail with validation errors because Pydantic enforces
# ? The type hints defined in the User model. This helps catch errors early in development.


# ----------------------------------------------------------
#                         AUTOMATIC TYPE CONVERSION                        
# ----------------------------------------------------------

user_2 = User(id=1, name="John Doe", email="john.doe@example.com", age="20")
user_3 = User(id="1", name="John Doe", email="john.doe@example.com", age=20)


class Price(BaseModel):
    amount: float
    currency: str


price = Price(amount=100, currency="USD")
price = Price(amount="100", currency="USD")

