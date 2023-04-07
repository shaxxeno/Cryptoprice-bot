from sqlalchemy import Column, Integer, VARCHAR, DATE, BigInteger, String
import datetime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    # Telegram user ID
    user_id = Column(BigInteger, unique=True, nullable=False, primary_key=True)

    user_name = Column(VARCHAR(32), unique=False, nullable=True)

    reg_date = Column(DATE, default=datetime.datetime.today())

    upd_date = Column(DATE, onupdate=datetime.datetime.today())

    def __str__(self) -> str:
        return f'<User:{self.user_id}>'
