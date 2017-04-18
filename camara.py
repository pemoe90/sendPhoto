import os
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from picamera import PiCamera
from time import sleep
import time
import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 
from email.MIMEBase import MIMEBase 
from email import encoders


ruta = os.getcwd()
ImgFileName = time.strftime('%c')
def setRuta():
	global ruta
	ruta = ruta + '/' + ImgFileName + '.jpg'

def tomarFoto():	
	camera = PiCamera()
	camera.rotation = 180
	camera.capture(ruta)
	print('Foto tomada')
	
	
def enviarCorreo():
	
	email_to = '' #poner direccion del destinatario
	email_from = '' #poner direccion desde donde se envia
	email_pass = '' #poner contraseña del email_from
	img_data = open(ruta, 'rb').read()
	msg = MIMEMultipart()
	msg['Subject'] = 'Ladron'
	msg['From'] = email_to
	msg['To'] = email_from 

	text = MIMEText("Ladron")
	msg.attach(text)
	image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
	msg.attach(image)

	s = smtplib.SMTP('smtp.gmail.com', 587) #configurado para usar gmail
	s.ehlo()
	s.starttls()
	s.ehlo()
	s.login(email_from , email_pass)
	s.sendmail(email_from , email_to, msg.as_string())
	s.quit()
	print("Foto enviada")

if __name__ == '__main__':
	setRuta()
	tomarFoto()
	enviarCorreo()
