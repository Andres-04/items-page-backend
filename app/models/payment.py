from pydantic import BaseModel

class PaymentMethods(BaseModel):
    credit_cards: list[str]
    debit_cards: list[str]
    cash: list[str]
