
import network  #import des fonction lier au wifi
import urequests #import des fonction lier au requetes http
import utime #import des fonction lier au temps
import ujson #import des fonction lier aà la convertion en Json

wlan = network.WLAN(network.STA_IF) # met la raspi en mode client wifi
wlan.active(True) # active le mode client wifi


ssid = 'IIM_Private'
password = 'Creatvive_Lab_2023'
wlan.connect(ssid, password) # connecte la raspi au réseau
url = "https://api.meteo-concept.com/api/forecast/daily/0?insee=92050&token=2adec8ce3ebf940275d6a0ebb57dd75069b41231e886f7d20f9ee3489ece08ce"
while not wlan.isconnected():
     pass

temperature = ''


from machine import Pin # importe dans le code la lib qui permet de gerer les Pin de sortie et d'entré
 
  
led1 = Pin(17, mode=Pin.OUT) # declaration d'une variable de type pin ici la 17
  
led2 = Pin(13, mode=Pin.OUT) # declaration d'une variable de type pin ici la 17 
pin_button = Pin(18, mode=Pin.IN, pull=Pin.PULL_UP) # declaration d'une variable de type pin ici la 14
                                                     #et on prescise que c'est une pine d'entré de courant (IN)

temper = 14
while True: # boucle infini     
    try:
         print("GET")
         r = urequests.get(url) # lance une requete sur l'url
         print(r.json()["forecast"]["tmax"]) # traite sa reponse en Json
         temperature = r.json()["forecast"]["tmax"]
         r.close() # ferme la demande 
    except Exception as e:
         print(e)
         
         
         print(pin_button.value()) # on envoie la valeur du bouton
    utime.sleep(.1)            # on attend 0.1 seconde
    if pin_button.value() == 0 and temper >= temperature:
        led1.on()
        led2.off()
    elif pin_button.value() == 0 and temper < temperature:
        led2.on()
        led1.off()
    else:
        led2.off()
        led1.off()
             
        
                 
    

        
        


