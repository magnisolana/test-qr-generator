import qrcode
import json
import test_intents

# Function to generate a QR code from JSON intent data for parsing using signer app
def generate_qr_code_from_json(json_input):
    json_str = json.dumps(json_input)
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(json_str)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.show()

if __name__ == "__main__":
    generate_qr_code_from_json(test_intents.transfer)
