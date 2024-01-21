# unlock-image-feeling-AI
한 명의 표정이 보이는 이미지를 넣으면 5가지의 감정으로 분석하는 AI\
감정 종류 : 기쁨, 당황, 분노, 슬픔, 중립\
정확도 : 56~57%

## 사용법
### CNN_faceFeelingAI_train_test.ipynb
훈련하고 정확도를 알 수 있는 테스트를 한 파일입니다.
### faceFeelingAI_demonstration.py
- 동영상이 있는 경로를 input하면 이미지로 나눠 폴더를 만들어 저장합니다. (폴더가 안 만들어지는 버그가 있다면 동영상 이름과 똑같은 폴더를 미리 만들고 실행해주세요.)
- 동영상이 아닌 이미지를 분석하고 싶다면 아래와 같이 동영상 경로를 넣는 곳을 주석처리하고 path에 바로 이미지가 있는 **폴더명**을 입력해주세요.
```python
# file = input("동영상 경로명을 입력하세요 : ")
path = "image folder"
```

## Data 출처
AIHub 한국인 감정인식을 위한 복합 영상 (링크 : https://www.aihub.or.kr/mypage/reqst/datareqst/view.do?currMenu=157&topMenu=106&dataReqstSn=364151)
