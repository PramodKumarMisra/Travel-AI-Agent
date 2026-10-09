TRIP = {
    "dates": "2026-11-27 to 2026-12-05 (9 days recommended to include Rishikesh safely)",
    "travelers": 5,
    "start": "New Delhi",
    "budget_food_per_person_per_day_inr": 1000,
    "itinerary": [
        {"day":1,"date":"2026-11-27","route":"New Delhi → Kalka (planned Kalka Shatabdi 12011, 07:40–11:40) → Shimla/Sarahan","distance_km":220},
        {"day":2,"date":"2026-11-28","route":"Shimla/Sarahan → Nako → Tabo → Kaza","distance_km":290},
        {"day":3,"date":"2026-11-29","route":"Kaza → Key → Kibber → Chicham → Hikkim/Komic → Kaza","distance_km":80},
        {"day":4,"date":"2026-11-30","route":"Kaza → Tabo/Dhankar → Kaza","distance_km":200},
        {"day":5,"date":"2026-12-01","route":"Kaza → Kunzum → Chandratal (conditional only; use a safe alternative if closed)","distance_km":120,"conditional":True},
        {"day":6,"date":"2026-12-02","route":"Kaza/Spiti → Nako → Kalpa","distance_km":230},
        {"day":7,"date":"2026-12-03","route":"Kalpa → Shimla (or a safe overnight stop based on weather, road and driver assessment)","distance_km":250},
        {"day":8,"date":"2026-12-04","route":"Shimla → Rishikesh; check in and explore Triveni Ghat, Ram Jhula/Lakshman Jhula area and riverside viewpoints","distance_km":250},
        {"day":9,"date":"2026-12-05","route":"Morning Shivpuri river rafting if officially operating and conditions are safe; explore Rishikesh, then travel to Delhi or stay overnight if tired","distance_km":240,"conditional":True}
    ],
    "transport": "Private 9/12-seater Tempo Traveller from Kalka; winter-experienced driver, heater, spare tyre and snow chains when required. Do not force long mountain drives in poor weather.",
    "rafting": {
        "location": "Shivpuri, near Rishikesh",
        "planned_date": "2026-12-05",
        "status": "Conditional: winter rafting is generally in season, but river levels, weather and official permissions can change. Confirm with a currently authorized operator shortly before and on the day.",
        "safety": "Use an authorized operator; require a properly fitted life jacket, helmet, safety briefing and trained guide. Follow age/health restrictions and do not raft if the operator or authorities suspend trips."
    },
    "packing": ["thermals","down/winter jacket","waterproof shell","gloves","beanie","wool socks","sunglasses","sunscreen","lip balm","water bottle","power bank","personal medicines","sturdy winter footwear","quick-dry clothes and secure footwear for rafting"],
    "emergency": {"india": "112"},
    "hotels": {"night_1":"Shimla/Sarahan","nights_2_5":"Kaza or safe alternate","night_6":"Kalpa","night_7":"Shimla or safe overnight stop","night_8":"Rishikesh"},
}

def itinerary_text():
    return "\\n".join(
        f"Day {x['day']} ({x['date']}): {x['route']} — ~{x['distance_km']} km"
        + (" [CONDITIONAL — verify locally]" if x.get("conditional") else "")
        for x in TRIP["itinerary"]
    )
