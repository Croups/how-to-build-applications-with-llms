
from pydantic import BaseModel

class Person(BaseModel):
    name: str
    age: int
    email: str

user = Person(name="John Doe", age=20, email="john.doe@example.com")

# ----------------------------------------------------------
# !  WHAT IF WE RECEIVE DATA FROM OTHER SOURCES?   
# ----------------------------------------------------------

sample_api_response = {
    "user": {
        "personal_info": {
            "name": "John Doe",
            "age": 20,
            "email": "john.doe@example.com"
        },
        "address": {
            "street": "123 Main St",
            "city": "New York",
            "state": "NY",
        }
    },
    "metadata": {
        "request_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "timestamp": "2023-07-15T14:32:17Z",
        "api_version": "v2.1.3"
    },
    "stats": {
        "last_login": "2023-07-14T09:45:22Z",
        "subscription_status": "premium",
        "activity_score": 78.5
    }
}

# ? HOW TO CONVERT THIS DATA TO PYDANTIC MODEL?

# ----------------------------------------------------------
# !  SOLUTION 1: MANUEL PARSING
# ----------------------------------------------------------

dummy_data = '"name" : "enes" , "id" : "abc123"'

class Person(BaseModel):
    name: str 
    id: str 

# Parse the data manually
data_dict = {}
pairs = dummy_data.split(",")
for pair in pairs:
    # Remove quotes and spaces, then split by :
    key, value = [x.strip().replace('"', '') for x in pair.split(":")]
    data_dict[key] = value

# Create Person instance using parsed data
person = Person(**data_dict)
print(person)

# ----------------------------------------------------------
# !  SOLUTION 2: TYPE ADAPTERS
# ----------------------------------------------------------

from pydantic import TypeAdapter

item_data = {'id': 1, 'name': 'My Item'}

class Item(BaseModel):
    id: int
    name: str

item = TypeAdapter(Item).validate_python(item_data)

#  ----------------------------------------------------------
# ?   READ DATA FROM JSON AND CONVERT IT TO PYDANTIC MODEL                           
#  ----------------------------------------------------------

from pydantic import PositiveInt
import pathlib 

class Person(BaseModel):
    name: str
    age: PositiveInt
    email: str
    
json_string = pathlib.Path('data/person.json').read_text()
person = TypeAdapter(Person).validate_json(json_string)

# * Or 

person = Person.model_validate_json(json_string)

# ----------------------------------------------------------
# ?    WHAT IF WE HAVE A LIST OF PEOPLE?                           
# ----------------------------------------------------------

class Person(BaseModel):
    name: str
    age: PositiveInt
    email: str

person_list_adapter = TypeAdapter(list[Person])  

json_string = pathlib.Path('data/people.json').read_text()
people = person_list_adapter.validate_json(json_string)

