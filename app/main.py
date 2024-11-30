from fastapi import FastAPI, HTTPException
# from app.routers import payment
from app.services.payment_service import *
from pydantic import BaseModel


app = FastAPI()

# # 결제 라우터 등록
# app.include_router(payment.router, prefix="/payments", tags=["Payments"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Payment API"}





### 토큰 받기
@app.get("/auth/token")
async def check_token():
    """
    발급받은 액세스 토큰 확인용 엔드포인트
    """
    try:
        token = await get_access_token()
        return {"access_token": token}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

### 일회성 결제 본문 검증 pydantic
class PaymentRequest(BaseModel):
    pg: str
    merchant_uid: str
    card_number: str
    expiry: str
    birth: str
    amount: float



### 일회성 결제 엔드포인트
@app.post("/payments/onetime")
async def process_one_time_payment(payment_request: PaymentRequest):
    try:
        payload = payment_request.dict()
        print("Request Payload:", payload)
        # 일회성 결제 함수 호출
        res = await one_time_payment(payload)
        print("Response:", res)

        return res
    
    except Exception as e:
        raise HTTPException(status_code=400,detail=str(e))
    