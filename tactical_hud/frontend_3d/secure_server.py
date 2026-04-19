import http.server
import ssl
import os

# Define Port
PORT = 8443

# Ensure we are in the right directory
web_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(web_dir)

# Initialize standard server
server_address = ('0.0.0.0', PORT)
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)

# Wrap it in SSL/TLS Encryption
try:
    httpd.socket = ssl.wrap_socket(
        httpd.socket,
        server_side=True,
        certfile='../../cert.pem', # Points to the cert we just made
        keyfile='../../key.pem',   # Points to the key we just made
        ssl_version=ssl.PROTOCOL_TLS
    )
    print("="*50)
    print(f" 🔒 AURUM-9 SECURE HUD ONLINE ")
    print(f" [*] Access via: https://localhost:{PORT}")
    print("="*50)
    httpd.serve_forever()
except Exception as e:
    print(f"[-] Encryption failure. Did you generate the keys? Error: {e}")
