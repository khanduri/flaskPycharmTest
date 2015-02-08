import sys
import os


sys.path.insert(1, os.path.join(os.path.abspath("."), 'venv/lib/python2.7/site-packages'))


from app import app


if __name__ == "__main__":
    app.run()