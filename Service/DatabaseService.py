import psycopg2

from domain.Error import Error
from domain.Service import Service


class DatabaseService:
    SEARCH_SQL = """SELECT id, name, httpmethod, httpurl, payload, type, httpstatus, mimetype
        FROM "mock-service".services 
        WHERE httpmethod = %s AND httpurl = %s AND name = %s """

    def __init__(self):
        self.conn = psycopg2.connect("dbname='mock-service' host='localhost' user='service' password='service'")
        self.cursor = self.conn.cursor()

    @staticmethod
    def get_service_name_and_url(http_url):
        split = http_url.split('/')
        service_name = split[0]
        split = split[1:]
        url = "/".join(split)
        return service_name, url

    def search(self, http_method, http_url, body):
        body = str(body.decode('latin-1'))
        print(http_method, http_url)
        print(body)
        service_name, url = DatabaseService.get_service_name_and_url(http_url)
        if body is not None and body != '':
            self.cursor.execute(self.SEARCH_SQL + "AND (ignorerequestbody = true or body = %s) ",
                                (http_method, url, service_name, body))
        else:
            self.cursor.execute(self.SEARCH_SQL, (http_method, url, service_name))
        services = []
        errors = []
        for row in self.cursor.fetchall():
            if row[5] == 'service':
                if row[4] is None:
                    services.append(Service(row[0], row[1], row[2], row[3], None, row[5], row[6], row[7]))
                else:
                    services.append(Service(row[0], row[1], row[2], row[3], bytes(row[4]), row[5], row[6], row[7]))
            elif row[5] == 'error':
                errors.append(Error(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
        return services, errors
