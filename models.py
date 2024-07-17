from sqlalchemy import Table, Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

# Association table for many-to-many relationship
order_invoice = Table(
    'order_invoice',
    Base.metadata,
    Column('order_id', Integer, ForeignKey('orders.id'), primary_key=True),
    Column('invoice_id', Integer, ForeignKey('invoices.id'), primary_key=True)
)

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, index=True)
    invoices = relationship("Invoice", secondary=order_invoice, back_populates="orders")

class Invoice(Base):
    __tablename__ = 'invoices'
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Integer)
    orders = relationship("Order", secondary=order_invoice, back_populates="invoices")