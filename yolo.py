from ultralytics import YOLO

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

        # 描画結果を返す
        return annotated_frame,detect_list


if __name__ == "__main__":
    Yolo.main()
