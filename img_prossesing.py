import cv2
import os


def vid_splitter(path: str):
    img = 'frames'
    os.mkdir(img)
    vidcap = cv2.VideoCapture(path)
    success, image = vidcap.read()
    count = 0
    rgb_frames=[]
    while success:
        vidcap.set(cv2.CAP_PROP_POS_MSEC, (count * 2000))
        cv2.imwrite(os.path.join(img, "frame{:d}.jpg".format(count)), image)  # save frame as JPEG file
        success, image = vidcap.read()
        print('Read a new frame: ', success)
        rgb_frames.append(image[:, :, ::-1])
        count += 1


    return rgb_frames
