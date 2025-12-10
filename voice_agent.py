from retell import Retell
from dotenv import load_dotenv
import os

load_dotenv()

retell_client = Retell(
  api_key=os.getenv("RETELL_API_KEY")
)

from_number = '+13322448167'
to_number = '+919588078815'

def make_call(name, aqi_level, warning_message):
    try:
        response = retell_client.call.create_phone_call(
            from_number=from_number,
            to_number=to_number,
            retell_llm_dynamic_variables={
                "name": name,
                "aqi_level": aqi_level,
                "warning_message": warning_message
            }
        )
        print(f"Call initiated: {response}")
        return response
    except Exception as e:
        print(f"Error making call: {e}")
        raise

# Run the function
if __name__ == "__main__":
    make_call("John Cena", "400", "Air quality is hazardous. Please stay indoors.")