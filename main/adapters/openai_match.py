from main.ports.matcher import Matcher
import os
import openai
from dotenv import load_dotenv, find_dotenv




class OpenAiMatch(Matcher):

    def __init__(self):
        _ = load_dotenv(find_dotenv())
        openai.api_key=os.getenv("OPENAI_API_KEY")
        self.model_selected = "gpt-3.5-turbo-1106"

    def match_candidate(self, candidate , role):
        user_prompt = f" Debes evaluar a un candidato para un cargo según algunos requisitos. Este es un diccionario (Json object) con los requisitos del cargo { role }. Genera un diccionario de pyhton en formato Json  object con las mismas llaves que el anterior, pero que cada llave tenga como valor un porcentaje en formato string ('0%', '25%', '50%', '75%' o '100%') que indique el grado de cumplimiento del requisito (por parte del candidato) considerando toda la información del candidato (que adjuntaré al final del mensaje). Además, remplaza la primera llave 'Cargo', por otra llave en la primera posición que se llame 'Data' y que contenga como valor otro diccionario en formato string como llaves 'Cargo' y 'Nombre'  y con valores: el nombre del cargo que está en el diccionario que puse al comienzo y el nombre del candidato que esta en la información del candidato que pondré ahora. La información que hay del candidato es: { candidate }. Retorna solo el diccionario (Json object) en formato string, sin texto extra, por ejemplo: {{'Data': {{'Cargo': 'Nombre del cargo', 'Nombre': 'Nombre del candidato'}}, 'Requisito 1': '75%',...}}"
        completion = openai.ChatCompletion.create(
            model=self.model_selected,
            response_format={ "type": "json_object" },
            messages=[{"role": "system", "content": "Eres un asistente dineñado para retornar un JSON object en español"},
            {"role": "user", "content": user_prompt}],
            temperature=0
        )

        output = completion.choices[0].message["content"]

        return output