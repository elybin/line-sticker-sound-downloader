# import libraries
import urllib2
import re
import os
import unicodedata
from bs4 import BeautifulSoup
import subprocess

def slugify(value):
    """
    Normalizes string, converts to lowercase, removes non-alpha characters,
    and converts spaces to hyphens.
    """
    value = unicode(value)
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub('[^\w\s-]', '', value).strip().lower()
    return re.sub('[-\s]+', '-', value)

sticker_id = 8455


# specify the url
#quote_page = 'https://store.line.me/stickershop/product/8455/en' #tatan
quote_page = 'https://store.line.me/stickershop/product/' + str(sticker_id) + '/en'
# query the website and return the html to the variable 
page = urllib2.urlopen(quote_page)
# parse the html using beautiful soup and store in variable 
soup = BeautifulSoup(page, 'html.parser')

sticker_title = soup.find('title').text.encode('utf-8')
sticker_title = str(sticker_title).split('\xe2\x80\x93')[0]
sticker_title = slugify(sticker_title)


# Take out the <div> of name and get its value
name_box = soup.find('div', attrs={'class': 'mdCMN09ImgList'})

price_box = name_box.find('ul', attrs={'class':'mdCMN09Ul'})

# price_box = price_box.text

# print price_box

# 
links = price_box.find_all('span')

ids = [0]*len(links)
link_oke = [0]*len(links)

for x in xrange(0,len(links)):
	ids[x] = links[x].get('v-on:click')
	ids[x] = re.findall("\d+", ids[x])
	ids[x] = str(ids[x]).replace("[u'", "")
	ids[x] = str(ids[x]).replace("']", "")
	# put to link 
	link_oke[x] = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/' + ids[x] + '/IOS/sticker_sound.m4a;compress=true'
	pass


if(len(link_oke) > 7):
	for x in xrange(1,3):
		if(os.path.isdir(sticker_title) & os.path.exists(sticker_title) ):
			print "exist"
			#
			for y in xrange(0,len(links)):
				res = os.system("wget -O " + sticker_title + "/" + sticker_title + "_" + str(y) + ".m4a " + link_oke[y])
				

				print res
				res = os.system("faad -o " + sticker_title + "/" + sticker_title + "_" + str(y) + ".wav " + sticker_title + "/" + sticker_title + "_" + str(y) + ".m4a")
				
				# del m4a
				res = os.system("rm \""+ sticker_title + "/" + sticker_title + "_" + str(y) + ".m4a\"")

				pass
			

		else:
			print "n-exist"
			print "create..."
			os.mkdir(sticker_title)

		pass