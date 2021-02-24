# -*- coding: utf-8 -*-

import os.path
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

    def opj(self, path):
        # print os.path.abspath(os.path.dirname(__file__))
        tpl = path.split("/")
        st = os.path.join(*tpl)
        # HACK: on Linux, a leading / gets lost...
        if path.startswith("/"):
            st = "/" + st
        return st

    def __del__(self):
        pass
