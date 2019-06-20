#!/usr/bin/python
# -*- coding: utf-8 -*-

from model import Dados
from db import BancoConfig

modelos = [Dados]

if True:  # true para criar banco
    db = BancoConfig.banco()
    db.connect()
    if True:  # True para Limpar banco
        db.drop_tables(modelos)
    db.create_tables(modelos)
    db.close()
