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
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    prog_info = {}
    if soup.find('h1', class_='template-heading'):
        prog_title = soup.find('h1', class_='template-heading').string
        # prog_school = soup.find('h2', class_='template-subheading').string
    prog_info['overview'], prog_info['admission'] = {}, {}
    prog_info['overview']['title'] = prog_title
    if soup.find('div', class_='tabbed-section'):
        overview = soup.find('div', id='overview')
        for tr in overview.find('table').find_all('tr'):
            key = tr.find_all('td')[0].string.lower().replace(' ', '_')
            value = tr.find_all('td')[1].text.strip()
            prog_info['overview'][key] = value
        admission = soup.find('div', id='admission')
        for h3 in admission.find(class_='tabbed-subsection').find_all('h3'):
            key = h3.text.lower().replace(' ', '_')
            value = []
            while h3.next_sibling is not None and\
                    (h3.next_sibling.name is None or h3.next_sibling.name == 'p'):
                h3 = h3.next_sibling
                print(type(h3))

                if h3.string is not None and h3.string.strip() is not '':
                    value.append(h3.text)
            print('---')
            # prog_info['admission'][key] = value
    pprint.pprint(prog_info, indent=2)


uoft_cs = '203'
uw_afm = '301'

scrape(uw_afm)
