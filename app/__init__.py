from flask import Flask
from app.blueprints import home_page

app=Flask(__name__)

app.register_blueprint(home_page.bp)


if(__name__=='__main__'):
    app.run(debug=True)