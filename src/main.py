import os
from ticket import creeTicket, utiliseTicket
from machine import getIdMachine
from function import generateQrCodeInLocal

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get host and port from the .env file

if __name__ == "__main__":

    # Infos machine
    machine_designation = os.getenv('MACHINE_DESIGNATION')
    machine_lieu = os.getenv('MACHINE_LIEU')
    machine_infos = {
        "designation": machine_designation,
        "lieu": machine_lieu
    }
    id_machine = getIdMachine(machine_infos).get('id_machine_recolte')

    # gains obtenu
    gains = {
        "montant": 20
    }

    # Create the ticket and return the id of ticket
    id_ticket = creeTicket(id_machine,gains).get('id_ticket')

    # Generate the Qr Code
    generateQrCodeInLocal(id_ticket)
