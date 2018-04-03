# -*- coding: utf-8 -*-
from sqlalchemy import (
    Column,
    BigInteger,
    String,
)

from . import Base


class User(Base):
    __tablename__ = 'alo_user'
    id = Column(BigInteger, primary_key=True)
    nickname = Column(String(32), nullable=False, unique=True)
    realname = Column(String(32), nullable=False, default='')
    password = Column(String(64), nullable=False, default='')
    email = Column(String(64), nullable=True, default=None, unique=True)
    phone = Column(String(16), nullable=True, default=None, unique=True)
