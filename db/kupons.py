from sqlalchemy import Integer, Column, VARCHAR, DECIMAL, DATE
from sqlalchemy.dialects.mssql import TINYINT

from db.base import BaseModel


class Coupons(BaseModel):
    __tablename__ = 'oc_coupon'

    coupon_id = Column(Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)

    name = Column(VARCHAR(128), unique=True, nullable=False)

    code = Column(VARCHAR(20), unique=True, nullable=False)

    type = Column(VARCHAR(1), nullable=False)

    discount = Column(DECIMAL, nullable=False)

    logged = Column(TINYINT, nullable=False)

    shipping = Column(TINYINT, nullable=False)

    total = Column(DECIMAL, nullable=False)

    date_start = Column(DATE, nullable=False, default='0000-00-00')

    date_end = Column(DATE, nullable=False, default='0000-00-00')

    uses_total = Column(Integer, nullable=False)

    uses_customer = Column(VARCHAR(11), nullable=False)

    status = Column(TINYINT, nullable=False)

    date_added = Column(DATE, nullable=False)

    def __str__(self) -> str:
        return f"<Coupons:(self.coupon_id)>"


class Test(BaseModel):
    __tablename__ = 'test'

    id = Column(Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)

    name = Column(VARCHAR(32), nullable=False)

    age = Column(Integer, nullable=False)

    speed = Column(Integer, nullable=False)

    def __str__(self) -> str:
        return f"<Test:(self.id)>"
