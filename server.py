from http.server import HTTPServer,BaseHTTPRequestHandler

content = '''
<!doctype html>
<HTML>
<HEAD>
</HEAD>
<body bgcolor="cyan">
    <table border="1" align="center" bgcolour="pink" cellpadding>
        <caption><h1>list of protocols</h1></caption>
        <tr><th>s.no</th><th>name of the layer<th>Name of the protocal</th></tr>
        <tr><td>1</td><td>application layer</td><td>http, ftp</td></tr>
        <tr><td>2</td><td>transport layer</td><td>TCP & UDP</td></tr>
        <tr><td>2</td><td>internet layer</td><td>ipv4 & ipv6</td></tr>
        <tr><td>3</td><td>physical layer</td><td>Ethernet</td></tr>
    </table>
</body>
</html>
'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('127.0.0.20',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()