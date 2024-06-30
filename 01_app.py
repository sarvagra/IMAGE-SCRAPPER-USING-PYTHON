from flask import Flask
from flask import request
from flask import render_template,jsonify
import logging 
logging.basicConfig(filename="01_logging.log", level=logging.DEBUG, format='%(asctime)s %(message)s')

logging.info()