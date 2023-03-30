import openai
from dotenv import load_dotenv
import os

load_dotenv()

class OpenAI:
    def __init__(self) -> None:
        openai.api_key = os.environ.get('OPEN_AI_API_KEY')

    
    def answer_questions_for_transcribed_text(self, transcription: str, questions: str) -> str:

        completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", 
                messages = [
                    {'role': 'user', 'content': transcription},
                    {'role': 'user', 'content': questions}
                ],
                temperature = 0.75
            )

        print(completion.choices[0].message.content)
        return completion.choices[0].message.content

