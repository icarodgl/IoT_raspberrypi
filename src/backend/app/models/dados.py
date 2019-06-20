from peewee import Model, CharField, FloatField,DateTimeField
from banco_config import BancoConfig

db = BancoConfig.banco()

'''
ModeloBase das classes
'''
class ModeloBase(Model):
    def __str__(self):
        return str(self)

    class Meta:
        database = db

class Dados(ModeloBase):
    rasp_id = CharField()
    temp = FloatField(default=0)
    umi = FloatField(default=0)
    pres = FloatField(default=0)
    data = DateTimeField()