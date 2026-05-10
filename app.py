from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def show_ip():
    # Get the IP address
    client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    
    # Render the HTML page and pass the IP address to it
    return render_template('index.html', ip_address=client_ip)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)