# coding: utf-8

import urllib2

class Viewer(object):

    def get_client_metadata(self, url, obj_urllib2=urllib2):

        try:
            urllib2_instance = obj_urllib2()
            json_string = urllib2_instance.urlopen(url)
        except urllib2.URLError:
            return None
        else:
            return json_string
