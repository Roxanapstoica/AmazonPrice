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
import lxml
import smtplib

# URL = "https://www.amazon.com/dp/B01NBKTPTS?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
URL = "https://www.yves-rocher.ro/apa_de_parfum_sel_dazur_100ml_pn"

# URL = "https://www.google.ro"
# URL = "https://www.amazon.com/dp/B09C8ZTJZJ/ref=twister_B0CBSTLB28?_encoding=UTF8&th=1"
USER_AGENT = "User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
ACCEPT_LANGUAGE = "en-US,en;q=0.9"

TARGET_PRICE = 5000

headers = {
    'Accept-Language': ACCEPT_LANGUAGE,
    'User-Agent':'Defined',
    'Cookie': "PHPSESSID=d646dab3bba3752a728f935bb50aabd2; _ga=GA1.2.2112563536.1696157177; _gid=GA1.2.940917246.1697955090; _ga_VL41109FEB=GS1.2.1697955089.7.0.1697955089.0.0.0"
    }

## passing headers in our request
response = requests.get(url=URL)
print(response)
webpage = response.text
# print(webpage)

soup = BeautifulSoup(webpage, 'lxml')
# print(soup)
# product_price = soup.select("div div span span")
# product_price = soup.find(name="div", class_="a-section a-spacing-micro")
# product_price_span = product_price.find(name="span", class_="a-price-whole")
# product_price = soup.find_all(name="span")
# # product_price = soup.select(".a-price[data-a-size=xl]")
# # product_price = soup.find(name="div",id="apex_offerDisplay_desktop")
product_price = soup.find(name="p",class_="product-new-price").getText()
product_price = product_price.split('Lei')[0]
product_price = product_price.replace('.','')
product_price = product_price.replace(' ','')
product_price = product_price.replace(',','.')
print(product_price)
print("****************")
print(type(product_price))
#
product_price_float = float(product_price)
product_title = soup.find(name="h1",class_="page-title")
product_title = product_title.getText()
#
# print("Title este: ",product_title)

### cand product_price_float <= TARGET_PRICE >> trimit email notificare

my_email = "testing.stuff443@gmail.com"
password = "kimuiopgizgflalx"

if product_price_float <= TARGET_PRICE:

    with smtplib.SMTP("smtp.gmail.com") as connection:

        connection.starttls() #encrypts the message, secures the message
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="roxana.p.stoica@gmail.com",
                            msg=f"Subject:Alerta pret {product_title}\n\nPretul la produsul: {product_title} \n\n"
                                f"a scazut, acum este {product_price_float} Lei\n\n"
                                f"Cumpara aici: {URL}"
                            )

