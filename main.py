from flask import Flask, make_response
import os

web_files = "./dist/"

App = Flask(__name__, static_folder=web_files, static_url_path='')


@App.route('/')
def index():
    return make_response(open(web_files+"index.html").read())


if __name__ == "__main__":
    if(os.getenv('ENV') == "production"):
        App.run()
    else:
        App.run(debug=True)
