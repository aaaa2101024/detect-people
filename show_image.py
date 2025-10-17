# 映像を取得し, yoloを使って人間を検出する
# 人間が検出されたらlog.txtに書き込み
from yolo import Yolo
import cv2
import datetime
import time
from settings import STANDBYTIME

cap = cv2.VideoCapture(0)

def show_image():
    yolo = Yolo()
    while True:
        ret, frame = cap.read()
        if not ret:
            print("映像が取得できませんでした")
            break
        annotated_frame,exist_person = yolo.main(frame)

        # JPEGに圧縮
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 80]
        result, encimg = cv2.imencode('.jpg', annotated_frame, encode_param)
        data = encimg.tobytes()

        # 映像を垂れ流す
        cv2.imshow("daa", annotated_frame)

        if exist_person:
            datetime_now = datetime.datetime.now()
            str_now = datetime_now.strftime('%Y/%m/%d %H:%M:%S')
            with open("log.txt", "a", encoding="utf-8") as f:
                print(f"{str_now} : person is exist", file=f)
            # 連続更新防止用の待機時間
            time.sleep(STANDBYTIME)
        
        # 'q'を押すと終了
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            break

if __name__ == "__main__":
    show_image()
