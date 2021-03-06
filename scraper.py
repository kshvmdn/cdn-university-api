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

    prog_info['overview'], prog_info['admission'], prog_info['requirements'] = \
        {}, {}, {}

    if soup.find('div', class_='tabbed-section'):
        overview = soup.find('div', id='overview')
        for tr in overview.find('table').find_all('tr'):
            key = tr.find_all('td')[0].string.lower().replace(' ', '_')
            value = tr.find_all('td')[1].text.strip().replace('\n', ', ')
            prog_info['overview'][key] = value
        prog_info['overview']['title'] = prog_title

        admission = soup.find('div', id='admission')
        for h3 in admission.find(class_='tabbed-subsection').find_all('h3'):
            key = h3.text.lower().replace(' ', '_')
            value = []
            for sib in h3.next_siblings:
                if sib.string is None or sib.string.strip() is not '':
                    value.append(sib.text)
                if sib.next_sibling is None or sib.next_sibling.name == 'h3':
                    break
            prog_info['admission'][key] = value

        req = soup.find('div', id='requirements').find('div', class_='tabbed-subsection')
        key = req.find('h4').string.lower()
        prereqs = []
        if req.find('ul'):
            for li in req.find_all('li'):
                prereqs.append(li.string)
        prog_info['requirements'][key] = prereqs
        return prog_info
    return None

if __name__ == '__main__':
    uoft_cs_code, uw_afm_code = '203', '301'
    uoft_cs = scrape(uoft_cs_code)
    print(json.dumps(uoft_cs, indent=2))
