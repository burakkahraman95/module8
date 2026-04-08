from flask import Flask, request, Response
import requests

app = Flask(__name__)

backends = ['http://127.0.0.1:5000', 'http://127.0.0.1:5001']
current = 0

@app.route('/', methods=['GET', 'POST'])
def load_balancer():
    global current
    backend = backends[current]
    current = (current + 1) % len(backends)
    resp = requests.request(
        method=request.method,
        url=backend + request.path,
        data=request.get_data(),
        headers=dict(request.headers)
    )
    return (resp.content, resp.status_code, resp.headers.items())

if __name__ == '__main__':
    app.run(port=8000)
