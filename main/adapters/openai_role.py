
import os
import openai
from dotenv import load_dotenv, find_dotenv




class OpenAiRole():
    MATCH_ERROR_MSG = "Error matching: "

    def __init__(self):
        _ = load_dotenv(find_dotenv())
        openai.api_key=os.getenv("OPENAI_API_KEY")
        self.model_selected = "gpt-3.5-turbo-0613"

    def parse_role(self, raw_role):
        try:
            user_prompt = f"A partir de este texo: { raw_role }, genera un diccionario de pyhton en formato string que repsesente los requisitos para el puesto de trabajo. Con cada item que encuentres y una descripcion que indique los requisitos del item."
            completion = openai.ChatCompletion.create(
                model=self.model_selected,
                messages=[{"role": "user", "content": user_prompt}],
                temperature=0
            )

            output = completion.choices[0].message["content"]

            return output
        except Exception as e:
            print(e.__dict__)