#!/usr/bin/env python3
import random
import datetime
import netifaces
import json
from pytz import timezone


class DataGenerator:

    def __init__(self):
        self.meta = {"temp": 20.0, "pres": 1.0, "umi": 50.0}
        self.atual = {
            "temp":round( random.randint(24, 28) + random.random(),2),
            "pres":round( ((1.5 + random.random())/2),2),
            "umi":round( random.randint(60, 80) + random.random(),2)
        }
        self.macaddress = self.getMacAddress()
        self.fuso_horario = timezone('America/Sao_Paulo')

    def generate(self):
        # logica do fake data coletar dados de um sendor de verdade
        if (round(self.atual["temp"], 1) == round(self.meta["temp"], 1)):
            self.meta["temp"] = random.randint(24, 28) + random.random()
        if (round(self.atual["pres"], 3) == round(self.meta["pres"], 3)):
            rval = random.random()
            self.meta["pres"] = (1.5 + rval)/2
        if (round(self.atual["umi"], 1) == round(self.meta["umi"], 1)):
            self.meta["umi"] = random.randint(60, 80) + random.random()
        mensagem = ""
        regulador = random.randint(1,100)
        if (regulador <= 5 ):
            self.atual["umi"] += round((self.meta["umi"] - self.atual["umi"])/10, 2)
            self.atual["pres"] += round((self.meta["pres"] - self.atual["pres"])/10, 2)
            self.atual["temp"] += round((self.meta["temp"] - self.atual["temp"])/10, 2)
            self.atual["date"] = datetime.datetime.now(tz=self.fuso_horario).__str__()
            self.atual["id"] = self.macaddress
            mensagem = json.dumps(self.atual)
        elif (regulador >= 95):
            mensagem = json.dumps({"ruido": "huehuehuehuehue"})
        else:
            self.atual["date"] = datetime.datetime.now(tz=self.fuso_horario).__str__()
            self.atual["id"] = self.macaddress
            mensagem = json.dumps(self.atual)
        return mensagem

    def getMacAddress(self):
        interfaces = netifaces.interfaces()
        interface = interfaces[0]
        if (len(interfaces) == 0):
            return ""
        elif (len(interfaces) > 1):
            interface = interfaces[1]
        else:
            interface = interfaces[0]
        return netifaces.ifaddresses(interface)[netifaces.AF_LINK][0]["addr"]
