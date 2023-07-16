from app import app
from Home import home

app.register_blueprint(home, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
