# coding: utf-8

from pyramid.view import view_config
from pyramid.response import Response
from .viewer import Viewer
from .tests import Dummyurllib2

@view_config(route_name='home', renderer='templates/home.pt')
def home(request):
    viewer_instance = Viewer()
    metadata = viewer_instance.get_client_metadata("http://www.scielo.br",Dummyurllib2)

    return {'metadata':metadata}
