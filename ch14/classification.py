import torch
from torchvision import models, transforms
from PIL import Image
from torchvision.models import ResNet18_Weights

# 사전 훈련된 ResNet 모델 불러오기
weights = ResNet18_Weights.IMAGENET1K_V1  # 훈련된 ResNet18 모델의 가중치를 가져옴
model = models.resnet18(weights=weights)  # ResNet18 모델을 불러옴, 해당 가중치를 적용
model.eval()  # 모델을 평가 모드로 설정

# 이미지 변환
preprocess = transforms.Compose([
    transforms.Resize(256),  # 이미지 크기를 256x256으로 조정
    transforms.CenterCrop(224),  # 중앙에서 224x224 크기로 자름 (ResNet 입력 사이즈)
    transforms.ToTensor(),  # 이미지를 PyTorch 텐서로 변환 (픽셀 값을 [0,1] 범위로 정규화)
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]), 
])

# 이미지 로드 및 전처리
image = Image.open("tiger.jpg")  # 'tiger.jpg'라는 이미지 파일을 열고 PIL 형식으로 저장
input_tensor = preprocess(image)  # 이미지에 대해 미리 정의한 전처리 과정을 수행
input_batch = input_tensor.unsqueeze(0)  # 배치 차원을 추가

# 이미지 분류
with torch.no_grad():  # 역전파 계산을 비활성화하여 메모리 및 연산 속도를 최적화
    output = model(input_batch)  # 전처리된 이미지를 모델에 입력하고 결과를 얻음

# 결과 출력 (가장 높은 확률의 클래스)
_, predicted = torch.max(output, 1)  # 모델의 예측 결과 중 가장 높은 확률의 클래스를 선택

# ImageNet 클래스 레이블 얻기
labels = weights.meta["categories"]  # ImageNet 클래스의 레이블 목록을 가져옴
predicted_label = labels[predicted.item()]  # 예측된 클래스에 해당하는 레이블을 가져옴
print(f"Predicted class: {predicted.item()} ({predicted_label})")  # 예측된 클래스 번호와 해당 레이블을 출력