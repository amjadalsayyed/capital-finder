from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests
 
class handler(BaseHTTPRequestHandler):

    # method to handle HTTP GET Request 
    def do_GET(self):
        
        path = self.path
        url_comp = parse.urlsplit(path)
        dict_of_res = dict(parse.parse_qsl(url_comp.query))
        country_name_s = dict_of_res.get("name")


        if country_name_s:
            url = f"https://restcountries.com/v3.1/name/{country_name_s}?fullText=true"
            res = requests.get(url)
            data = res.json()
            name_of_capital = data[0]["capital"][0]
            result = f'The capital of {country_name_s} is {name_of_capital}.'  



        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(result.encode('utf-8'))
        return