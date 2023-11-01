
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
            user_prompt = f"A partir de este texo: { raw_role }, genera un diccionario de pyhton en formato string que repsesente los requisitos para el puesto de trabajo. Que cada llave sea el nombre de un requisito ( una palabra que capture lo escencial del requisito) y el valor la descripcion del requisito que indique los requisistos correspondientes que se requieren. Que la primera llave sea 'Cargo' y tenga como valor el nombre del cargo. Retorna solo el diccionario en formato string, sin texto extra, por ejemplo {{'Cargo': 'Nombre del cargo', 'Estudios': 'Ser titular de una licenciatura en Ciencias de la Computación o un campo relacionado',...}}"
            completion = openai.ChatCompletion.create(
                model=self.model_selected,
                messages=[{"role": "user", "content": user_prompt}],
                temperature=0
            )

            output = completion.choices[0].message["content"]

            return output
        except Exception as e:
            print(e.__dict__)