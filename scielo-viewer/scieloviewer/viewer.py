# coding: utf-8

import urllib2

#class Viewer(object):


class LoadService(object):
    def __init__(self, url, obj_urllib2=urllib2):
        self._url = url
        self._obj_urllib2 = obj_urllib2

    def get_client_metadata(self):
        try:
            json_string = self._obj_urllib2.urlopen(self._url).read()
        except urllib2.URLError:
            return None

        return json_string

    def validate_metadata(self, metadata):

        return True