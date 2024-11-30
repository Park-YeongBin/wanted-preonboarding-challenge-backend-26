from pydantic import BaseModel

# 요청/응답 스키마
class VirtualAccountCreateRequest(BaseModel):
    user_id: int
    amount: float
    description: str

class VirtualAccountCreateResponse(BaseModel):
    account_number: str
    bank_name: str
    expiration_date: str

class PaymentCancelRequest(BaseModel):
    transaction_id: str

class PaymentCancelResponse(BaseModel):
    status: str
    reason: str
