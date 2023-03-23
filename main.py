from fastapi import FastAPI
from ConexionMongo import conexion_mongo
import subprocess
import uvicorn


app = FastAPI()



@app.get("/{criptomoneda}/{date}/{time}")
async def read_root(criptomoneda:str="BTC",date:str="",time:str=""):


    instance = conexion_mongo()

    collection = instance.collection(f"Datos{criptomoneda.upper()}_{date}")


    if time == "5":

        resultados = collection.find({"Minute": {"$in": ["05","10","15","20","25","30","35","40","45","50","55","00"]}},{"_id":0})

    elif time == "10":

        resultados = collection.find({"Minute": {"$in": ["10","20","30","40","50","00"]}},{"_id":0})
    
    elif time == "15":

        resultados = collection.find({"Minute": {"$in": ["15","30","45","00"]}},{"_id":0})
    
    elif time == "30":

        resultados = collection.find({"Minute": {"$in": ["30","00"]}},{"_id":0})
    
    elif time == "hour":

        resultados = collection.find({"Minute": {"$in": ["00"]}},{"_id":0})

    else:

        pass
        


    book = []


    for data in resultados:

        book.append(data)



    return {"date":book}



if __name__ == "__main__":

    subprocess.Popen(["python","ConexionAPICriptowath.py"])

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)
