import subprocess
import os
from bs4 import BeautifulSoup
from collections import namedtuple
from unidecode import unidecode

def WP_scrape():
    Chapter = namedtuple('Chapter', ['title', 'url', 'content'])

    def html2rst(html):
        # adapted from http://johnpaulett.com/2009/10/15/html-to-restructured-text-in-python-using-pandoc/
        p = subprocess.Popen(['pandoc', '--from=html', '--no-wrap', '--to=rst'],
                             stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        return unidecode(p.communicate(html)[0].decode('utf-8'))

    # Pull down a single episode in order to extract the TOC
    page_content = subprocess.check_output(['curl', 'http://parahumans.wordpress.com/category/stories-arcs-1-10/arc-4-shell/4-x-interlude/'])

    soup = BeautifulSoup(page_content)

    categories = soup.find_all(attrs={"class":"widget_categories"})[0]
    groups = categories.contents[2]

    lis = groups.find_all("li")
    chapters = []
    for li in lis:
        if li.li is None:
            print li.a.contents[0], li.a.get('href')
            url = li.a.get('href')
            mirror_path = os.path.join(url.replace('http://parahumans.wordpress.com', '../mirror'),'index.html')
            mirror_path = mirror_path.encode('ascii', 'ignore')
            os.system('mkdir -p ' + os.path.split(mirror_path)[0])
            with open(mirror_path, 'w') as f:
                f.write(subprocess.check_output(['curl', url]))

            # chapters.append(Chapter(title=li.a.contents[0], url=li.a.get('href'), content=''))

    # chapters = [Chapter(title=c.title, url=c.url, content=BeautifulSoup(subprocess.check_output(['curl', c.url]))) for c in chapters]

    # for c in chapters:
    #     display_title = unidecode(c.content.find_all(attrs={'class':'entry-title'})[0].get_text())
    #     fname = c.title + ' ' + display_title
    #     fname = fname.replace(' ', '_')
    #     f = open('../rst/' + fname + '.rst', 'w')
    #     f.write("{}\n{}\n".format(display_title,'='*(len(display_title))))
    #     text = html2rst(str(c.content.find_all("div", attrs={'class':'entry-content'})[0]))
    #     text = '\n'.join(text.splitlines()[1:-1])
    #     f.write(text)
    #     f.close()

if __name__ == '__main__':
    WP_scrape()
