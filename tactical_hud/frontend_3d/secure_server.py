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

# --- MODERN ENCRYPTION BLOCK (Python 3.12+) ---
try:
    # Create a secure SSL context for a server
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    
    # Load the keys you just generated
    # Paths adjusted to reach root from tactical_hud/frontend_3d/
    context.load_cert_chain(certfile='../../cert.pem', keyfile='../../key.pem')
    
    # Wrap the socket using the modern context
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
    
    print("="*50)
    print(" 🔒 AURUM-9 SECURE HUD: ONLINE (TLS 1.3) ")
    print(f" [*] Operator: Dsosnac-TEC-Enterprise")
    print(f" [*] Secure Access: https://localhost:{PORT}")
    print("="*50)
    
    httpd.serve_forever()

except Exception as e:
    print(f"\n[-] ENCRYPTION FAILURE.")
    print(f"[!] Technical Detail: {e}")
    print("[*] Solution: Ensure cert.pem and key.pem are in the root directory.")
