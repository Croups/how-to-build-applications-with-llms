from dotenv import load_dotenv  #type: ignore
import os
from pathlib import Path

# ----------------------------------------------------------
#                   CHECK CURRENT DIRECTORY                       
# ----------------------------------------------------------
os.system("pwd")
# ----------------------------------------------------------
#                   LOAD ENVIRONMENT VARIABLES                       
# ----------------------------------------------------------

env_path = Path(__file__).parent.parent.parent / '.env'

load_dotenv(override=True, dotenv_path=env_path)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# ----------------------------------------------------------
#                   MANUEL SETTING                        
# ----------------------------------------------------------

os.environ["OPENAI_API_KEY"] = "OPENAI_API_KEY"

print(os.getenv("OPENAI_API_KEY"))
