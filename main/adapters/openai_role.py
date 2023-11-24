
import os
import openai
from main.ports.role import Role
from dotenv import load_dotenv, find_dotenv




class OpenAiRole(Role):
    

    def __init__(self):
        _ = load_dotenv(find_dotenv())
        openai.api_key=os.getenv("OPENAI_API_KEY")
        self.model_selected = "gpt-3.5-turbo-1106"

    def parse_role(self, raw_role):
        
        user_prompt = f"A partir de este texo: { raw_role }, genera un diccionario de pyhton en formato Json object que repsesente los requisitos para el puesto de trabajo. Que cada llave sea el nombre de un requisito ( una palabra que capture lo escencial del requisito) y el valor la descripcion del requisito que indique los requisistos correspondientes que se requieren. Que la primera llave sea 'Cargo' y tenga como valor el nombre del cargo. MUY IMPORTANTE: Retorna solo el diccionario (Json object) en formato string , sin nada de texto extra, por ejemplo: {{'Cargo': 'Nombre del cargo', 'Estudios': 'Ser titular de una licenciatura en Ciencias de la Computación o un campo relacionado', 'Experiencia': 'Tener mas de 5 años de experiencia en desarrollo de software', ...}} "
        completion = openai.ChatCompletion.create(
            model=self.model_selected,
            response_format={ "type": "json_object" },
            messages=[{"role": "system", "content": "Eres un asistente diseñado para retornar un JSON object en español"}, 
            {"role": "user", "content": user_prompt}],
            temperature=0
        )

        output = completion.choices[0].message["content"]

        return output
