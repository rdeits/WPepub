This is a simple set of scripts I put together to generate an ePub edition from a wordpress blog, specifically <http://parahumans.wordpress.com/>. To run it, just do `rake` in the root directory, and it will assemble the final book as `build/out.epub`. 

Requirements:

* python 2.7
* BeautifulSoup
* [unidecode](https://pypi.python.org/pypi/Unidecode/)
* [txt2epub](https://github.com/mfrasca/txt2epub)

