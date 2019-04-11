import logging
import os

import flask

app = flask.Flask(__name__)

LOGGER = logging.getLogger("my-app")

STATUS = True

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/memory")
def ready():
    # allocate a lot of memory
    my_var = "x" * 1000000000
    return "Memory test"


@app.route("/replicas")
def replicas():
    return "Hello from: {}".format(os.getenv("HOSTNAME", "unknown"))

@app.route("/health")
def health():
    if STATUS:
        return "I am OK"
    else:
        flask.abort(500)

@app.route('/quit')
def quit():
    global STATUS
    STATUS = False
    return "I am about to quit"

def main():
    app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    main()
