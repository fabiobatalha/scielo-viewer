# coding: utf-8

import urllib2
import urlparse
import json

class InvalidSource(Exception):
    def __init__(self, *args):
        super(InvalidSource, self).__init__(*args)

class UnauthorizedParameters(Exception):
    def __init__(self, *args):
        super(UnauthorizedParameters, self).__init__(*args)

class InvalidData(Exception):
    def __init__(self, *args):
        super(InvalidData, self).__init__(*args)


class LoadService(object):
    def __init__(self, url, obj_urllib2=urllib2):
        self._url = url
        self._obj_urllib2 = obj_urllib2

    def get_client_metadata(self):
        try:
            url_file_data = self._obj_urllib2.urlopen(self._url)
        except urllib2.URLError:
            raise InvalidSource("Invalid URL: {}".format(_url))
        
        return url_file_data

    def delivery_metadata(self):
        """
        Convert Services Response into JSON Object
        """

        metadata = json.load(self.get_client_metadata())

        return metadata

    def validate_metadata(self):
        """
        Validate Mandatory fields that must be delivered, and not allowed parameters
        """
        metadata = self.get_client_metadata()

        return True

#class ViewerHandler(object):

    #def __init__(self):
        #self._metadata = {}

    #def prepare_metadata(self):