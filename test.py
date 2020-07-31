import cv2
import numpy as np
import requests
import io
import json
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get('http://www.knowyourcollege-gov.in/')
sleep(1)

driver.get_screenshot_as_file("captcha123.png")
driver.quit()
#add screenshot

img = cv2.imread('C:\\Users\\user\\Desktop\\knowyourcollege\\captcha.jpg')
height , width , _ = img.shape
#print(img)

#Cutting or Croping screenshot
roi = img[441:441+103, 987:987+163]
#using External OCR API 

url_api = "https://api.ocr.space/parse/image"
_, compressedimage = cv2.imencode(".jpg", roi, [1, 90])
file_bytes = io.BytesIO(compressedimage)

result = requests.post(url_api, files = {"captcha.jpg": file_bytes}, data = {"apikey": "19b169c2cf88957"})
result = result.content.decode()
result = json.loads(result)
#print(result)
text_detected = result.get("ParsedResults")[0].get("ParsedText")
print(text_detected)
cv2.imshow("roi", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
