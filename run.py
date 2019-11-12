"""Assignment 2: House Price Data."""

# ~ For this project, my hope is that we will read in the [Paid Price Data](https://www.gov.uk/government/statistical-data-sets/price-paid-data-downloads) from HM Land Registry, write it to a [SQLite](https://docs.python.org/3/library/sqlite3.html) database, and create a [Flask](https://flask.palletsprojects.com/en/1.1.x/) web app that uses Leaflet to visualize a selection of that data on a map. This should be able to run anywhere by anyone with the code, but we'll host it on PythonAnywhere; and then we'll try and also have an API on the PythonAnywhere site so that we can also display the Leaflet frontend on a static site.

from flask import Flask         # for serving web app

app = Flask(__name__)

@app.route('/')
def house_prices():
    """Returns a minimal example."""
    return "<title>House Prices</title> Houses cost money."

if __name__=='__main__':
    app.run()
    
