from django.http import HttpResponse
from django.core.serializers import serialize
import json

class HttpMixinResponse(object):
    def render_to_http_response(self, json_confirm_data, status=200):
        return HttpResponse(json_confirm_data, content_type='application/json', status=status)

class SerializeMixin(object):    
    def serialize(self,query_string):
        json_data = serialize('json', query_string)
        dict_data = json.loads(json_data)
        complete_list_of_data = []
        for d in dict_data:
            cric_data = d['fields']
            complete_list_of_data.append(cric_data)
            json_data=json.dumps(complete_list_of_data)
        return json_data