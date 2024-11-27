from flask import Flask
from app.blueprints import home_page
from app.blueprints import about

app=Flask(__name__)

app.register_blueprint(home_page.bp)
app.register_blueprint(about.bp)

if(__name__=='__main__'):
    app.run(debug=True)