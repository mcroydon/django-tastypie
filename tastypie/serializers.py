from django.core.exceptions import ImproperlyConfigured
from django.core.serializers import json, xml_serializer, pyyaml
from django.template import loader, Context
from django.utils import simplejson
try:
    import lxml
except ImportError:
    lxml = None
try:
    import yaml
except ImportError:
    yaml = None


class Serializer(object):
    formats = ['json', 'xml', 'yaml', 'html']
    content_types = {
        'json': 'application/json',
        'xml': 'application/xml',
        'yaml': '',
        'html': 'text/html',
    }
    supported_formats = []
    
    def __init__(self, formats=None, content_types=None):
        if formats is not None:
            self.formats = formats
        
        if content_types is not None:
            self.content_types = content_types
        
        for format in self.formats:
            try:
                self.supported_formats.append(self.content_types[format])
            except KeyError:
                raise ImproperlyConfigured("Content type for specified type '%s' not found. Please provide it at either the class level or via the arguments." % format)
    
    def to_json(self, data):
        return simplejson.dump(data, cls=json.DjangoJSONEncoder, sort_keys=True)
    
    def from_json(self, content):
        return simplejson.loads(content)
    
    def to_xml(self, data):
        if lxml is None:
            raise ImproperlyConfigured("Usage of the XML aspects requires lxml.")
        
        # FIXME: This is incomplete and will likely be painful.
    
    def from_xml(self, content):
        if lxml is None:
            raise ImproperlyConfigured("Usage of the XML aspects requires lxml.")
        
        # FIXME: This is incomplete and will likely be painful.
    
    def to_yaml(self, data):
        if yaml is None:
            raise ImproperlyConfigured("Usage of the YAML aspects requires yaml.")
        
        return yaml.dump(data, Dumper=pyyaml.DjangoSafeDumper)
    
    def from_yaml(self, content):
        if yaml is None:
            raise ImproperlyConfigured("Usage of the YAML aspects requires yaml.")
        
        return yaml.load(content)
    
    def to_html(self, data):
        pass
    
    def from_html(self, content):
        pass
    