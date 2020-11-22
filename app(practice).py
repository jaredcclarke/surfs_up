from flask import Flask
app = Flask(__name__)
@app.route('/')
    def hello_world():
       return 'Hello world'

@app.route('/name')
    def name():
        return 'Jared'

app.route('/age')
    def age():
        return '32'