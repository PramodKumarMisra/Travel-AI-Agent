import os
from typing import Any

_memory={"expenses":[],"hotels":{},"vehicle":{}}

def _db():
    return os.getenv("DATABASE_URL")

def add_expense(item:dict[str,Any]):
    _memory["expenses"].append(item); return item

def expenses(): return _memory["expenses"]

def set_hotel(night:str, value:str):
    _memory["hotels"][night]=value; return _memory["hotels"]

def hotels(): return _memory["hotels"]

def set_vehicle(value:dict):
    _memory["vehicle"]=value; return value

def vehicle(): return _memory["vehicle"]

def db_status():
    return {"configured": bool(_db()), "mode": "database-configured" if _db() else "memory-fallback"}
