import os
import qrcode

def generateQrCodeInLocal(unique_id):
# Create the 'qr_codes' directory if it doesn't exist
    if not os.path.exists("qr_codes"):
        os.makedirs("qr_codes")

    # Create a QR code for the unique ID
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(unique_id)
    qr.make(fit=True)

    # Save QR code image
    img = qr.make_image(fill='black', back_color='white')
    qr_image_path = f"qr_codes/{unique_id}.png"
    img.save(qr_image_path)
    print("QRCode crée!!!")
    return qr_image_path
