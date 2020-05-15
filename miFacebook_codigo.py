

import qrcode

img = qrcode.make("https://www.facebook.com/jotasELmaja")
f = open("Facebook_jotas.png", "wb")
img.save(f)
f.close()

