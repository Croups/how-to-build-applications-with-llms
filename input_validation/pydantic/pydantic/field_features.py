
from pydantic import BaseModel, Field

# ----------------------------------------------------------
#                      PYDANTIC MODEL                        
# ----------------------------------------------------------

class User(BaseModel):
    id: int 
    name: str
    email: str
    age: int
    
user = User(id=1, name="John Doe", email="john.doe@example.com", age=30)

# ----------------------------------------------------------
#                      DEFAULT VALUES                        
# ----------------------------------------------------------


class User(BaseModel):
    id: int 
    name: str = "ENES" 
    email: str 
    age: int = 22
    
user = User(id=1, name="John Doe", email="john.doe@example.com", age=30)
user = User(id=1,email="enes@example.com")


# ----------------------------------------------------------
#                    NUMERIC FIELD FEATURES                   
# ----------------------------------------------------------


class User(BaseModel):
    id: int
    name: str
    email: str
    age: int = Field(gt=18, lt=30) 
    
# ? gt: greater than
# ? lt: less than
# ? ge: greater than or equal to
# ? le: less than or equal to

user = User(id=1, name="John Doe", email="john.doe@example.com", age=25)
invalid_user = User(id=1, name="Elisa", email="elisa.doe@example.com", age=15) # This will raise a validation error


# ----------------------------------------------------------
#                      TEXT FIELD FEATURES                        
# ----------------------------------------------------------


class User(BaseModel):
    username: str = Field(min_length=3)
    bio: str = Field(max_length=10)
    phone_number: str = Field(pattern=r'^\d*$')
    
user = User(username="john", bio="developer", phone_number="1234567890")
invalid_user = User(username="jo", bio="this bio is way too long for the field", phone_number="ABC") # This will raise a validation error


# ----------------------------------------------------------
#                      DECIMAL FIELD FEATURES                        
# ----------------------------------------------------------


from decimal import Decimal

class User(BaseModel):
    account_balance: Decimal = Field(max_digits=5, decimal_places=2)

user = User(account_balance=Decimal('123.45'))
user = User(account_balance=Decimal('123.456')) # This will raise a validation error
user = User(account_balance=Decimal('12456')) # This will raise a validation error


# ? ----------------------------------------------------------
# ?           YOU CAN FIND ALL FIELD FEATURES BELOW                    
# ? ----------------------------------------------------------

# * https://docs.pydantic.dev/latest/concepts/fields/
