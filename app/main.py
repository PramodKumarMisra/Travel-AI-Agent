from fastapi import FastAPI, Header, HTTPException, Query
from pydantic import BaseModel
from .agent import answer
from .trip_data import TRIP, itinerary_text
from .store import add_expense, expenses, set_hotel, hotels, set_vehicle, vehicle, db_status
from .whatsapp import send_whatsapp

app = FastAPI(title="Spiti Travel AI Agent", version="0.2.0")

class ChatRequest(BaseModel):
    message: str

class ExpenseRequest(BaseModel):
    amount: float
    category: str
    note: str = ""
    paid_by: str = ""

class HotelRequest(BaseModel):
    night: str
    hotel: str

class VehicleRequest(BaseModel):
    provider: str
    vehicle: str
    driver: str = ""
    phone: str = ""

@app.get("/")
def root():
    return {"service":"Spiti Travel AI Agent","status":"online","docs":"/docs","health":"/health"}

@app.get("/health")
def health():
    return {"status":"ok","service":"Spiti Travel AI Agent","version":"0.2.0","storage":db_status()}

@app.get("/trip")
def trip(): return TRIP

@app.get("/itinerary")
def itinerary(): return {"itinerary":TRIP["itinerary"],"text":itinerary_text()}

@app.post("/chat")
async def chat(req: ChatRequest):
    return await answer(req.message)

@app.get("/weather")
async def weather(city: str = Query("Kaza")):
    from .agent import live_weather
    return await live_weather(city)

@app.get("/packing")
def packing(): return {"packing":TRIP["packing"]}

@app.get("/emergency")
def emergency(): return TRIP["emergency"]

@app.post("/expenses")
def create_expense(req: ExpenseRequest): return add_expense(req.model_dump())

@app.get("/expenses")
def get_expenses(): return {"expenses":expenses(),"total_inr":sum(x["amount"] for x in expenses())}

@app.put("/hotel")
def put_hotel(req: HotelRequest): return set_hotel(req.night,req.hotel)

@app.get("/hotel")
def get_hotels(): return hotels()

@app.put("/vehicle")
def put_vehicle(req: VehicleRequest): return set_vehicle(req.model_dump())

@app.get("/vehicle")
def get_vehicle(): return vehicle()

@app.get("/whatsapp/webhook")
def whatsapp_verify(hub_mode: str = Query(None, alias="hub.mode"), hub_challenge: str = Query(None, alias="hub.challenge"), hub_verify_token: str = Query(None, alias="hub.verify_token")):
    import os
    if hub_mode == "subscribe" and hub_verify_token == os.getenv("WHATSAPP_VERIFY_TOKEN"):
        return int(hub_challenge)
    raise HTTPException(status_code=403, detail="verification failed")

@app.post("/whatsapp/webhook")
async def whatsapp_webhook(payload: dict):
    messages=[]
    for entry in payload.get("entry",[]):
        for change in entry.get("changes",[]):
            for msg in change.get("value",{}).get("messages",[]):
                if msg.get("type")=="text":
                    messages.append({"from":msg.get("from"),"text":msg.get("text",{}).get("body","")})
    for m in messages:
        result=await answer(m["text"])
        await send_whatsapp(m["from"],result["reply"])
    return {"ok":True,"processed":len(messages)}

@app.post("/admin/send-morning-briefing")
async def morning_briefing(x_briefing_secret: str = Header(default="")):
    import os
    if x_briefing_secret != os.getenv("BRIEFING_SECRET",""):
        raise HTTPException(status_code=403, detail="invalid briefing secret")
    result=await answer("Show itinerary and current weather in Kaza. Include the Chandratal conditional warning.")
    return result
