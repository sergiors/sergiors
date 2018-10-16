# -*- coding: utf-8 -*-

from mechanicalsoup import StatefulBrowser
from pyf import map


def concordance(word: str):
    url = 'https://skell.sketchengine.co.uk/run.cgi/concordance?lpos=&query={}'
    browser = StatefulBrowser()
    browser.open(url.format(word))
    tbody = browser.get_current_page().select('#conc_content tbody tr')

    return tbody | map(lambda x: ''.join(x.findAll('td')[1].text.strip().splitlines()))