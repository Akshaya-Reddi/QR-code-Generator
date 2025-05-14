!pip install qrcode pillow 

import qrcode
website_link = 'https://www.youtube.com/watch?v=X4ChmlNNkeE&ab_channel=Lunaticladz'
qr = qrcode.QRCode(version = 1, box_size = 5, border = 5) 
#Creating an instance for qrcode, Since it's a Python library, we can call the package constructor to create a qrcode object, customized to our specifications.
qr.add_data(website_link)
qr.make()
img = qr.make_image(fill = 'black', back_color = 'white')
img.save('youtube_qr.png')

