import cv2
import os



def vid_splitter(dir_name: str):
    img = 'frames'
    if not os.path.exists(img):
        os.makedirs(img)
    directory = os.fsencode(dir_name)
    count = 0
    for file in os.listdir(directory):
        filename = os.fsdecode(file)


        if filename.endswith(".mp4"):
            full_path = os.path.abspath(os.path.join(directory, file))
            full_path = full_path.decode("utf-8")
            full_path = full_path.replace("\\","\\\\")

            print(full_path)
            vidcap = cv2.VideoCapture(full_path)

            success, image = vidcap.read()

            rgb_frames = []
            while success:
                vidcap.set(cv2.CAP_PROP_POS_MSEC, (count * 200))
                cv2.imwrite(os.path.join(img, "frame{:d}.jpg".format(count)), image)  # save frame as JPEG file
                success, image = vidcap.read()
                print('Read a new frame: ', success)
                if not(image is None):
                    rgb_frames.append(image[:, :, ::-1])

                count += 1

    return rgb_frames

vid_splitter("vids")