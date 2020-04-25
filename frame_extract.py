#Python script to extract frames from a test video passed as an argument.

import cv2
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-v", help='video to be processed', default='test_video.mkv')
parser.add_argument("-f", help='folder path to save frames', default='test_vid_frames')
args = parser.parse_args()

#Check if destination folder exists, if not make a new directory
if os.path.exists(args.f):
    print('ERROR: Destination folder already exists. Please change the outut path.')
    exit()
else:
    os.mkdir(args.f)

# Opens the Video file
cap= cv2.VideoCapture(args.v)
i=0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    cv2.imwrite(args.f+'/frame'+str(i)+'.jpg',frame)
    i+=1
print('Total number of frames extracted: '+str(i))

cap.release()
