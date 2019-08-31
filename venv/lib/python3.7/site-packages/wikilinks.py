#!/usr/bin/env python
# -*- coding: utf8 -*-

import re
import time
import codecs
import optparse

from six.moves.urllib.parse import urlencode
from six.moves.urllib.request import urlopen, Request

LANGS = [
    "ar", "bg", "ca", "cs", "da", "de", "el", "en", "eo", "es",
    "eu", "fa", "fi", "fr", "he", "hu", "id", "it", "ja", "ko",
    "lt", "ms", "nl", "no", "pl", "pt", "ro", "ru", "sk", "sl",
    "sv", "tr", "uk", "vi", "vo", "zh"
]

def wikilinks(site, langs=LANGS, page_size=500, offset=0, retries=5):
    """
    wikilinks is a generator that returns a source, target tuples where source 
    is the url for a document at wikipedia and target is a url for a document 
    at a given site. Use the langs parameter to control what language wikipedias
    are consulted. By default it will look at all of them.
    """
    for lang in langs:
        if lang not in LANGS:
            raise Exception("invalid language code %s" % lang)

    for lang in langs:
        links_url = 'https://%s.wikipedia.org/w/index.php?title=Special:LinkSearch&target=%s&limit=%s&offset=%s'
        wikipedia_host = 'https://%s.wikipedia.org' % lang
        while True:
            url = links_url % (lang, site, page_size, offset)
            html = codecs.decode(_fetch(url), 'utf8')
            found = 0
            for line in html.split("\n"):
                m = re.search('<li><a class="external".+?href="([^"]+)".+?<a href="(/wiki/[^"]+)"', line)
                if m:
                    found += 1
                    yield wikipedia_host + m.group(2), m.group(1)  

            if found == page_size:
                offset += page_size
            else:
                break


def _fetch(url, params=None, retries=5):
    if params:
        req = Request(url, data=urlencode(params))
        req.add_header('Content-type', 'application/x-www-form-urlencoded; charset=UTF-8')
    else:
        req = Request(url)
    req.add_header('User-agent', 'wikipedialinks v0.2')

    try:
        return urlopen(req).read()
    except URLError as e:
        return _fetch_again(e, url, params, retries)
    except urllib2.HTTPError as e:
        return _fetch_again(e, url, params, retries)


def _fetch_again(e, url, params, retries):
        retries -= 1
        if retries == 0:
            raise e
        else: 
            time.sleep(10)
            return _fetch(url, params, retries)

def main():
    parser = optparse.OptionParser("wikilinks url")
    parser.add_option('-l', '--lang', type='string', help='language wikipedias to search: e.g. en')
    opts, args = parser.parse_args()
    if opts.lang:
        langs = opts.lang.split(',')
    else:
        langs = LANGS
    if len(args) != 1:
        parser.error('please supply url to search for')
    site = args[0]
    for link in wikilinks(site, langs=langs):
        print('\t'.join(link))

if __name__ == '__main__':
    main()

