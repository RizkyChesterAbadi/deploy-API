#Import Package
from fastapi import FastAPI , Request, Header, HTTPException

import pandas as pd

#membuat object FastAPI dan simpan ke variable app
app = FastAPI()



API_KEY = "secret123"


#  membuat alamat utama / home endpoint. alamatnya adalah /
# www.namadomain.com --> / 
@app.get('/')
def gethome():
    return 'Hello World'


# Membuat Headers
@app.get('/see-headers')
def readHeader(request : Request):
    # Mengambil headers dari Request
    headers = request.headers

    # informasi credential --> password, id ,
