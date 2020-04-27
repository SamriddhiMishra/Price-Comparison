import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
def AmazonItemName(item):
    amazon_item=item.split()
    amz=''
    for i in range(len(amazon_item)):
        amz=amz+amazon_item[i]+'+'
    amz=amz[:-1]
    return amz
print("ENTER THE CHOICE")
print("ONLY MOBILES TABLETS LAPTOPS OTHER OS DEVICES ARE VALID")
item=input()
driver = webdriver.Chrome(executable_path=r"C:\Users\samriddhi mishra\Desktop\ssss\chromedriver.exe")
#FLIPKART FROM HERE
driver.get('https://www.flipkart.com')
driver.get('https://www.flipkart.com/search?q={}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'.format(item))
flipkart_price = driver.find_elements_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "_1vC4OE", " " ))]')
fp=[]
for i in flipkart_price:
    fp.append(i.text)
flipkart_name = driver.find_elements_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "_3wU53n", " " ))]')
if(len(flipkart_name)==0):
    flipkart_name = driver.find_elements_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "_2B_pmu", " " ))]')
    if(len(flipkart_name)==0):
        flipkart_name = driver.find_elements_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "_2cLu-l", " " ))]')

    
fn=[]
for i in flipkart_name:
    fn.append(i.text)

#AMAZON FROM HERE
driver.get('https://www.amazon.com')
amazon_item=AmazonItemName(item)
driver.get('https://www.amazon.in/s?k={}&ref=nb_sb_noss_2'.format(amazon_item))
amazon_price = driver.find_elements_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "a-price-whole", " " ))]')

amazon_name = driver.find_elements_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "a-size-medium", " " ))]')
if(len(amazon_name)==0):
    amazon_name = driver.find_elements_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "s-line-clamp-1", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "a-color-base", " " ))]')
    if(len(amazon_name)==0):
        amazon_name = driver.find_elements_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "a-size-base-plus", " " ))]')
        if(len(amazon_name)==0):
            amazon_name = driver.find_elements_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "a-color-base", " " )) and contains(concat( " ", @class, " " ), concat( " ", "a-text-normal", " " ))]')
                                        

ap=[]
for i in amazon_price:
    ap.append(i.text)    
an=[]
for i in amazon_name:
    an.append(i.text)

    #fp ---> list of flipkart price
    #ap ---> list of amazon price
    #fn ---> list of flipkart name
    #an ---> list of amazon name
    
print(ap) #list of amazon price
print(an) #list of amazon name
print(fp) #list of flipkart price
print(fn) #list of flipkart name
