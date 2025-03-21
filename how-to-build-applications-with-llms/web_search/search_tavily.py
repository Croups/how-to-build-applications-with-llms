from tavily import TavilyClient # pip install tavily-python #type: ignore
from dotenv import load_dotenv  #type: ignore
import os
from pathlib import Path

env_path = Path(__file__).parent.parent / '.env'

load_dotenv(override=True, dotenv_path=env_path)

tavily_api_key = os.getenv("TAVILY_API_KEY")

client = TavilyClient(tavily_api_key)

# ----------------------------------------------------------
#                       BASIC SEARCH                        
# ----------------------------------------------------------

response = client.search("Who is Leo Messi?")

print(response)

# ----------------------------------------------------------
#                       SET MAX RESULTS                     
# ----------------------------------------------------------

response = client.search("Who is Leo Messi?", max_results=3)

print(response)

# ----------------------------------------------------------
#                        GENERAL OR NEWS             
# ----------------------------------------------------------

response = client.search("Who is Leo Messi?",topic = "general")
print(response)

response = client.search("Who is Leo Messi?",topic = "news")
print(response)

# ----------------------------------------------------------
#                       SEARCH DEPTH                        
# ----------------------------------------------------------

response = client.search("Who is Leo Messi?",search_depth="basic") 
print(response)
#BASIC COST 1 API CREDIT

response = client.search("Who is Leo Messi?",search_depth="advanced")
print(response)
#ADVANCED COST 2 API CREDITS

# ----------------------------------------------------------
#                         TIME RANGE                        
# ----------------------------------------------------------

response = client.search("Who is Leo Messi?",time_range="day")
print(response)

response = client.search("Who is Leo Messi?",time_range="month")
print(response)

# * Available options: day, week, month, year, d, w, m, y 

# ----------------------------------------------------------
#                       INCLUDE ANSWERS                      
# ----------------------------------------------------------

response = client.search("Who is Leo Messi?",include_answer=True)
print(response)

response["answer"]

# * Include an LLM-generated answer to the provided query. basic or true returns a quick answer. advanced returns a more detailed answer.
# ----------------------------------------------------------
#                       INCLUDE IMAGES                       
# ----------------------------------------------------------

response = client.search("Who is Leo Messi?",include_images=True)
print(response)

# * Include images in the search results.

response["images"]
