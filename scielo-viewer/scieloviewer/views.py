from pyramid.view import view_config
from pyramid.response import Response
from .services import ServicesSampler

@view_config(route_name='home', renderer='templates/home.pt')
def home(request):
    return {'project':'scielo-viewer'}

@view_config(route_name='metadata_delivery', renderer='templates/metadata_delivery.pt')
def json_metadata_delivery(request):
    ss = ServicesSampler(request)
    sample = ss.json_metadata_delivery()

    return {'metadata':sample}