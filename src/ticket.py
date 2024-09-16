import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get host and port from the .env file
api_host = os.getenv('IP_ADDRESS_BACKEND_EXPRESS')
api_port = os.getenv('PORT_BACKEND_EXPRESS')

# Construct the API URL dynamically
# url_cree = f'http://{api_host}:{api_port}/ticket/:id_machine_recolte'
# url_utilise = f'http://{api_host}:{api_port}/ticket/utilise/:id_ticket'


# Function to make a POST request to create a ticket
def creeTicket(id_machine_recolte, payload, timeout=5):
    try:
        # Construct the dynamic URL with the provided id_machine_recolte
        url_cree = f'http://{api_host}:{api_port}/ticket/{id_machine_recolte}'

        # Make the POST request to the API with the given payload
        response = requests.post(url_cree, json=payload, timeout=timeout)

        # Check if the request was successful
        if response.status_code == 200:
            print("Ticket créée avec succès !")
            return response.json()  # Return the JSON response if needed
        else:
            print(f"Échec de la création de la ressource : {response.status_code}")
            return None

    except requests.exceptions.Timeout:
        print("La requête a expiré. Veuillez réessayer plus tard.")
        return None

    except requests.exceptions.ConnectionError:
        print("Erreur de connexion. Veuillez vérifier si le serveur est en cours d'exécution.")
        return None

    except requests.exceptions.HTTPError as http_err:
        print(f"Erreur HTTP : {http_err}")
        return None

    except requests.exceptions.RequestException as err:
        print(f"Une erreur est survenue : {err}")
        return None

# Function to make a GET request
def utiliseTicket(id_ticket,timeout=5):
    try:
        # Send GET request to the API
        url_utilise = f'http://{api_host}:{api_port}/ticket/utilise/{id_ticket}'
        
        response = requests.get(url_utilise, timeout=timeout)
        
        # Check if the request was successful
        response.raise_for_status()  # Will raise an error for bad status codes
        
        # Parse the JSON response data
        data = response.json()
        print("Données récupérées depuis l'API :")
        print(data)
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