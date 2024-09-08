import flask
def main(html, host="localhost", port=8080):
    app = flask.Flask("Pravda HTTP Server")
    @app.route("/")
    def index():
        return html
    app.run(host, port)
