# app/services/payment_service.py

from app.config import IMP_KEY, IMP_SECRET
import httpx

PORTONE_API_URL = "https://api.iamport.kr"

async def get_access_token():
    """
    포트원의 액세스 토큰 발급 API 호출
    """
    url = f"{PORTONE_API_URL}/users/getToken"  # 완전한 엔드포인트 URL
    payload = {
        "imp_key": IMP_KEY,
        "imp_secret": IMP_SECRET
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload)
        if response.status_code == 200:
            data = response.json()
            if data["code"] == 0:  # 성공 코드
                return data["response"]["access_token"]
            else:
                raise Exception(f"Token Error: {data['message']}")
        else:
            raise Exception(f"HTTP Error: {response.status_code} - {response.text}")



## 일회성 결제 함수
async def one_time_payment(payload: dict):

    access_token = await get_access_token()

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    url = f"{PORTONE_API_URL}/subscribe/payments/onetime"

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=payload)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"HTTP Error: {response.status_code} - {response.text}")
        
