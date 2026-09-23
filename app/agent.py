import os
from datetime import date
import httpx
from .trip_data import TRIP, itinerary_text

SYSTEM = """You are SpitiTrip AI, a cautious travel assistant for a 5-person Spiti Valley trip from 27 Nov 2026 to 3 Dec 2026.
Never claim live road, weather, hotel, price, or permit information unless a live tool/source supplied it.
Chandratal on 1 Dec 2026 is CONDITIONAL: late-November/early-December access depends on weather, snow and Kunzum/road conditions. Never guarantee access.
Use the supplied itinerary as the planned baseline and clearly label assumptions.
Emergency India number: 112.
"""

async def live_weather(city="Kaza"):
    coords={"Kaza":(32.2269,78.0719),"Shimla":(31.1048,77.1734),"Kalpa":(31.5397,78.2556)}
    lat,lon=coords.get(city,coords["Kaza"])
    url="https://api.open-meteo.com/v1/forecast"
    params={"latitude":lat,"longitude":lon,"current":"temperature_2m,wind_speed_10m","timezone":"Asia/Kolkata"}
    try:
        async with httpx.AsyncClient(timeout=8) as client:
            r=await client.get(url,params=params); r.raise_for_status()
            d=r.json()
            c=d.get("current",{})
            return {"city":city,"temperature_c":c.get("temperature_2m"),"wind_kmh":c.get("wind_speed_10m"),"source":"Open-Meteo"}
    except Exception:
        return {"city":city,"error":"Live weather unavailable"}

async def answer(message:str):
    lower=message.lower()
    if "weather" in lower:
        city="Kaza" if "kaza" in lower else ("Shimla" if "shimla" in lower else ("Kalpa" if "kalpa" in lower else "Kaza"))
        return {"reply":f"Current weather check for {city}: {await live_weather(city)}","live":True}
    if "chandratal" in lower or "kunzum" in lower:
        return {"reply":"Chandratal is conditional for this trip. The planned date is 1 Dec 2026, but access depends on actual snow, Kunzum/road conditions and local authority/operator guidance. Do not treat the itinerary as a guarantee.","live":False}
    if "itinerary" in lower or "plan" in lower or "route" in lower:
        return {"reply":itinerary_text(),"live":False}
    if "pack" in lower:
        return {"reply":"Packing: "+", ".join(TRIP["packing"])+".","live":False}
    if "emergency" in lower:
        return {"reply":"India emergency number: 112. For mountain travel, also follow local police/administration and driver/operator instructions.","live":False}
    key=os.getenv("OPENAI_API_KEY")
    if key:
        try:
            from openai import AsyncOpenAI
            client=AsyncOpenAI(api_key=key)
            resp=await client.responses.create(model=os.getenv("OPENAI_MODEL","gpt-5-mini"),input=[{"role":"system","content":SYSTEM},{"role":"user","content":message}])
            return {"reply":resp.output_text,"live":False}
        except Exception:
            pass
    return {"reply":"I can help with the Spiti itinerary, Chandratal safety, packing, emergency information, and live weather. Try: 'show itinerary', 'Chandratal status', or 'weather in Kaza'.","live":False}
