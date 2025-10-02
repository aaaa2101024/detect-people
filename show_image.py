import socket
from yolo import Yolo
import cv2
import struct

def show_image():
    yolo = Yolo()
    while True:
        frame,detect_list = yolo.main()

        # qを押すと終了
        if type(frame) is str:
            break

        # JPEGに圧縮
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 80]
        result, encimg = cv2.imencode('.jpg', frame, encode_param)
        data = encimg.tobytes()

        # 映像を垂れ流す
        cv2.imshow("daa", frame)

        with open("log.txt", "a", encoding="utf-8") as f:
            for list in detect_list:
                print(detect_list, file=f)

if __name__ == "__main__":
    show_image()
