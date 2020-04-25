#Python script for combining frames to make a video.

import cv2
import argparse
import os


def combine_frames(folder, video_name):
    img_array = []
    frames = os.listdir(folder)
    list.sort(frames)
    for i in frames:
        img = cv2.imread(os.path.join(folder,i))
        img_array.append(img)

    height, width, layers = img.shape
    size = (width,height)
    out = cv2.VideoWriter(video_name,cv2.VideoWriter_fourcc(*'DIVX'), 25, size)
    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()
    print('Video saved as: '+video_name)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", help='Path fot input frames', default='frames')
    parser.add_argument("-d", help='file name of generated video with extension(.mkv, .avi, .mp4)', default='combined_video.mkv')
    args = parser.parse_args()
    combine_frames(args.f, args.d)
