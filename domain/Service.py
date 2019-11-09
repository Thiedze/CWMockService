from domain.Mock import Mock


class Service(Mock):

    def __init__(self, id, name, http_method, http_url, payload, service_type, http_status, mime_type):
        Mock.__init__(self, id, name, http_method, http_url, payload, service_type, http_status, mime_type)
