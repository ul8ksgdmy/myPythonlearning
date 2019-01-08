# 얼굴이미지 인식 예제
from sklearn.datasets import fetch_lfw_people
from matplotlib import pyplot as plt

faces = fetch_lfw_people(min_faces_per_person=100)
print(faces.target_names)
print(faces.images.shape)

fig, ax = plt.subplots(3, 5) # 그래프 영역을 3 x 5로 설정
for i, axi in enumerate(ax.flat):
    # axi.imshow(faces.images[i], cmap='bone') # 청색
    axi.imshow(faces.images[i], cmap='gray') # 흑백
    axi.set(xticks=[], yticks=[]) # x/y축 제거
    facename = faces.target_names[faces.target[i]]
    axi.set_xlabel(facename) #facename
plt.show()