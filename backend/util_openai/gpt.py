# %%
import openai
from dotenv import load_dotenv
import os
from utils.logger import Log

load_dotenv()

# %%
class OpenAIUtil:
    def __init__(self) -> None:
        openai.api_key = os.environ.get('OPEN_AI_API_KEY')

    
    def answer_questions_for_transcribed_text(self, transcription: str, questions: str) -> str:
        
        Log().i(transcription)
        Log().i(questions)

        completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", 
                messages = [
                    {'role': 'user', 'content': transcription},
                    {'role': 'user', 'content': questions}
                ],
                temperature = 0.70
            )

        return completion.choices[0].message.content

# %%
# OpenAI().answer_questions_for_transcribed_text("Test", "some question")
# %%
