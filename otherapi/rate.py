#!/usr/bin/env python

#https://github.com/jzempel/fedex

#workon fedex-second-api

from fedex.services import FedexService
import fedex.config
import os.path

file_path = os.path.abspath(__file__)
dir_name = os.path.dirname(file_path)
file_name = os.path.join(dir_name, "cred.cfg")

#serv = FedexService
