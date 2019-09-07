from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
from urllib.request import Request

base_url = 'https://www.allmusic.com'

search_url = 'https://www.allmusic.com/search/artists/'

artist_name = "chi"

search_url+=artist_name

req = Request(search_url, headers={'User-Agent': 'Mozilla/5.0'})
results_html = uReq(req).read()

#html parsing
page_soup = BeautifulSoup(results_html, "html.parser")

#grabs all artists

print(len(containers))
while True:
    try {
        containers = page_soup.findAll("ul", {"class":"search-results"})
        artist_url = containers[0].div.a['href']
        print(artist_url)
        break
    }


artist_id = artist_url[-12:]
print(artist_id)

#artist_img = containers[0].div.img['src']
#print(artist_img)

related_url = base_url + artist_url + '/related'

req = Request(related_url, headers={'User-Agent': 'Mozilla/5.0'})
related_html = uReq(req).read()

page_soup = BeautifulSoup(related_html, "html.parser")
#containers = page_soup.findAll("li")
containers = page_soup.findAll("section", {"class":"related similars"})
#print(containers)
# print(containers)
# print(len(containers))
artist_list = []
#print(containers)
#print(len(containers))
for container in containers:
    #print(container)
    artist_return = container.findAll(text=True)

#print(artist_return)
for artist in artist_return:
#    print(str(artist))
#    print(type(str(artist)))
    artist_list.append(str(artist))

#print(artist_list)

fixed = []
for artist in artist_list:
    if artist != '\n' and artist != ' ' and artist != "Similar To":
        fixed.append(artist)

print(fixed)




# for container in containers:
#     print(container)
    #brand = container.find("div", "item-info")
    #brand = brand.div.a.img["title"]
    #print(brand)
    #title_container = container.findAll("a", {"class":"item-title"})
    #print(title_container)
    #product_name = title_container[0].text
    #print(product_name)
    #shipping_container = container.findAll("li", {"class":"price-ship"})
    #print(shipping_container)
    #shipping = shipping_container[0].text.strip()
    #print(shipping)
    #print()

    # counter_object = Counter.objects.get(pk=1)
    # counter_object.count += 1
    # counter_object.save()
