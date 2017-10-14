from urllib import parse, request
from json import loads

class QueryResponse:
    def __init__(self, raw_response):
        self._json = loads(raw_response)

        self.requestID = self._json['requestID'] if 'requestID' in self._json else None
        self.clientContextID = self._json['clientContextID'] if 'clientContextID' in self._json else None
        self.signature = self._json['signature'] if 'signature' in self._json else None
        self.results = self._json['results'] if 'results' in self. _json else None
        self.metrics = self._json['metrics'] if 'metrics' in self._json else None

class AsterixConnection:
    def __init__(self, server = 'http://localhost', port = 19002):
        self._server = server
        self._port = port
        self._url_base = self._server +':'+ str(port)

    def query(self, statement, pretty=False, client_context_id=None):
        endpoint = '/query/service'

        url = self._url_base + endpoint

        payload = {
            'statement': statement,
            'pretty': pretty
        }

        if client_context_id:
            payload['client_context_id'] = client_context_id

        data = parse.urlencode(payload).encode("utf-8")
        req = request.Request(url, data)
        response = request.urlopen(req).read()

        return QueryResponse(response)


if __name__ == '__main__':
    asterix_conn = AsterixConnection()
    response = asterix_conn.query('''
        use TinySocial;
        SELECT VALUE ds FROM Metadata.`Dataset` ds;
        SELECT VALUE ix FROM Metadata.`Index` ix;''')

    print(response.results)