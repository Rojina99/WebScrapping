import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'

#Opening up the connection, grabbing the page
uClient = uReq(my_url)
#Offloads the content into the variable
page_html = uClient.read()
#Close connection request
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")

# print(page_soup.h1)

# print(page_soup.p)

# print(page_soup.body.span)

#Find all the div with object class having name item-container
#Grabs each product
containers = page_soup.findAll("div", {"class": "item-container"})
# print(containers)

len(containers)

# print(containers[0])
# print(containers[1])

# container = containers[0]

#div tag inside of div tag of container, a tag inside div tags , image tag inside a tag and title is attribute inside a
# container.div.div.a.img["title"]

filename = "D:/Pycharm PRoject/Web Scrapping/data/newegg/products.csv"
f = open(filename, "w")
headers = "brand,product_name,shipping\n"
f.write(headers)
count = 0
for container in containers:
    try:
        brand = container.div.div.a.img["title"]
        title_container = container.findAll("a", {"class": "item-title"})
        product_name = title_container[0].text
        shipping_container = container.findAll("li", {"class": "price-ship"})
        #strip() removes all whitespaces, newline,.. before-after text
        shipping = shipping_container[0].text.strip()
    except Exception as e:
        print("No value", str(e))
        continue

    print("brand",brand)
    print("product_name",product_name)
    print("shipping",shipping)
    count+=1
    print(count)

    #Replace string , by |
    #Write takes only one value so '+' insted of ','
    f.write(brand+","+product_name.replace(",","|")+","+shipping+"\n")

#close file so that you can open it otherwise not
f.close()








