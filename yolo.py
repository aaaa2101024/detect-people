from ultralytics import YOLO
from check_person import is_exist_person


# Yolo関係の処理
class Yolo:
    def __init__(self):
        # YOLOv11のモデルをロード
        self.model = YOLO("yolo11n.pt")

    def get_value(self, results):
        detect = []
        for result in results:
            for box in result.boxes:
                temp = [result.names[int(box.cls)], float(box.conf)]
                detect.append(temp)

        return detect

    def main(self, frame):
        # YOLOで物体検出を行う
        results = self.model(frame)

        # 結果をフレームに描画して表示
        annotated_frame = results[0].plot()

        # 各値の取得
        detect_list = self.get_value(results)

        # personがいるかどうかを探してもらう
        exist_person = is_exist_person(detect_list)
        # 描画結果と人間がいたかどうかを返す
        return annotated_frame, exist_person


if __name__ == "__main__":
    Yolo.main()
