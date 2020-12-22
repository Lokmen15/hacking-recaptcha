"""
python script that hacks the recaptcha test.

usage: 

    $ python3 main.py  

"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import urllib.request
import detection
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--port", help="set your port",type=int)
args = parser.parse_args()

link_to_natigate = "http://localhost:"+str(args.port)+"/"
button_submit_xpath = '//*[@id="root"]/div/div/div/button'


chrome_options =Options()
chrome_options.add_argument('--headless')
#setting the chromedriver.
browser = webdriver.Chrome(executable_path=r'./chromedriver')
browser.get(link_to_natigate)
#map  (dcitionnary in python ) to attach each name of image to its xpath so we can click on them later since the return of the detection 
# algorithm is a list of names of iimage that contain buses
map_imgname_xpath = {}
names=[]
xpth_target_list=[]
xpath_range = range(2, 11)


#downloading the images in the same folder.
for i in xpath_range :
    #diffrent xpaths 
    image =browser.find_element_by_xpath('//*[@id="root"]/div/div/div/div/ul/li['+str(i)+']/div/div/img')
    src=image.get_attribute('src') 
    urllib.request.urlretrieve(src, "captcha"+str(i)+".png")
    names.append("captcha"+str(i)+".png")
    # add key and value to map.
    map_imgname_xpath["captcha"+str(i)+".png"] = '//*[@id="root"]/div/div/div/div/ul/li['+str(i)+']/div/div/img'
    i+=1


## call the tensorflow model and get a list of names of images that contain bus/buses
# input : list of all images names in the directory
# output : list of images names with buses.
busImages=detection.get_bus(names)

# get the xpath of each image that contain buses using the map created before.
for image in busImages:
    xpth_target_list.append(map_imgname_xpath[image])
print(xpth_target_list)

#convert it to set to avoid clicking twice on a same picture.
xpth_target_set=set(xpth_target_list)

#clicking on each of the xpaths in the list
for xpth in xpth_target_set:
    element = browser.find_element_by_xpath(xpth)
    element.click()
    print('clicked on '+ str(xpth))



#click on the submit button with it's own xpath.
element = browser.find_element_by_xpath(button_submit_xpath)
element.click()

