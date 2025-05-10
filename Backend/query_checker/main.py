#!/usr/bin/python3

import validator
import queryManip as qm
import inputHandler as ih
import logger


class QueryChecker:
    def __init__(self,data, peer):
        self.og_query = data['og_query']
        self.input_vals = data['input_vals']
        self.og_query = ih.normalize_og_query(self.og_query,self.input_vals)
        self.host,self.port = peer
    

    def check(self):
        inp_query = qm.add_input(self.og_query, self.input_vals)
        validity = validator.validate_query(inp_query, self.og_query)
        logger.logServ("Query before adding user input :")
        logger.logServ(qm.read_query('og'))
        logger.logServ("Query after adding user input :")
        logger.logServ(qm.read_query('inp'))
        logger.logQuery(self.host,self.port,inp_query,self.og_query,validity)
        return validity


