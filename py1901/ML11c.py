# 고유얼굴 특성 추출을 이용한 PCA 순석
# 특성추출 : 원본 데이터를 있는 그대로 표현하기보다 분석하기에 적합하도록 표현하는 방식
# 이미지를 다루는 분야에서 특성추출이 자주 사용됨.
# LFW 데이터 셋의 얼굴 이미지에서 특성 추출
# LFW - 유명인사들의 얼굴 이미지로 2000년 초반이후 정치인, 가수, 배우, 운동선수 등이 포함 (62명, 3023개)
import numpy as np
from sklearn.datasets import fetch_lfw_people
import matplotlib.pyplot as plt

people = fetch_lfw_people(min_faces_per_person=20, resize=0.7)
people_shape = people.images[0].shape

fig, axes = plt.subplots(2,5, figsize=(15, 8), subplot_kw={'xticks':(), 'yticks':()})
for target, image, ax, in zip(people.target, people.images, axes.ravel()):
    ax.imshow(image, cmap='gray')
    ax.set_title(people.target_names[target])
plt.show()

print('사진 크기', people_shape) # (87, 65)
print('사진 종류', len(people.target_names))

cnt = np.bincount(people.target)
for i, (count, name) in enumerate(zip(cnt, people.target_names)):
    print('{0:25} {1:3}'.format(name, count), end='        ')
    if (i+1) % 3 == 0: print() # 3번 째 데이터는 줄바꿈 후 출력

# 위에서 볼 수 있듯이 조지부시 사진이 530개로 가장 많음
# 그 뒤로 파웰은 236개, 럼스펠트가 121개의 사진이 있음.
# 데이터셋의 편중을 없애기 위해 사람별로 50개 이하의 이미지만 선택함.

mask = np.zeros(people.target.shape, dtype=np.bool)
for target in np.unique(people.target):
    mask[np.where(people.target == target)[0][:50]] = 1

X_people = people.data[mask]
y_people = people.target[mask]

X_people = X_people / 255 #칼라 이미지를 흑백이미지로 변환

# k최근접이웃 분석법으로 손글씨 인식 예제를 실행했듯이 얼굴인식 분석을 k최근접이웃 분석기법을 사용해 봄.
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

Xtrain, Xtest, ytrain, ytest = train_test_split(X_people, y_people, random_state=0)
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(Xtrain, ytrain)
print('정확도', knn.score(Xtest, ytest))


