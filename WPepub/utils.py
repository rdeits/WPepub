from unidecode import unidecode
from collections import namedtuple
import subprocess

Chapter = namedtuple('Chapter', ['title', 'url', 'content'])

def html2rst(html):
    # adapted from http://johnpaulett.com/2009/10/15/html-to-restructured-text-in-python-using-pandoc/
    p = subprocess.Popen(['pandoc', '--from=html', '--no-wrap', '--to=rst'],
                         stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    return unidecode(p.communicate(html)[0].decode('utf-8'))
