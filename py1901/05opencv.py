#파이썬에서 이미지 다루기
#opencv (computer vision library)
#이미지 데이터 관련 작업(이미지 선명화, 픽셀화 등등)을 기계적으로 수행할 수 있도록 도와주는 라이브러리
#주로 이미지를 통한 얼굴인식, 장애물인식, 객체 인식에 사용
#딥러닝을 통한 이미지 인식에 널리 사용되고 있음
#심지어 영상처리를 이용한 객체 인식에도 사용됨

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import cv2
from PIL import Image

#C:\Users\TJ\Pictures\Saved Pictures

#그레이스케일로 이미지 출력하기
#imread(그림파일, 읽어올 방식)
# img = cv2.imread('C:/Users/TJ/Pictures/Saved Pictures/test.png', cv2.IMREAD_GRAYSCALE) #흑백으로 읽기
# print(type(img)) #이미지 객체의 유형 확인
# print(img) #이미지의 픽셀값 확인
# print(img.shape) #이미지의 크기 확인
# print(img[0,0]) #이미지의 첫번째 픽셀값 확인
#
# plt.imshow(img, cmap='gray')
# plt.axis('off')
# plt.show()
#
# img = cv2.imread('C:/Users/TJ/Pictures/Saved Pictures/test.png', cv2.IMREAD_COLOR) #IMREAD_COLOR는 BGR형식으로 픽셀 저장
# print(type(img)) #이미지 객체의 유형 확인
# print(img) #이미지의 픽셀값 확인
# print(img[0],[0])
# print(img.shape) #이미지의 크기 확인
# print(img[0,0]) #이미지의 첫번째 픽셀값 확인
#
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# plt.imshow(img, cmap='gray')
# plt.axis('off')
# plt.show()

#이미지 픽셀화 예제

#파이썬에서 이미지 다루기 2 - PIL (pillow)
# 또 다른 이미지 관련 패키지로 Pillow가 있는데 파이썬 버전에
# 여러가지 이미지 형식을 다룰 수 있게 해주고
# 이미지 내부 데이터에 접근, 다양한 이미지 처리 기능을 지원하고 있음.

#이미지 픽셀화 예제
img = Image.open('C:/Users/TJ/Pictures/Saved Pictures/tower.jpg')
# pixels = img.getdata()
# print(img.size)
# print(np.array(pixels)) #픽셀을 numpy 배열로 변환

# img.show()

# plt.imshow(img)
# plt.axis('off')
# plt.show()


#그레이스케일 변환
# gsimg = img.convert('L')
# pixels = gsimg.getdata()
# print(np.array(pixels))

# gsimg.show()

#이미지를 16x16 크기의 배열로 만든후 출력함
#이미지 흑백 전환은 average hash기법을 사용함
#즉, 255의 평균값을 기준으로 평균보다 작으면 0, 평균보다 크면 1로 설정

# imgsize = 31
# gsimg = gsimg.resize((imgsize, imgsize), Image.ANTIALIAS)
# #이미지 크기 재조정 및 부드럽고 매끈하게 처리
#
# pixel_data = gsimg.getdata()
# pixel_data = np.array(pixel_data)
# pixels = pixel_data.reshape(imgsize, imgsize) #픽셀들을 31 x 31 크기로 재조정
#
# avg = pixels.mean() #픽셀의 평균을 구하고
# diff = 1*(pixels > avg) #평균보다 크면 1, 아니면 0
# print(diff)
# gsimg.show()

# 이미지 픽셀화 예제
img = cv2.imread('C:/Users/TJ/Pictures/Saved Pictures/test.png', cv2.IMREAD_COLOR)  #이미지를 BGR로 불러오기
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # RGB로 변환

#plt.imshow(img)
#plt.axis('off')
#plt.show()

# 흑백(greyscale)로 변환

img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
#
# plt.imshow(img)
# plt.axis('off')
# plt.show() # 그냥 바꾸면 색깔이 이상하게 나온다

# plt.imshow(img, cmap='gray')
# plt.axis('off')
# plt.show() # cmap(colormap)을 gray로 고쳐줌

# 이미지 축소

img32 = cv2.resize(img, (32, 32))
img64 = cv2.resize(img, (64, 64))
img128 = cv2.resize(img, (128, 128))
img256 = cv2.resize(img, (256, 256))
#resize(대상, (가로크기, 세로크기))
# 32, 64, 96, 128, 256

# 축소한 이미지 출력
plt.imshow(img32, cmap='gray')
plt.axis('off')
plt.show()

avg = img32.mean()
diff = 1 * (img32 > avg)
# average hash 방식을 이용해서 픽셀을 0/1로 변환

plt.imshow(diff, cmap='gray')
plt.axis('off')
plt.show()

avg = img128.mean()
diff = 1 * (img128 > avg)
# average hash 방식을 이용해서 픽셀을 0/1로 변환

plt.imshow(diff, cmap='gray')
plt.axis('off')
plt.show()


avg = img256.mean()
diff = 1 * (img256 > avg)
# average hash 방식을 이용해서 픽셀을 0/1로 변환

plt.imshow(diff, cmap='gray')
plt.axis('off')
plt.show()

avg = img256.mean()
diff = 1 * (img256 > avg)
# average hash 방식을 이용해서 픽셀을 0/1로 변환

plt.imshow(img256, cmap='gray')
plt.axis('off')
plt.show()

np.set_printoptions(edgeitems=30, linewidth=100000)
print(img32)