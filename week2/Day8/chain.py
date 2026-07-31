import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from time import sleep

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

client = Groq(api_key=my_api_key)

my_model = "llama-3.3-70b-versatile"


JD="""
We are hiring a Backend Python Developer.

Requirements:
- Strong Python
- FastAPI or Django
- PostgreSQL
- Docker
- AWS
- REST APIs
- 2+ years of experience
"""

RESUME="""
Name: Rahul Sharma

Experience:
3 years as a Software Developer.

Skills:
Python, FastAPI, MySQL, Docker,
REST APIs, Git

Projects:
Built a food delivery backend using
FastAPI and MySQL.

Deployed applications using Docker.
"""

def ask_llm(system_prompt, user_prompt):
    message_system = {
        "role": "system",
        "content": system_prompt
    }

    my_message = {
        "role": "user",
        "content": user_prompt
    }

    my_messages = [message_system, my_message]

    response = client.chat.completions.create(
        model=my_model,
        messages=my_messages,
        temperature=0
    )

    answer = response.choices[0].message.content

    return answer

#step 1: Resume Extract
def extract_resume_info():
    # extract skills from resume
    print("Extracting skills from resume...")
    system_prompt = """
    You are a professional HR assistant. Extract the skills from the candidates resume provided. 
    Only return the skills no other information. Do not invent any skillsby yourself.
    Output Format:
    Skills should be separated by commas. Just return comma separated skills do not return any other filler information
    """
    user_prompt=f"""
    Extract the skills from this resume
    {RESUME}
    """
    return ask_llm(system_prompt, user_prompt)

#step 2 JD Extract
def extract_jd_info():
    # extract skills from JD
    print("Extracting skills from JD...")
    system_prompt = """
    You are a professional HR assistant. Extract the skills from the job description provided. 
    Only return the skills no other information. Do not invent any skillsby yourself.
    """
    user_prompt=f"""
    Extract the skills from this job description
    {JD}
    """
    return ask_llm(system_prompt, user_prompt)

#step 3: Match Skills
def match_skills(resume_skills, jd_skills):
    # match skills
    print("Matching skills...")
    system_prompt="""
    You are a professional HR assistant. compare the skills of candidate and the skills required in the JD and produce a final score between
    1 and 100. also produce a short verdict whther the candidate is a good fit for the role.
    """
    user_prompt=f"""
    Compare and match the skills
    JD:
    {jd}
    Candidate:
    {candidate}
    """
    return ask_llm(system_prompt, user_prompt)

candidate=extract_resume_info()
print("Candidate Skills:", candidate)
sleep(2)
jd=extract_jd_info()
print("JD Skills:", jd)
sleep(2)
score=match_skills(candidate, jd)
print(score)

