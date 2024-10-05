#Se va a encargar de montar el servidor
#flask(Minusculas) es la libreria y Flask(Mayuscula) es módulo 
from flask import Flask  #nos permite craer el servisdor
from flask_restful import Api #Nos permite crear la funcionalidad de api

#Creamos un función que configure el servidor 
def configurar_app():
#Va a almacenar el servidor
  app = Flask(__name__)
#Varible que va almacenas la Api
#Le indicamos sobre que servidor va a interactuiar 
api = Api(app) 

return app