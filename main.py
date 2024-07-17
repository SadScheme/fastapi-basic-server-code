from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from database import SessionLocal, init_db
from crud import create_order, get_orders, create_invoice, get_invoices
from schemas import OrderCreate, Order, InvoiceCreate, Invoice
from typing import List

app = FastAPI()

# Dependency to get the DB session
async def get_db():
    async with SessionLocal() as session:
        yield session

@app.on_event("startup")
async def on_startup():
    await init_db()

@app.post("/orders/", response_model=Order)
async def create_order_endpoint(order: OrderCreate, db: AsyncSession = Depends(get_db)):
    return await create_order(db, order)

@app.get("/orders/", response_model=List[Order])
async def read_orders(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    return await get_orders(db, skip=skip, limit=limit)

@app.post("/invoices/", response_model=Invoice)
async def create_invoice_endpoint(invoice: InvoiceCreate, db: AsyncSession = Depends(get_db)):
    return await create_invoice(db, invoice)

@app.get("/invoices/", response_model=List[Invoice])
async def read_invoices(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    return await get_invoices(db, skip=skip, limit=limit)
