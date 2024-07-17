from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from models import Order, Invoice
from schemas import OrderCreate

async def create_order(db: AsyncSession, order: OrderCreate):
    db_order = Order(**order.model_dump())
    db.add(db_order)
    await db.commit()
    await db.refresh(db_order)
    return db_order

async def get_orders(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(Order).offset(skip).limit(limit))
    return result.scalars().all()

async def create_invoice(db: AsyncSession, invoice: InvoiceCreate):
    db_invoice = Invoice(**invoice.dict())
    db.add(db_invoice)
    await db.commit()
    await db.refresh(db_invoice)
    return db_invoice

async def get_invoices(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(Invoice).offset(skip).limit(limit))
    return result.scalars().all()
