from pydantic import BaseModel
from typing import List, Optional

class InvoiceBase(BaseModel):
    amount: int

class InvoiceCreate(InvoiceBase):
    pass

class Invoice(InvoiceBase):
    id: int
    orders: List['Order'] = []

    class Config:
        orm_mode = True

class OrderBase(BaseModel):
    description: str

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: int
    invoices: List[Invoice] = []

    class Config:
        orm_mode = True
