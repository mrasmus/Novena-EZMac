from django import http
from django.core.serializers.json import DjangoJSONEncoder
from django.utils.encoding import force_text
from models import *
import json
from django.core import serializers

class EzJSONEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Address):
            return {'Serial': str(obj.serial),
                               'MAC': str(obj.mac),
                               'Status': str(obj.status)}
        return super(EzJSONEncoder, self).default(obj)

# http://www.pioverpi.net/2012/05/14/ajax-json-responses-using-django-class-based-views/
class JSONDetailResponseMixin(object):
    def render_to_response(self, context):
        "Returns a JSON response containing 'context' as payload"
        return self.get_json_response(self.convert_context_to_json(context))

    def get_json_response(self, content, **httpresponse_kwargs):
        "Construct an `HttpResponse` object."
        return http.HttpResponse(content,
                                 content_type='application/json',
                                 **httpresponse_kwargs)

    def convert_context_to_json(self, context):
        "Convert the context dictionary into a JSON object"
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        return json.dumps(context['object'], cls=EzJSONEncoder)
