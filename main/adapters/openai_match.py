from main.ports.matcher import Matcher
import os
import openai
from dotenv import load_dotenv, find_dotenv




class OpenAiMatch(Matcher):

    MATCH_ERROR_MSG = "Error matching: "

    def __init__(self):
        #super().__init__()
        _ = load_dotenv(find_dotenv())
        openai.api_key=os.getenv("OPENAI_API_KEY")
        self.model_selected = "gpt-3.5-turbo-0613"

    def match_candidate(self, candidate , role):
        try:
            user_prompt = f" Este es un diccionario con los requisitos del puesto { role }, genera un diccionario de pyhton en formato string con las mismas llaves que el anterior, pero que en cada llave tenga un porcentaje del 0 al 100 como valor, que indique en que medida el candidato cumple dicho requisito (en formato por ejemplo '0%','75%','100%', etc). Para el porcentaje de cumplimineto de cada requisito, considera toda la información que hay del candidato, el cumplimiento no debe ser textual, sino de forma general. Agregale además una llave en la primera posición al diccionario que se llame 'Nombre' y que contenga el nombre del candidato. La información que hay del candidato es: { candidate } "
            completion = openai.ChatCompletion.create(
                model=self.model_selected,
                messages=[{"role": "user", "content": user_prompt}],
                temperature=0
            )

            output = completion.choices[0].message["content"]

            return output
        except Exception as e:
            print(e.__dict__)