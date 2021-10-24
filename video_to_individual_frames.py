import cv2
vidfile = input("enter the name of ur video file. e.g = rickroll.mp4 :")
vidcap = cv2.VideoCapture(vidfile)

def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite("image"+str(count)+".jpg", image)     
    return hasFrames
sec = 0
x = float(input("how much frames per sec do u want? :"))
frameRate = float(1/x)
count=1
success = getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)