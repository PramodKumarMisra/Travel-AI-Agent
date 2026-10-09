from .trip_data import TRIP, itinerary_text

async def live_weather(city="Kaza"):
    return {"city": city, "error": "Live weather lookup temporarily unavailable"}

async def answer(message: str):
    lower = message.lower()
    if "rafting" in lower or "shivpuri" in lower or "rishikesh" in lower:
        return {"reply": "Rishikesh is planned for 4 Dec 2026 and Shivpuri rafting for 5 Dec. Raft only if authorities and an authorized operator confirm safe conditions that day. Use a fitted life jacket, helmet, safety briefing and trained guide.", "live": False}
    if "weather" in lower:
        return {"reply": await live_weather(), "live": False}
    if "chandratal" in lower or "kunzum" in lower:
        return {"reply": "Chandratal is conditional for 1 Dec 2026. Access depends on snow, road conditions and local guidance.", "live": False}
    if "itinerary" in lower or "plan" in lower or "route" in lower:
        return {"reply": itinerary_text(), "live": False}
    if "pack" in lower:
        return {"reply": "Packing: " + ", ".join(TRIP["packing"]), "live": False}
    if "emergency" in lower:
        return {"reply": "India emergency number: 112.", "live": False}
    return {"reply": "Ask for itinerary, Rishikesh rafting, Chandratal safety, packing, emergency information or weather.", "live": False}
