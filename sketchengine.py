# -*- coding: utf-8 -*-

from mechanicalsoup import StatefulBrowser
from pyf import map


def concordance(*, query: str):
    """
    >>> from sketchengine import concordance
    >>> concordance('feet')[0]
    'The "widow boats" averaged 15 feet.'
    """
    url = 'https://skell.sketchengine.co.uk/run.cgi/concordance?lpos=&query={}'
    browser = StatefulBrowser()
    browser.open(url.format(query))
    tbody = browser.get_current_page().select('#conc_content tbody tr')

    return tbody | map(lambda x: ''.join(x.findAll('td')[1].text.strip().splitlines()))


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)