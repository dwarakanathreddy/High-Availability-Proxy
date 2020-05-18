from flask import Flask
import os
app = Flask(__name__)

@app.route("/")
def hello():
    vari = os.environ["appid"]
    print(vari)
    return "Hello World! "+ str(vari)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug = False)
