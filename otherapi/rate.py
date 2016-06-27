#!/usr/bin/env python

#https://github.com/jzempel/fedex

#workon fedex-second-api

from fedex.services import FedexService
from fedex.config import FedexConfiguration
import os.path

file_path = os.path.abspath(__file__)
dir_name = os.path.dirname(file_path)
file_name = os.path.join(dir_name, "cred.cfg")

conf = FedexConfiguration(wsdls='beta', file_name=file_name)



#serv = FedexService
