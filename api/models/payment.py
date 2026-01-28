from pydantic import BaseModel, EmailStr, Field

class PaymentReport(BaseModel):
    project: str = Field(..., min_length=3, max_length=50)
    name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    amount: float = Field(..., gt=0)
    currency: str = Field(..., min_length=2, max_length=10)
    reference: str = Field(..., min_length=4, max_length=100)
    method: str = Field(..., min_length=2, max_length=50)
    anonymous: bool
