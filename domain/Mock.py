class Mock:

    def __init__(self, id, name, http_method, http_url, payload, service_type, http_status, mime_type):
        self.id = id
        self.name = name
        self.http_method = http_method
        self.http_url = http_url
        self.payload = payload
        self.service_type = service_type
        self.http_status = http_status
        self.mime_type = mime_type
