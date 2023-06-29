from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/')
def index():
    return Response(open('page.html').read(), mimetype="text/html")

if __name__ == '__main__':
    app.run()
