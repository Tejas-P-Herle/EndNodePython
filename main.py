#!/usr/bin/env python3

import os
from pymongo import MongoClient
from selenium import webdriver
from flask import Flask, request, jsonify

app = Flask(__name__)
port = os.environ["PORT"] if "PORT" in os.environ else 5000
password = os.environ["password"] if "password" in os.environ else ""
uri = f'mongodb+srv://admin:{password}@scraperdata.oov0lls.mongodb.net/?retryWrites=true&w=majority'

options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("--headless")
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

browser = None
dbClient = None


@app.route('/')
def hello_world():
    return 'End Point is Awake'


@app.route('/testBrowser')
def testBrowser():
    global browser, dbClient
    if not browser or not dbClient:
        wakeUp()

    browser.get('https://example.com')
    return browser.page_source


@app.route('/scrape')
def scrape():
    global browser, dbClient
    if not browser or not dbClient:
        wakeUp()

    reqObj = request.json
    targetUrl = reqObj['targetUrl']
    selectionRules = reqObj['selectionRules']
    navigationRules = reqObj['navigationRules']

    browser.get(targetUrl)

    return jsonify({"DONE": True})


def wakeUp():
    global browser, dbClient

    browser = webbrowser.Chrome(options=options)
    # dbClient = MongoClient(uri)


def sleep():
    global browser, dbClient

    browser.close()
    dbClient.close()

    browser = None
    dbClient = None


if __name__ == '__main__':
    app.run('0.0.0.0')

