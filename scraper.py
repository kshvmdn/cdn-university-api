import requests
import bs4
import pprint
import json

BASE_URL = 'http://www.electronicinfo.ca/programs/{0}'


def scrape(prog_code):
    return parse(request(prog_code))


def request(prog_code):
    """Return the html content for the program_code provided."""
    return requests.get(BASE_URL.format(prog_code))


def parse(response):
    """Parse response for the given program content and return data as a dict"""
    return response.text

