import qrcode

# Enter the data you want to encode in the barcode
data = "This is a barcode"

# Create a QRCode object
qr = qrcode.QRCode(version=1, error_correction=qrcode.ERROR_CORRECT_L, box_size=10, border=5)

# Encode the data in the QRCode object
qr.add_data(data)

# Generate the barcode image
img = qr.make_image()

# Save the barcode image
img.save("barcode.png")