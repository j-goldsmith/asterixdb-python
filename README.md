# asterixdb-python
Python wrapper for AsterixDB HTTP API
https://asterixdb.apache.org/docs/0.9.2/api.html

AsterixConnection 
- server: defaults to 'http://localhost'
- port: defaults to 19002

AsterixConnection.query
- statement: SQL++, required
- pretty: response formatting, defaults to false
- client_context_id: defaults to None
  
query 'mode' is always immediate. async and deferred not implemented.
~~~~
asterix_conn = AsterixConnection()
response = asterix_conn.query('''
    use TinySocial;
    SELECT VALUE ds FROM Metadata.`Dataset` ds;
    SELECT VALUE ix FROM Metadata.`Index` ix;''')

print(response.results)
~~~~~
