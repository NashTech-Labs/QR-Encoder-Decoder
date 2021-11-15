import cv2
# Create The Decoder
decoder = cv2.QRCodeDetector()
# Load Your Data
file_name = "QR.png"
image = cv2.imread(file_name)
# Decode and Print the required information
link, data_points, straight_qrcode = decoder.detectAndDecode(image)
print(link)
