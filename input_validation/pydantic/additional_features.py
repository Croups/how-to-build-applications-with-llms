from datetime import datetime
import random
from typing import Any, Literal, Optional
from pydantic import BaseModel, Field

# ----------------------------------------------------------
#                  PYDANTIC MODEL                        
# ----------------------------------------------------------

class User(BaseModel):
    id: int
    name: str
    is_active: bool

user = User(id=1, name="John Doe", is_active=True)

                    
# ----------------------------------------------------------
#                      DATETIME                       
# ----------------------------------------------------------

class User(BaseModel):
    id: int
    name: str
    is_active: bool
    created_at: datetime

user = User(id=1, name="John Doe", is_active=True, created_at=datetime.now())

# ----------------------------------------------------------
#                       UUID                       
# ----------------------------------------------------------

from uuid import uuid4

class User(BaseModel):
    id: str = Field(default_factory=lambda: uuid4().hex)
    name: str
    is_active: bool

user = User(name="John Doe", is_active=True)
print(user)
# ----------------------------------------------------------
#                        RANDOM                    
# ----------------------------------------------------------

class User(BaseModel):
    id: int = 1
    name: str
    age: int = Field(default_factory=lambda: random.randint(19, 24), gt=18, lt=25)

user = User(name="Enes")
print(user)

# ----------------------------------------------------------
#                      ENUM                       
# ----------------------------------------------------------

from enum import Enum

class UserStatus(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    BANNED = "banned"
    PENDING = "pending"
    DELETED = "deleted"

class User(BaseModel):
    status: UserStatus

user = User(status=UserStatus.INACTIVE)

user.status
user.status.value

# ----------------------------------------------------------
#                      LITERAL                       
# ----------------------------------------------------------

class User(BaseModel):
    id: int
    name: str
    email: str
    role: Literal["admin", "user", "moderator"]

user = User(id=1, name="John Doe", email="john.doe@example.com", role="GM")

user.role


# ----------------------------------------------------------
#                      ANY DATA TYPE                      
# ----------------------------------------------------------

class User(BaseModel):
    data : Any  

user = User(data="Hello, World!")
user = User(data=123)
user = User(data=True)
user = User(data=None)
user = User(data=[])

#  ----------------------------------------------------------
#                       OPTIONAL                   
#  ----------------------------------------------------------

class User(BaseModel):
    id : int
    name : Optional[str]
    email : Optional[str] = None


user = User(id=1, name="John Doe", email="john.doe@example.com")
user = User(id=1, name="John Doe")
user = User(id=1, name=None)

# ? CHECK REQUIRED, OPTIONAL, NOT REQUIRED, DEFAULT BELOW :
# * https://docs.pydantic.dev/latest/migration/#required-optional-and-nullable-fields