#!/usr/bin/env python3

import logging

logging.basicConfig(
    filename="ref.log",
    level= logging.DEBUG,
    format= "%(asctime)s [ %(levelname)s ] %(name)s [ %(funcName)s ] [ %(filename)s, %(lineno)s ] %(message)s",
    datefmt= "[ %d/%m/%Y %H:%M:%S ]"
)

logging.info("Mensagem de teste")

CUSTUM = 49
logging.addLevelName(CUSTUM, "CUSTUM")
def custum(self, message, *args, **kwargs):
    if self.isEnabledFor(CUSTUM):
        self._log(CUSTUM, message, args, **kwargs)

logging.Logger.custum = custum

logger = logging.getLogger()
logger.custum("Meu log customizado")