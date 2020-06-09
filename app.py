from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('.env')

@app.before_first_request
def create_db():
   database.create_all()

@app.route('/')
def hello():
    return 'Hello World!'

if __name__ == '__main__':
    from data.sql_alchemy import database
    database.init_app(app)
    app.run(debug=True)
