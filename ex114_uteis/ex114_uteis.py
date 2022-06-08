import urllib
import urllib.request


def test_site(msg):
    try:
        site = urllib.request.urlopen(msg)
    except urllib.error.URLError:
        print('\033[0;31mO site não está acessivel.\033[m')
    else:
        print('\033[0;32mO site está acessivel\033[m')

