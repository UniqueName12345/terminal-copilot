import yaml
import requests
from splinter import Browser

config = yaml.safe_load(open('config.yaml'))

with Browser('firefox') as browser:
    browser.visit("https://chat.openai.com/")
    browser.maximize_window()
    browser.find_by_id("login-button").click()
    browser.find_by_id("username").fill(config['openai']['email'])
    browser.find_by_id("action").click()
    browser.find_by_id("password").fill(config['openai']['password'])
    browser.find_by_id("action").click()
