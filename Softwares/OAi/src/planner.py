#This code will also have definations and meaning of steps for better understanding
import os
from groq import Groq
from dotenv import load_dotenv
import json

load_dotenv()

"""imports groq and json files"""

class Planner:
    def __init__(self):
        #initialize groq 
        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError("GROQ_API_KEY not found in environment variables")
        
        self.client = Groq(api_key=api_key)

    """initializes the planner class with an API key for Groq"""

    def generate_plan(self, normalized_command, context):
        prompt = f"""
You are an Ai desktop Assistant automation planner.

Your works include:
- Break the user command into clear steps 
- Use only valid actions
- Output strictly in JSON format

Allowed actions you can perform:
- open_browser
- type_text
- press_key
- click_elements

Return format:
{{
    "plan": [
    {{"action": "...","parameters": {{...}}}}
    ]
}}

User command:
{normalized_command}

Context:
{context}
"""
        """this is the prompt for the ai to perform the task and before prompt 
        we have taken the input from normalizer and also imported the context"""
        
        response = self.client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "you are a structured planner."},
                {"role": "user", "content": prompt}
            ]
        )

        """this calls the ai and chooses model and gives output"""

        plan_text = response.choices[0].message.content

        # debug output
        print("\n[RAW AI OUTPUT]:", plan_text)

        # clean + parse JSON safely
        try:
            start = plan_text.find("{")
            end = plan_text.rfind("}") + 1
            clean_json = plan_text[start:end]

            return json.loads(clean_json)

        except Exception as e:
            print("JSON error:", e)
            return {"plan": []}

        """output string is taken and cleaned then converted to json"""

# print(os.getenv("GROQ_API_KEY"))