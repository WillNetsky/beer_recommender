#!/usr/bin/env python
from app import app as application

if __name__ == '__main__':
    application.run(port=9000, debug=True)
