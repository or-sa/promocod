from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from db.kupons import Coupons, Test


# def create_as_engine(url: str) -> AsyncEngine:
#     return create_async_engine(url=url, echo=True, encoding='utf-8', pool_pre_ping=True)
#
#
# def get_session_maker(engine: AsyncEngine) -> sessionmaker:
#     return sessionmaker(bind=engine, class_=AsyncSession)


def test(con):
    engine = create_engine(url=con, echo=True)

    session = sessionmaker(bind=engine)
    s = session()
    kup_list = list()

    for row in s.query(Test).all():
        # kup_list.append(f'{row.name} - {row.discount} % - {row.status} \n')
        kup_list.append(f'{row.name} - {row.age} % - {row.speed} \n')
    return kup_list


# def test(sm):
#     session = sm
#     s = session()
#     kup_list = list()
#     for row in s.query(Coupons).all():
#         kup_list.append(f'{row.name} - {row.discount} % - {row.status} \n')
#     return kup_list
#
#
# def kups_list()

