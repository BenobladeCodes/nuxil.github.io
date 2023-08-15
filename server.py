import http.server
import socketserver
import socket

PORT = 8080

# Find your local IP address
def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except:
        return "Unavailable"

local_ip = get_local_ip()

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at {local_ip}:{PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

# Print local IP at the end
print("Local IP:", local_ip)
