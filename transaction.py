from sanic import Sanic
from sanic.response import HTTPResponse,JSONResponse
import random
import json

TR_DATA = open('1000_random_transaction_data.json')

TR_JSON = json.load(TR_DATA)


app = Sanic("PINE_LAB")

@app.get("/")
async def Home(request=None):
  r_tr = [random.choice(TR_JSON) for _ in range(10)]
  links = [
      f"""<br/><a href="/TID/{tr['Transaction_ID']}" target='_blank'>Transaction ID {tr['Transaction_ID']}</a>"""
      for tr in r_tr
  ]
  return HTTPResponse("""
    <h1>Welcome to PINE-LAB Home</h1>
    <h2>To get Tranasction Details Details : /TID/Transaction_ID</h2>
    <p> Please find below some sample Transaction API Calls
    """+"".join(links))

@app.get("/TID/<Transaction_ID:str>")
async def getTransactionStatus(request=None, Transaction_ID=None):
    t_rsp = {
        "Transactio_id":Transaction_ID,
        "Status":"NA",
        "Amount":"NA",
        "Name":"NA",
        "gender":"NA",
        "ip_address":"NA"
        }
    for tr in TR_JSON:
      if Transaction_ID == tr['Transaction_ID']:
        t_rsp = tr
    
    return JSONResponse(t_rsp)