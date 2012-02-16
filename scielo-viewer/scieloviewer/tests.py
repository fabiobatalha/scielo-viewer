# coding: utf-8

import unittest
import urllib2
from pyramid import testing

from .viewer import LoadService


class DummyFile(object):
    def __init__(self, str_data):
        self._str_data = str_data
    
    def read(self):
        return self._str_data

class Dummyurllib2(object):

    def __init__(self):
        self._metadata = {}

    def urlopen(self, url):
            urllib2.urlopen(url)
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

            json_metadata = DummyFile(str(self._metadata))

            return json_metadata

"""
VIEWER TestCase
"""
class LoadServiceTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
    
    def tearDown(self):
        testing.tearDown()

    def test_get_client_metadata(self):
        request = testing.DummyRequest()
        
        dummy_urllib2 = Dummyurllib2()
        dummy_metadata = dummy_urllib2.urlopen("http://www.scielo.br").read()

        """
        Valid Response
        """
        load_service_instance = LoadService("http://www.scielo.br",dummy_urllib2)
        metadata = load_service_instance.get_client_metadata()
        self.assertEqual(dummy_metadata, metadata)

        """
        URL Error return None
        """
        load_service_instance = LoadService("http://www.scielo.b",dummy_urllib2)
        metadata = load_service_instance.get_client_metadata()
        self.assertEqual(None, metadata)

    #def test_validate_metadata(self):





"""       
VIEWS TestCase
"""
class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    #def test_home(self):
        #from .views import home
        #request = testing.DummyRequest()
        #info = home(request)
        
        #viewer_instance = Viewer()
        #metadata = viewer_instance.get_client_metadata("http://www.scielo.br",Dummyurllib2)
        #import pdb; pdb.set_trace()
        #self.assertEqual(info['metadata'], metadata)
