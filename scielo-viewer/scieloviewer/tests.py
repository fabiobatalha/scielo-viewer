# coding: utf-8

import unittest
import urllib2
import json
from pyramid import testing

from .viewer import LoadService, InvalidSource

dummy_metadata = {} 
dummy_metadata['title'] = "A Pilots Guide to Aircraft Insurance"
dummy_metadata['subject'] = ["Aircraft leasing and renting","Dogs","Olympic Skiing"]
dummy_metadata['description'] = "Illustrated guide to airport markings and lighting signals, with particular reference to SMGCS (Surface Movement Guidance and Control System) for airports with low visibility conditions."
dummy_metadata['type'] = "Text"
dummy_metadata['source'] = "http://lildbibio.bhlscielo.org/1283hd3"
dummy_metadata['coverage'] = ["1995-1996","Boston, MA","17th century","Upstate New York"]
dummy_metadata['creator'] = ["Shakespear, William","Wen Lee","Hubble Telescope"]
dummy_metadata['publisher'] = ["University of South Where","Institute of Biodiversity"]
dummy_metadata['contributor'] = ["Comite de Ciências","MZUSP"]
dummy_metadata['rights'] = ["Access limited to members","Creative Commons NYBCC"]
dummy_metadata['date'] = ["1999-12-31","1998-12","1999"]
dummy_metadata['format'] = ["file/pdf"]
dummy_metadata['identifier'] = ["DOI...","ISBN:0385424728"]
dummy_metadata['language'] = ['en','br','en-US','pt-BR','es']
dummy_metadata['audience'] = ['elementary school student','ESL Teatchers','adults']
dummy_metadata['provence'] = ['This copy once owned by Benjamin Spock.','MZUSP']
dummy_metadata['file_url'] = ['http://lildbibio.bhlscielo.org/pdf/1283hd3']


class DummyFile(object):
    def __init__(self, data):
        self._data = data
    
    def read(self):
        return json.dumps(self._data)

class Dummyurllib2(object):

    def __init__(self):
        self._metadata = {}

    def urlopen(self, url):
            try:
                urllib2.urlopen(url)
            except urllib2.URLError:
                raise InvalidSource()

            self._metadata = dummy_metadata
            json_metadata = DummyFile(self._metadata)

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

        """
        Valid Response
        """
        load_service_instance = LoadService("http://www.scielo.br",dummy_urllib2)
        metadata = load_service_instance.get_client_metadata()
        self.assertIsInstance(metadata, DummyFile)

        """
        Invalid URL
        """
        load_service_instance = LoadService("http://www.scielo.b",dummy_urllib2)
        self.assertRaises(InvalidSource, load_service_instance.get_client_metadata)

    def test_delivery_metadata(self):

        dummy_urllib2 = Dummyurllib2()
        dummy_json_metadata = json.loads(json.dumps(dummy_metadata))

        """
        Testing the metadata delivery
        """
        load_service_instance = LoadService("http://www.scielo.br",dummy_urllib2)
        metadata = load_service_instance.delivery_metadata()
        #import pdb; pdb.set_trace()
        self.assertEquals(metadata,dummy_json_metadata)


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
