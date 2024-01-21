# unlock-image-feeling-AI
한 명의 표정이 보이는 이미지를 넣으면 5가지의 감정으로 분석하는 AI\
감정 종류 : 기쁨(Happy), 당황(Panic), 분노(Angry), 슬픔(Sad), 중립(expressionless)\
정확도(Accuracy) : 56~57%

## 사용법
### CNN_faceFeelingAI_train_test.ipynb
모델을 훈련하고 모델의 정확도를 알 수 있는 테스트를 한 파일입니다.\
This is a file that trained the model and tested it to know the accuracy of the model.
### faceFeelingAI_demonstration.py
- 동영상이 있는 경로를 input하면 이미지로 나눠 폴더를 만들어 저장합니다. (폴더가 안 만들어지는 버그가 있다면 동영상 이름과 똑같은 폴더를 미리 만들고 실행해주세요.)\
When you enter the path where the video is located, you create a folder and store the video in it by dividing it into images. (If there is a bug that does not create a folder, please make a folder with the same name as the video in advance and run it.)
- 동영상이 아닌 이미지를 분석하고 싶다면 아래와 같이 동영상 경로를 넣는 곳을 주석처리하고 path에 바로 이미지가 있는 **폴더명**을 입력해주세요.\
If you want to analyze an image other than a video, please annotate the video path as below and enter **the folder name** with the image directly in the path.
```python
# file = input("동영상 경로명을 입력하세요 : ")
path = "image folder"
```
- 윈도우 운영체제인 경우 그래프의 한글이 깨질 수 있습니다. 'AppleGothic'을 'Malgun Gothic'으로 수정해주세요. 그래도 한글이 깨진다면 컴퓨터에 설치된 한글 폰트체를 직접 찾아 수정해야합니다.\
If it is a Windows operating system, Hangul in the graph may be broken. Please change 'AppleGothic' to 'MalgunGothic'. Still, if Hangul is broken, you have to find and modify the Hangul font installed on your computer.
```python
plt.rcParams['font.family'] = 'Malgun Gothic'
```

## Data 출처
AIHub 한국인 감정인식을 위한 복합 영상 (링크 : https://www.aihub.or.kr/mypage/reqst/datareqst/view.do?currMenu=157&topMenu=106&dataReqstSn=364151)
