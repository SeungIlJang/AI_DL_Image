#openCv 가져오기
import cv2

#동영상 불러오기
cap = cv2.VideoCapture('03.mp4')

while True:
    #동영상에서 이미지 추출,ret은 다 읽으면 False
    ret, img = cap.read()

    if ret == False:
        break
    # 칼라를 그레이로 변환
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    # 이미지 자르기 y에서 x로
    img = img[183:721,465:878]    
    #이미지 보여주기
    cv2.imshow('result', img)
    #10초간 기다렸다가 출력,q이면 종료
    if cv2.waitKey(10) == ord('q'):
        break