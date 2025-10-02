import cv2
from ultralytics import YOLO

# Yolo関係の処理
class Yolo:
    def __init__(self):
        # YOLOv11のモデルをロード
        self.cap = cv2.VideoCapture(0)
        # Webカメラの起動
        self.model = YOLO("yolo11n.pt") 

    def main(self):
        ret, frame = self.cap.read()
        if not ret:
            return 'q'

        # YOLOで物体検出を行う
        results = self.model(frame)

        # 結果をフレームに描画して表示
        annotated_frame = results[0].plot()

        # 'q'を押すと終了
        if cv2.waitKey(1) & 0xFF == ord('q'):
            self.cap.release()
            cv2.destroyAllWindows()
            return 'q'

        # 描画結果を返す
        return annotated_frame

if __name__ == "__main__":
    Yolo.main()
