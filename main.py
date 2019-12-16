import flask

from Service.DatabaseService import DatabaseService

app = flask.Flask(__name__)
database_service = DatabaseService()


@app.route('/', defaults={'path': '', 'method': ''})
@app.route('/<path:path>', methods=['POST', 'GET', 'PATCH', 'PUT', 'OPTIONS'])
def catch_all(path):
    services, errors = database_service.search(flask.request.method, path, flask.request.data)
    if len(services) == 1:
        return flask.Response(services[0].payload, mimetype=services[0].mime_type, status=services[0].http_status)
    elif len(errors) == 1:
        return flask.Response(errors[0].payload, mimetype=errors[0].mime_type, status=errors[0].http_status)
    else:
        return flask.Response('{"message": "None or multiple results"}', mimetype='application/json', status=500)


if __name__ == '__main__':
    app.run()
