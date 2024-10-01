import os
import qrcode
import urllib.parse

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get host and port from the .env file
api_host = os.getenv('IP_ADDRESS_BACKEND_EXPRESS')
api_port = os.getenv('PORT_BACKEND_EXPRESS')

def generateQrCodeTicketInLocal(id_ticket):
    # Create the 'qr_codes' directory if it doesn't exist
    if not os.path.exists("qr_codes"):
        os.makedirs("qr_codes")

    # Check if environment variables are loaded correctly
    if not api_host or not api_port:
        raise ValueError("API host or port not set in environment variables")

    # Define the URL template
    # url_template = f'http://{api_host}:{api_port}/ticket/{id_ticket}'
    url_template = f'http://{api_host}/ticket/{id_ticket}'

    
    # Encode the URL
    encoded_url = urllib.parse.quote(url_template, safe='')

    # Create a QR code for the encoded URL
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(encoded_url)
    qr.make(fit=True)

    # Save QR code image
    img = qr.make_image(fill='black', back_color='white')
    qr_image_path = f"qr_codes/{id_ticket}.png"
    img.save(qr_image_path)
    print("QRCode créé !!!")
    return qr_image_path