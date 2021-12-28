from flask import Flask
#from other_module import fn_from_other_module

#fn_from_other_module();

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5050)

# @app.route("/hello")
# def hello1():
#     return "Hello1, World!"   