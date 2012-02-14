# coding: utf-8

import json

class ServicesSampler(object):

    def __init__(self,request):
        self._service_domain = "http://localhost:6543/"
        self._metadata = {}

    def json_metadata_delivery(self):

        self._metadata['title'] = "A Pilot's Guide to Aircraft Insurance"
        self._metadata['subject'] = ["Aircraft leasing and renting","Dogs","Olympic Skiing"]
        self._metadata['description'] = "Illustrated guide to airport markings and lighting signals, with particular reference to SMGCS (Surface Movement Guidance and Control System) for airports with low visibility conditions."
        self._metadata['type'] = "Text"
        self._metadata['source'] = "http://lildbibio.bhlscielo.org/1283hd3"
        self._metadata['coverage'] = ["1995-1996","Boston, MA","17th century","Upstate New York"]
        self._metadata['creator'] = ["Shakespear, William","Wen Lee","Hubble Telescope"]
        self._metadata['publisher'] = ["University of South Where","Institute of Biodiversity"]
        self._metadata['contributor'] = ["Comite de Ciências","MZUSP"]
        self._metadata['rights'] = ["Access limited to members","Creative Commons NYBCC"]
        self._metadata['date'] = ["1999-12-31","1998-12","1999"]
        self._metadata['format'] = ["file/pdf"]
        self._metadata['identifier'] = ["DOI...","ISBN:0385424728"]
        self._metadata['language'] = ['en','br','en-US','pt-BR','es']
        self._metadata['audience'] = ['elementary school student','ESL Teatchers','adults']
        self._metadata['provence'] = ['This copy once owned by Benjamin Spock.','MZUSP']
        self._metadata['file_url'] = ['http://lildbibio.bhlscielo.org/pdf/1283hd3']
        
        json_metadata = str(self._metadata) 


        return json_metadata