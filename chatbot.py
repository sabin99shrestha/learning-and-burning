import requests
import os

from dotenv import load_dotenv
load_dotenv("api.env")  # Load environment variables from .env file
from openai import OpenAI
client = OpenAI(
    api_key=os.getenv("CHAT_BOT_API_KEY")
)
userinput=None
while userinput!="exit":
        userinput=input("Enter your query:  ")

        response=client.responses.create(
        model="gpt-5.4-mini",
        input = userinput,
        store=True,

        )
        print("\n"+response.output_text + "\n")
