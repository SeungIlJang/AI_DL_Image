import cv2

# 동영상 불러오기
cap = cv2.VideoCapture('04.mp4')
# 웹캠 연동
# cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()

    if ret == False:
        break

    cv2.rectangle(img, pt1=(721, 183), pt2=(878, 465), color=(255, 0, 0), thickness=2)
    
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    img = cv2.resize(img, dsize=(640,360))
    
    # 이미지 자르기
    # img = img[100:200,150:250]
    
    cv2.imshow('result', img)

    if cv2.waitKey(100) == ord('q'):
        break