#!/usr/bin/env python3
import random
import datetime


class DataGenerator:

    def __init__(self):
        self.meta = {"temp": 20.0, "pres": 1.0, "umi": 50.0}
        self.atual = {"temp": 20.0, "pres": 1.0, "umi": 50.0}


    def generate(self):
        # logica do fake data coletar dados de um sendor de verdade

        if round(self.atual["temp"], 1) == round(self.meta["temp"], 1):
            self.meta["temp"] = random.randint(20, 35) + random.random()

        if round(self.atual["pres"], 3) == round(self.meta["pres"], 3):
            self.meta["pres"] = random.random()

        if round(self.atual["umi"], 1) == round(self.meta["umi"], 1):
            self.meta["umi"] = random.randint(40, 95) + random.random()

        self.atual["umi"] += (self.meta["umi"] - self.atual["umi"]) / 10
        self.atual["pres"] += (self.meta["pres"] - self.atual["pres"]) / 10
        self.atual["temp"] += (self.meta["temp"] - self.atual["temp"]) / 10
        mensagem = "data: %s temp:%.2f, pres: %.3f, umi: %.2f" % (datetime.datetime.now(
        ).__str__(), self.atual["temp"], self.atual["pres"], self.atual["umi"],)

        return mensagem
