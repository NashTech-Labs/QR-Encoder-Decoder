# import modules
import qrcode
from PIL import Image
  
# taking image which user wants 
# in the QR code center
Logo_link = 'knoldus.png'
  
logo = Image.open(Logo_link)
  
# taking base width
basewidth = 100
  
# adjust image size
wpercent = (basewidth/float(logo.size[0]))
hsize = int((float(logo.size[1])*float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
QRcode = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=15,
    border=4,
)
  
# taking url or text
value = input("Please enter some data as string:\n")
#url = 'https://www.knoldus.com/home'
  
# addingg URL or text to QRcode
QRcode.add_data(value)
  
# generating QR code
QRcode.make()
  
# taking color name from user
QRcolor = 'Orange'
  
# adding color to QR code
QRimg = QRcode.make_image(
    fill_color=QRcolor, back_color="white").convert('RGB')
  
# set size of QR code
pos = ((QRimg.size[0] - logo.size[0]) // 2,
       (QRimg.size[1] - logo.size[1]) // 2)
QRimg.paste(logo, pos)
  
# save the QR code generated
QRimg.save('QR.png')
  
print('QR code generated!')




