import cv2
import os
#from google.colab.patches import cv2_imshow

def fileOpen(filepath):
    video = cv2.VideoCapture(filepath) # 사용할 비디오 파일의 경로 및 이름을 넣어주도록 함

    if not video.isOpened(): # 비디오가 열리지 않으면 프로그램 종료
        print("Could not Open :", filepath)
        exit(0)

    #불러온 비디오 파일의 정보 출력
    length = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video.get(cv2.CAP_PROP_FPS)
    # CAP_PROP_POS_MSEC 밀리초 단위로 현재 위치
    print('밀리초 단위로 현재 위치 :', video.get(cv2.CAP_PROP_POS_MSEC))

    print("length :", length) # 프레임 총 개수 = 418초 x 23.976023fps
    print("width :", width)
    print("height :", height)
    print("fps :", fps)
    print("")
    return filepath, video

# t / 10 초 (t=1이면 0.1초)
def time(t):
  h = 0
  m = 0
  s = t // 10
  ss = t % 10

  if s >= 60:
    m = t // 60
    s = t % 60
  if m >= 60:
    h = m // 60
    m = m % 60

  return (f'{h:0>2}:{m:0>2}:{s:0>2}.{ss}')

# 동영상 t / 10초씩 잘라 저장하기
def imageSave(filepath, t):
    filepath, video = fileOpen(filepath)

    #프레임을 저장할 디렉토리를 생성
    try:
        if not os.path.exists(filepath[:-4]):
            os.makedirs(filepath[:-4])
    except OSError:
        print ('Error: Creating directory. ' +  filepath[:-4])
        exit(0)


    count = t
    
    while True:
      success, image = video.read()
      
      if success == False:
          break
      
      if (int(video.get(cv2.CAP_PROP_POS_MSEC)/ 100)) == count:
        tt = time(count)
        cv2.imwrite(filepath[:-4] + f"/time{tt}.jpg", image)
        print(f"\nsaved image {tt}.jpg")
        #print('밀리초 단위로 현재 위치 :', video.get(cv2.CAP_PROP_POS_MSEC))
        print('초 단위로 현재 위치 :', video.get(cv2.CAP_PROP_POS_MSEC)/1000)

        if cv2.waitKey(10) == 27:  # esc키 누르면 종료
            break
        count += t
        
        # 일단 이미지 20개 저장되면 종료되게
        if count == 210:
            break
    
    # 이미지 저장된 디렉토리 경로명 반환
    return filepath[:-4]

# 동영상 t / 10초씩 잘라 저장하기
def imageSave2(filepath, savepath, t):
    filepath, video = fileOpen(filepath)

    #프레임을 저장할 디렉토리를 생성
    try:
        if not os.path.exists(filepath[:-4]):
            os.makedirs(savepath)
    except OSError:
        print ('Error: Creating directory. ' +  filepath[:-4])
        exit(0)


    count = t
    
    while True:
      success, image = video.read()
      
      if success == False:
          break
      
      if (int(video.get(cv2.CAP_PROP_POS_MSEC)/ 100)) == count:
        tt = time(count)
        cv2.imwrite(savepath + f"/time{tt}.jpg", image)
        print(f"\nsaved image {tt}.jpg")
        #print('밀리초 단위로 현재 위치 :', video.get(cv2.CAP_PROP_POS_MSEC))
        print('초 단위로 현재 위치 :', video.get(cv2.CAP_PROP_POS_MSEC)/1000)

        if cv2.waitKey(10) == 27:  # esc키 누르면 종료
            break
        count += t
        
        # 일단 이미지 20개 저장되면 종료되게
        if count == 210:
            break
    
    # 이미지 저장된 디렉토리 경로명 반환
    return savepath