# pillar_detection
## 物件偵測方法
主要使用霍夫圓轉換找出大小圓及其圓心，再換算距離確定其是否在要求範圍內(預設為大小圓距離大於小圓半徑，或小圓圈極接近或超過大圓圈判定為<code style="color : red">Fail</code>)
因使用模板有三個柱子，切割三個大小相同且包含一柱子的圖片，並放大至(300,400),模糊化,灰階化和色彩轉換等方式加強其辨識能力。
## 霍夫圓轉換簡介
圓有圓心和半徑的特性,檢測到圖形的圓型輪廓,利用霍夫梯度法可找到圓心位置。霍夫圓轉換有以下參數:
- image: 輸入灰階圖片(可參考<code style="color : black">cv2.imread(img_name,cv.IMREAD_GRAYSCALE</code>)
- circles: 輸出偵測到的圓，每一個圓以一組浮點數<code style="color : black">x,y,radius</code>向量呈現
