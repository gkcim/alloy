# -*- coding: utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
metadata = Base.metadata

from .user import *  # noqa
