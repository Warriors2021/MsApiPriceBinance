import requests
import pandas as pd
from datetime import datetime
import os
import dotenv
import time
from ConexionMongo import conexion_mongo

instancia = conexion_mongo()


dotenv.load_dotenv()




def searchData(moneda:str):

    url = f"https://api.cryptowat.ch/markets/binance/{moneda}/ohlc?apikey={os.getenv('APIKEY')}"

    dia = '300'


    response = requests.get(url, params={"periods": dia})  # conexion a la api y rescatado de datos
    data = response.json()  # Convirtiendo los datos en json



    data = data["result"][dia]  # accediendo a la lista do
    items = ['CloseTime', 'OpenPrice', 'HighPrice', 'LowPrice', 'ClosePrice', 'Volume_BTC', 'VolumeUSD']
    lista = []

    y = 0
    x = 0

    for y in range(len(data)):
        diccionario = {}

        for x in range(len(items)):
            diccionario[items[x]] = data[y][x]

            lista.append(diccionario)


    df = pd.DataFrame(lista)



    listaFechas = []
    listaHoras=[]
    data = df.CloseTime




    for dato in data:
        
        informacion = str(datetime.fromtimestamp(dato))
        informacion = informacion.split()        
        listaFechas.append(informacion[0])
        listaHoras.append(informacion[1])


    hours = []
    minutes= []
    

    for dato in listaHoras:

        datos = dato.split(":")

        hours.append(datos[0])
        minutes.append(datos[1])





    df["Date"] = listaFechas
    df["Hour"] = hours
    df["Minute"] = minutes


    dft = df[["Date","Hour","Minute","OpenPrice",'HighPrice', 'LowPrice', 'ClosePrice']]

    dft = dft.tail(1)

    dft = dft.to_dict("records")

    return dft






def subirDatos():

    
    lista = os.getenv("MONEDAS")
    lista =lista.split(",")
 
    
    num = ["00","05","10","15","20","25","30","35","40","45","50","55"]


    while True:

        date = datetime.now()

        minute = date.time()

        date = str(datetime.now().date()).split("-")

        date = f"{date[0]}_{date[1]}_{date[2]}"

        minute = str(minute).split(":")

        minute = minute[1]

        for data in num:

            time.sleep(1)

            if minute == data:

                for moneda in lista:

                    datos = data = searchData(moneda=moneda)
                    instancia.collection(f"Datos{moneda.upper()}_{date}").insert_many(datos)
                    print(f"datos subidos para la moneda {moneda}")

                time.sleep(60)
            
            else:
                pass



if __name__ == "__main__":

    subirDatos()