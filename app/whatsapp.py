import os, httpx

async def send_whatsapp(to:str, text:str):
    token=os.getenv("WHATSAPP_TOKEN")
    phone_id=os.getenv("WHATSAPP_PHONE_NUMBER_ID")
    if not token or not phone_id:
        return {"sent":False,"reason":"WhatsApp credentials not configured"}
    url=f"https://graph.facebook.com/v23.0/{phone_id}/messages"
    payload={"messaging_product":"whatsapp","to":to,"type":"text","text":{"body":text}}
    async with httpx.AsyncClient(timeout=15) as client:
        r=await client.post(url,headers={"Authorization":f"Bearer {token}"},json=payload)
        return {"sent":r.is_success,"status_code":r.status_code,"response":r.json()}
