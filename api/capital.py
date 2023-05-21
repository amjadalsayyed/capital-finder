from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests
 
class handler(BaseHTTPRequestHandler):

    # method to handle HTTP GET Request 
    def do_GET(self):
        
        path = self.path
        url_comp = parse.urlsplit(path)
        dict_of_res = dict(parse.parse_qsl(url_comp.query))
        capital_name = dict_of_res.get("capital")


        if capital_name:
            url = f"https://restcountries.com/v3.1/capital/{capital_name}"
            res = requests.get(url)
            data = res.json()
            name_of_country = data[0]["name"]['common']
            result = f'{capital_name} is the capital of {name_of_country}'   



        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(result.encode('utf-8'))
        return