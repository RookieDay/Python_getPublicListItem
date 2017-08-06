# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, create_engine, Integer, Sequence, MetaData, Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/t_guangdong',echo=True)
metadata = MetaData(engine)
Base.metadata.drop_all(engine)
user_table = Table('guangdongMsg', metadata,
        Column('id', Integer, primary_key=True),
        Column('case_no', String(200)),
        Column('case_name', String(200)),
        Column('punish_type1', String(200)),
        Column('punish_type2', String(200)),
        Column('punish_reason', String(500)),
        Column('law_item', String(800)),
        Column('punish_result', String(800)),
        Column('entity_name', String(200)),
        Column('credit_no', String(200)),
        Column('org_code', String(200)),
        Column('reg_no', String(200)),
        Column('tax_no', String(200)),
        Column('identity_card', String(200)),
        Column('legal_man', String(200)),
        Column('punish_date', String(200)),
        Column('punish_agent', String(200)), 
        Column('area_code', String(200)),
        Column('current_status', String(200)), 
        Column('offical_updtime', String(200)), 
        Column('note', String(200))
        )
metadata.create_all()
