#Recaptche passing using selenium and object detection

This script dowload automaticly the images of recaptcha. Passes the images to a model which detects whether there's a bus or not

After this using selenium we control the browser and select the right images and click on submit button.


We are using selenium with Google Chrome, so we need a chromedriver. Please check the exact version of your chrome and download the right 

chrome driver from this page: https://chromedriver.chromium.org/downloads

Also please download the RetinaNet model file that will be used for object detection via this:

https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/resnet50_coco_best_v2.0.1.h5

system info:

- ubuntu 18.04

- python 3.6.9

-

## Installing
use a virtual env: 
```bash
python3 -m venv yourvenv
```
update pip:
```bash
pip install --upgrade pip
```
install requirements:
```bash
pip3 install -r requirements
```



## usage
```bash
python3 main.py --port YOURPORT
```




