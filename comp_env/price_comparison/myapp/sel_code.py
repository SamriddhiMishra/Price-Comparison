import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .models import amfp

def AmazonItemName(item):
    amazon_item = item.split()
    amz = ''
    for i in range(len(amazon_item)):
        amz = amz + amazon_item[i] + '%20'
    amz = amz[:-1]
    return amz


def Sort_Tuple(tup):
    lst = len(tup)
    for i in range(0, lst):
        for j in range(0, lst - i - 1):
            a=((tup[j][1]).strip()).replace(',','')
            b=((tup[j+1][1]).strip()).replace(',','')
            if(a[0]=='R'):
                a=int(a[3:])
                b=int(b[3:])
            else:
                a=int(a[1:])
                b=int(b[1:])
            if (a > b):
                temp = tup[j]
                tup[j] = tup[j + 1]
                tup[j + 1] = temp
    return tup

def compare(item):
    driver = webdriver.Chrome(
        executable_path=r"C:\Users\samriddhi mishra\Documents\Projects\price_comparison\comp_env\price_comparison\myapp\chromedriver.exe")
    # FLIPKART FROM HERE
    driver.get('https://www.flipkart.com')
    driver.get(
        'https://www.flipkart.com/search?q={}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'.format(
            item))
    flipkart_price = driver.find_elements_by_xpath(
        '//*[contains(concat( " ", @class, " " ), concat( " ", "_1vC4OE", " " ))]')
    fp = []
    for i in flipkart_price:
        fp.append(i.text)
    flipkart_name = driver.find_elements_by_xpath(
        '//*[contains(concat( " ", @class, " " ), concat( " ", "_3wU53n", " " ))]')
    if (len(flipkart_name) == 0):
        flipkart_name = driver.find_elements_by_xpath(
            '//*[contains(concat( " ", @class, " " ), concat( " ", "_2B_pmu", " " ))]')
        if (len(flipkart_name) == 0):
            flipkart_name = driver.find_elements_by_xpath(
                '//*[contains(concat( " ", @class, " " ), concat( " ", "_2cLu-l", " " ))]')

    fn = []
    for i in flipkart_name:
        fn.append(i.text)

    # AMAZON FROM HERE
    amazon_item = AmazonItemName(item)
    # name = driver.find_element_by_xpath('//input');
    # name.sendKeys("{}".format(item));
    # WebElement login = driver.findElement(By.id("SubmitLogin"));
    # login.click()
    driver.get('https://paytm.com/shop/search?q={}&from=organic&child_site_id=1&site_id=1'.format(amazon_item))
    amazon_item = AmazonItemName(item)
    amazon_price = driver.find_elements_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "_1kMS", " " ))]')

    amazon_name = driver.find_elements_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "_2apC", " " ))]')

    ap = []
    for i in amazon_price:
        ap.append(i.text)
    an = []
    for i in amazon_name:
        an.append(i.text)


        # fp ---> list of flipkart price
        # ap ---> list of amazon price
        # fn ---> list of flipkart name
        # an ---> list of amazon name

    # print(ap) #list of amazon price
    # print(an) #list of amazon name
    # print(fp) #list of flipkart price
    # print(fn) #list of flipkart name


    if(len(fp)<len(fn)):
        m=len(fp)
    else:
        m=len(fn)
    if (len(ap) < len(an)):
        n = len(ap)
    else:
        n = len(an)
    ff=[(fn[i], fp[i]) for i in range(0, m)]
    aa=[(an[i], ap[i]) for i in range(0, n)]
    aa=Sort_Tuple(aa)
    ff=Sort_Tuple(ff)

    for i in range(n):
        an[i]=aa[i][0]
        ap[i] = aa[i][1]
    for i in range(m):
        fn[i]=ff[i][0]
        fp[i] = ff[i][1]

    if (n < m):
        m = n
    else:
        m = m

    for i in range(m):
        f = amfp(aprod=an[i], aprice=ap[i], fprod=fn[i], fprice=fp[i])
        f.save()



