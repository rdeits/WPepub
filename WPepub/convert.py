import os
from bs4 import BeautifulSoup
from unidecode import unidecode
from utils import html2rst, Chapter

def WP_convert():
    # Pull down a single episode in order to extract the TOC
    with open("../mirror/category/stories-arcs-1-10/arc-1-gestation/1-01/index.html", 'r') as f:
        page_content = f.read()

    soup = BeautifulSoup(page_content)

    categories = soup.find_all(attrs={"class":"widget_categories"})[0]
    groups = categories.contents[2]

    lis = groups.find_all("li")
    chapters = []
    for li in lis:
        if li.li is None:
            print li.a.contents[0], li.a.get('href')
            url = li.a.get('href')
            mirror_path = os.path.join(url.replace('http://parahumans.wordpress.com', '../mirror'), 'index.html')
            mirror_path = mirror_path.encode('ascii', 'ignore')
            if 'arc-29' in mirror_path:
                break
            with open(mirror_path, 'r') as f:
                content = BeautifulSoup(f.read())
            chapters.append(Chapter(title=li.a.contents[0], url=url, content=content))

    for c in chapters:
        display_title = unidecode(c.content.find_all(attrs={'class':'entry-title'})[0].get_text())
        fname = c.title + ' ' + display_title
        fname = fname.replace(' ', '_').replace('/', '-')
        if len(fname.split('.')[0]) == 1:
            fname = '0' + fname
        f = open('../rst/' + fname + '.rst', 'w')
        f.write("{}\n{}\n".format(display_title,'='*(len(display_title))))
        text = html2rst(str(c.content.find_all("div", attrs={'class':'entry-content'})[0]))
        text = '\n'.join(text.splitlines()[1:-1])
        f.write(text)
        f.close()

if __name__ == '__main__':
    WP_convert()
