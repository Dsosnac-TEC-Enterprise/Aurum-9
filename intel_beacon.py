from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from datetime import datetime

class GitHubIntelHandler(BaseHTTPRequestHandler):
    """Listens for incoming HTTP POST requests from GitHub Webhooks."""
    
    def do_POST(self):
        # Get the size of the incoming data
        content_length = int(self.headers['Content-Length'])
        # Read the data
        post_data = self.rfile.read(content_length)
        payload = json.loads(post_data.decode('utf-8'))
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # 1. Check for a FORK event
        if 'forkee' in payload:
            hacker_name = payload['forkee']['owner']['login']
            print(f"\n[🚨 {timestamp}] INTEL ALERT: Aurum-9 was FORKED by github.com/{hacker_name}")
            print(f"[*] Shadow-repo created at: {payload['forkee']['html_url']}")

        # 2. Check for a STAR event
        elif 'action' in payload and payload['action'] == 'created' and 'star_at' in payload:
             hacker_name = payload['sender']['login']
             print(f"\n[⭐ {timestamp}] INTEL ALERT: Aurum-9 was STARRED by {hacker_name}")

        # Send a 200 OK back to GitHub so they know we received it
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Intel received. Aurum-9 Out.")

    def log_message(self, format, *args):
        # Mute standard HTTP logs to keep the terminal clean
        pass

if __name__ == "__main__":
    port = 8080
    server = HTTPServer(('0.0.0.0', port), GitHubIntelHandler)
    print("="*50)
    print(" 📡 AURUM-9 INTEL BEACON ONLINE 📡 ")
    print(f" [*] Listening for GitHub Webhooks on port {port}...")
    print("="*50)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[*] Shutting down Intel Beacon.")
        server.server_close()
