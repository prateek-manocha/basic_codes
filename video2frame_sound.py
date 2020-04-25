#Python script to extract frames from a test video passed as an argument.

import cv2
import os
import argparse
import moviepy.editor


def extract_frame_sound(video, folder):
    #For extraction of frames

    #To add leading zeros to frame number
    width = 3
    #Check if destination folder exists, if not make a new directory
    if os.path.exists(folder):
        print('ERROR: Destination folder already exists. Please change the outut path.')
        exit()
    else:
        os.mkdir(folder)

    # Opens the Video file
    cap= cv2.VideoCapture(video)
    i=0
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == False:
            break
        cv2.imwrite(os.path.join(folder,'frame'+str(i).zfill(width)+'.jpg'),frame)
        i+=1

    print('Total number of frames extracted: '+str(i))
    cap.release()

    #For extraction of sound
    video = moviepy.editor.VideoFileClip(video)
    audio = video.audio
    audio.write_audiofile(folder+".mp3")
    print("Audio extracted as: "+folder+".mp3")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", help='video to be processed(name along with extension)', default='test_video.mkv')
    parser.add_argument("-f", help='folder path to save frames', default='test_video')
    args = parser.parse_args()
    extract_frame_sound(args.v, args.f)
