from flask import Flask, render_template
# from waitress import serve
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('main.html')


if __name__ == '__main__':
    app.run(host='143.89.144.230', port=81)
#    serve(app, host='143.89.144.230', port=81)
