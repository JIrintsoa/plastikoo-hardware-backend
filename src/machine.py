import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get host and port from the .env file
api_host = os.getenv('IP_ADDRESS_BACKEND_EXPRESS')
api_port = os.getenv('PORT_BACKEND_EXPRESS')

# Function to make a GET request
def getIdMachine(payloads,timeout=5):
    try:
        # Send GET request to the API
        url = f'http://{api_host}:{api_port}/machine'
        
        response = requests.post(url, json=payloads ,timeout=timeout)
        
        # Check if the request was successful
        response.raise_for_status()  # Will raise an error for bad status codes
        
        # Parse the JSON response data
        data = response.json()
        # print("Données récupérées depuis l'API :")
        # print(data)
        return data
        
    except requests.exceptions.ConnectionError:
        print("Erreur de connexion. Veuillez vérifier si le serveur est en cours d'exécution.")
        return None

    except requests.exceptions.HTTPError as http_err:
        print(f"Erreur HTTP : {http_err}")
        return None

    except requests.exceptions.RequestException as err:
        print(f"Une erreur est survenue : {err}")
        return None