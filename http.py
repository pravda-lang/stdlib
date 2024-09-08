import flask

def main(routing: list, host="localhost", port=8080):
    urls = [item[0] for item in routing]
    htmls = [item[1] for item in routing]
    app = flask.Flask("Pravda HTTP Server")
    @app.route("/<url>")
    def index(url: str):
        try:
            return htmls[urls.index(url)]
        except ValueError:
            return "Item not found", 404
    app.run(host, port)
