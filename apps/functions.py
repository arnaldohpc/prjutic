# -*- coding: utf-8 -*-
import datetime


class Functions(object):
    def __init__(self):
        pass

    # Ahora mismo
    def now_txt(self):
        ahora_t = ""
        ahora = datetime.datetime.now()
        ahora = ahora.strftime("%d/%m/%Y %H:%M")
        ahora_t = str(ahora)
        return ahora_t

    def __del__(self):
        pass
