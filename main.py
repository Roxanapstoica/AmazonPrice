### 1 ###
### Find a product on Amazon that you want to track and get the product URL
### In addition to the URL, when your browser tries to load up a page in Amazon,
# it also passes a bunch of other information. e.g. Which browser you're using,
# which computer you have etc. These additional pieces of information are passed along
# in the request Headers.

### 2 ###
### Use the requests library to request the HTML page of the Amazon product using
# the URL you got from 1. You'll need to pass along some headers in order for the request
# to return the actual website HTML. # At minimum you'll need to give your "User-Agent" and
# "Accept-Language" values in the request header.
## how you pass headers with the requests library:
## https://stackoverflow.com/questions/6260457/using-headers-with-the-python-requests-librarys-get-method

import requests
from bs4 import BeautifulSoup

# URL = "https://www.amazon.com/dp/B01NBKTPTS?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
# URL = "https://www.google.ro"
URL = "https://www.amazon.com/dp/B09C8ZTJZJ/ref=twister_B0CBSTLB28?_encoding=UTF8&th=1"
USER_AGENT = "User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
ACCEPT_LANGUAGE = "en-US,en;q=0.9"

headers = {
    'Accept-Language': ACCEPT_LANGUAGE,
    'User-Agent':'Defined',
    }

## passing headers in our request
response = requests.get(url=URL,headers=headers)

print(response)
webpage = response.text
print(webpage)

soup = BeautifulSoup(webpage, 'lxml')




