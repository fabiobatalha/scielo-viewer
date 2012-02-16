# coding: utf-8

import urllib2

class Viewer(object):

    def get_client_metadata(self, url, obj_urllib2=urllib2):
		
        try:
        	#urllib2_instance = obj_urllib2()
        	json_string = obj_urllib2.urlopen(url).read()
        except urllib2.URLError:
            return None
        else:
            return json_string
