# 人間がいるかどうかをカメラで検知するdiscord bot
カメラを用いて, 人間がいるかを検知し, 存在する場合は時間情報をつけてdiscord上に送信を行うプログラムを作成しました. 簡易的な監視カメラにはなると思いますやったね!!!!!

## ファイル構成図
```text
.
├── README.md                          // これ!!!!!
├── __pycache__
│   ├── check_person.cpython-311.pyc
│   ├── settings.cpython-311.pyc
│   └── yolo.cpython-311.pyc
├── check_person.py                    // yoloから検出した情報の中に人間らしきものが存在するかを返す関数
├── log.txt                            // 人間の検出履歴を時刻とともに保存する
├── requirements.txt                   
├── send_detect_person.py              // discord bot 本体
├── settings.py                        // .envから情報を読み込む
├── show_image.py                      // カメラから映像をキャプチャ
├── yolo.py                            // キャプチャした映像をyoloで検証する
└── yolo11n.pt                         
```

図を見てわかります通り, txtファイルにログを取る形で構成を行いました. 

## システム構成図
![システム構成図](./システム構成図.png)

## 起動方法
```shell
python send_detect_person.py # discord botを起動
python show_image.py  # カメラを起動
```