from enum import Enum
from typing import List, Literal
from openai import OpenAI # type: ignore
from pydantic import BaseModel, Field # type: ignore

client = OpenAI()

# TASK IS TO CREATE A SYSTEM THAT GENERATES ARTICLES FOR A BLOG                        

# ----------------------------------------------------------
#              VERSION 1 : SIMPLE ARTICLE WRITER                     
# ----------------------------------------------------------

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant that generates articles for a blog."},
        {"role": "user", "content": "I want to write an article about the benefits of using AI in the workplace."}
    ]
)

print(completion.choices[0].message.content)

# ! WE DON'T HAVE ANY CONTROL OVER THIS SYSTEM

# ----------------------------------------------------------
#              VERSION 2 : STRUCTURED ARTICLE WRITER                     
# ----------------------------------------------------------

class Article(BaseModel):
    title: str
    content: str
    conclusion: str
    references: List[str]
    
completion = client.beta.chat.completions.parse(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant that generates articles for a blog."},
        {"role": "user", "content": "I want to write an article about the benefits of using AI in the workplace."}
    ],
    response_format=Article
)

response = completion.choices[0].message.parsed

response.references

# ! WE HAVE CONTROL OVER THE STRUCTURE OF THE ARTICLE, BUT IT'S NOT CUSTOMIZABLE

# ----------------------------------------------------------
#   VERSION 3 : PASS USER PREFERENCES TO THE SYSTEM PROMPT                    
# ----------------------------------------------------------

class Preferences(BaseModel):
    tone: str
    length: Literal["short", "medium", "long"]
    complexity: str
    topic: str
    
class Article(BaseModel):
    title: str = Field(description="The title of the article")
    content: str = Field(description="The content of the article")
    conclusion: str = Field(description="The conclusion of the article")
    references: List[str] = Field(description="A list of references to the sources used in the article")
    
preferences = Preferences(tone="formal", length="short", complexity="simple", topic="Why OPENAI is the best AI company")
    
completion = client.beta.chat.completions.parse(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": f"You are a helpful assistant that generates articles for a blog with user preferences : {preferences}."},
        {"role": "user", "content": "I want to write an article about the benefits of using AI in the workplace."}
    ],
    response_format=Article
)

response = completion.choices[0].message.parsed

# preferences.topic 
# response.title

# ----------------------------------------------------------
#   VERSION 4 : LET'S HAVE EVEN MORE CONTROL OVER THE ARTICLE                     
# ----------------------------------------------------------

class WritingStyle(Enum):
    FORMAL = "formal"
    INFORMAL = "informal"
    CONCISE = "concise"
    VERBOSE = "verbose"
    PIRATE = "pirate" 

class Complexity(Enum):
    SIMPLE = "simple"
    MEDIUM = "medium"
    COMPLEX = "complex"
    
class Preferences(BaseModel):
    writing_style: WritingStyle
    complexity: Complexity
    topic: str
     
class Section(BaseModel):
    title: str = Field(description="The title of the section")
    content: str = Field(description="The content of the section")
    
class Reference(BaseModel):
    title: str = Field(description="The title of the reference")
    url: str = Field(description="The url of the reference")

class StructuredBlog(BaseModel):
    title: str = Field(description="The title of the blog")
    sections: List[Section] = Field(description="A list of sections that make up the blog")
    introduction: str = Field(description="The introduction of the blog")
    conclusion: str = Field(description="The conclusion of the blog")
    references: List[Reference] = Field(description="A list of references to the sources used in the blog")
    abstract: str = Field(description="A short summary of the blog")
    
class Blog(BaseModel):
    article : str = Field(description="The final version of the blog")
    references : List[Reference] = Field(description="A list of references to the sources used in the blog")
    
# DEFINE PREFERENCES

preferences = Preferences(writing_style=WritingStyle.FORMAL, complexity=Complexity.SIMPLE, topic="Google's impact on open source")

# SET UP THE SYSTEM PROMPT FOR THE BLOG STRUCTURE GENERATION

generate_blog_structure_system_prompt = f"""
You are a writer for a blog.
You will be given a topic and a set of preferences.
You will need to generate an article that is written in the style of the preferences.

Writing style: {preferences.writing_style}

Complexity: {preferences.complexity}

Topic: {preferences.topic}
"""

# DEFINE THE FUNCTION TO GENERATE THE BLOG STRUCTURE

def generate_blog_structure(preferences: Preferences) -> StructuredBlog:
    completion = client.beta.chat.completions.parse(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": generate_blog_structure_system_prompt},
            {"role": "user", "content": "Write a blog post for my blog."}
        ],
        response_format=StructuredBlog
    )

    return completion.choices[0].message.parsed

# GENERATE THE BLOG STRUCTURE

blog_structure = generate_blog_structure(preferences)

# DEFINE THE SYSTEM PROMPT FOR THE BLOG REWRITING

generate_blog_system_prompt = f"""
You are a rewriter specialized in blogs.
You will be given a blog structure and content with a set of preferences.
Your task is to rewrite the blog with a good readability and a good flow.

Title : {blog_structure.title}

Introduction : {blog_structure.introduction}

Sections : {blog_structure.sections}

Conclusion : {blog_structure.conclusion}

References : {blog_structure.references}

Abstract : {blog_structure.abstract}

Make sure to keep the same structure and the same tone of the original blog.

Writing style: {preferences.writing_style}

Complexity: {preferences.complexity}
"""

# DEFINE THE FUNCTION TO GENERATE THE BLOG

def generate_blog(blog_structure: StructuredBlog) -> Blog:
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": generate_blog_system_prompt},
            {"role": "user", "content": f"Rewrite the blog please."}
        ]
    )

    return completion.choices[0].message.content

# GENERATE THE BLOG

blog = generate_blog(blog_structure)

# CREATE A FINAL FUNCTION TO PROCESSING :

def process_blog(preferences: Preferences) -> Blog:
    blog_structure = generate_blog_structure(preferences)
    blog = generate_blog(blog_structure)
    return blog

# PROCESS THE BLOG

blog = process_blog(preferences)
print(blog)

# TODO 

# todo : ADD A WEB SEARCH TO FIND THE MOST RELEVANT REFERENCES

# todo : ADD A FUNCTION TO CHECK THE QUALITY OF THE BLOG


# ?  ----------------------------------------------------------
# ?                 TRY YOURSELF : PRACTICES                                       
# ? ----------------------------------------------------------

"""
HOMEWORK ASSIGNMENT: STRUCTURED CONTENT GENERATION

Based on what you've learned about structured outputs and content generation, 
complete the following projects:

1. RECIPE GENERATOR:
   Create a structured recipe generator that takes user preferences for:
   - Cuisine type (Italian, Mexican, Asian, etc.)
   - Dietary restrictions (vegetarian, vegan, gluten-free, etc.)
   - Difficulty level (easy, medium, hard)
   - Available cooking time

   The output should be a structured recipe with:
   - Title
   - Ingredients list with measurements
   - Step-by-step instructions
   - Nutritional information
   - Cooking tips

 # ----------------------------------------------------------

2. TRAVEL ITINERARY PLANNER:
   Build a system that generates a travel itinerary based on:
   - Destination
   - Trip duration
   - Budget level (budget, moderate, luxury)
   - Traveler interests (history, food, adventure, relaxation)
   - Season of travel

   The output should include:
   - Daily schedule with activities
   - Recommended accommodations
   - Transportation options
   - Estimated costs
   - Packing suggestions

# ----------------------------------------------------------

3. EDUCATIONAL CONTENT CREATOR:
   Develop a system that creates educational content on any topic with:
   - Target age group/education level
   - Learning style preference
   - Content length
   - Media type (text-heavy, visual, interactive)

   The output should include:
   - Learning objectives
   - Main content sections
   - Practice exercises or quizzes
   - Additional resources for further learning

"""

# ? SEND ME YOUR SOLUTIONS VIA LINKEDIN 