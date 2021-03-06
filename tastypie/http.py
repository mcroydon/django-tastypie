from django.http import HttpResponse


class HttpCreated(HttpResponse):
    status_code = 201
    
    def __init__(self, *args, **kwargs):
        if 'location' in kwargs:
            location = kwargs['location']
            del(kwargs['location'])
        
        super(HttpCreated, self).__init__(*args, **kwargs)
        self['Location'] = location


class HttpAccepted(HttpResponse):
    status_code = 204


class HttpSeeOther(HttpResponse):
    status_code = 303


class HttpNotModified(HttpResponse):
    status_code = 304


class HttpMethodNotAllowed(HttpResponse):
    status_code = 405


class HttpConflict(HttpResponse):
    status_code = 409


class HttpGone(HttpResponse):
    status_code = 410


class HttpNotImplemented(HttpResponse):
    status_code = 501
