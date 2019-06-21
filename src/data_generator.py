#!/usr/bin/env python3
import random
import datetime
import netifaces
import json


class DataGenerator:

    def __init__(self):
        self.meta = {"temp": 20.0, "pres": 1.0, "umi": 50.0}
        self.atual = {"temp": 20.0, "pres": 1.0, "umi": 50.0}
        self.macaddress = self.getMacAddress()

    def generate(self):
        # logica do fake data coletar dados de um sendor de verdade
        if (round(self.atual["temp"], 1) == round(self.meta["temp"], 1)):
            self.meta["temp"] = random.randint(20, 35) + random.random()
        if (round(self.atual["pres"], 3) == round(self.meta["pres"], 3)):
            self.meta["pres"] = random.random()
        if (round(self.atual["umi"], 1) == round(self.meta["umi"], 1)):
            self.meta["umi"] = random.randint(40, 95) + random.random()
        mensagem = ""
        regulador = random.randint(1,100)
        if (regulador <= 20 ):
            self.atual["umi"] += (self.meta["umi"] - self.atual["umi"])/10
            self.atual["pres"] += (self.meta["pres"] - self.atual["pres"])/10
            self.atual["temp"] += (self.meta["temp"] - self.atual["temp"])/10
            self.atual["date"] = datetime.datetime.now().__str__()
            self.atual["id"] = self.macaddress
            mensagem = json.dumps(self.atual)
        elif (regulador >= 90):
            mensagem = json.dumps({"ruido": "huehuehuehuehue"})
        else:
            self.atual["date"] = datetime.datetime.now().__str__()
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
