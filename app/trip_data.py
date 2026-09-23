TRIP = {
    "dates": "2026-11-27 to 2026-12-03",
    "travelers": 5,
    "start": "New Delhi",
    "budget_food_per_person_per_day_inr": 1000,
    "itinerary": [
        {"day":1,"date":"2026-11-27","route":"New Delhi → Kalka → Shimla/Sarahan","distance_km":220},
        {"day":2,"date":"2026-11-28","route":"Shimla/Sarahan → Nako → Tabo → Kaza","distance_km":290},
        {"day":3,"date":"2026-11-29","route":"Kaza → Key → Kibber → Chicham → Hikkim/Komic → Kaza","distance_km":80},
        {"day":4,"date":"2026-11-30","route":"Kaza → Tabo/Dhankar → Kaza","distance_km":200},
        {"day":5,"date":"2026-12-01","route":"Kaza → Kunzum → Chandratal → Kaza","distance_km":120,"conditional":True},
        {"day":6,"date":"2026-12-02","route":"Kaza/Spiti → Nako → Kalpa","distance_km":230},
        {"day":7,"date":"2026-12-03","route":"Kalpa → Shimla/Kalka → Delhi","distance_km":500},
    ],
    "transport": "Private 9/12-seater Tempo Traveller from Kalka; winter-experienced driver, heater, spare tyre and snow chains when required.",
    "packing": ["thermals","down/winter jacket","waterproof shell","gloves","beanie","wool socks","sunglasses","sunscreen","lip balm","water bottle","power bank","personal medicines","sturdy winter footwear"],
    "emergency": {"india": "112"},
    "hotels": {"night_1":"Shimla/Sarahan","nights_2_5":"Kaza or safe alternate","night_6":"Kalpa"},
}

def itinerary_text():
    return "\n".join(f"Day {x['day']} ({x['date']}): {x['route']} — ~{x['distance_km']} km" + (" [CONDITIONAL]" if x.get("conditional") else "") for x in TRIP["itinerary"])
