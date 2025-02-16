# pillar_detection(瑕疵偵測)

## 物件偵測方法

主要使用霍夫圓轉換找出大小圓及其圓心,再換算距離確定其是否在要求範圍內(預設為大小圓距離大於小圓半徑,或小圓圈極接近或超過大圓圈判定為<code style="color : red">Fail</code>)
因使用模板有三個柱子，切割三個大小相同且包含一柱子的圖片，並放大至(300,400),模糊化,灰階化和色彩轉換等方式加強其辨識能力。

## 霍夫圓轉換簡介

圓有圓心和半徑的特性,檢測到圖形的圓型輪廓,利用霍夫梯度法可找到圓心位置。霍夫圓轉換有以下參數:
- <code>image</code>: 輸入灰階圖片(可參考<code style="color : black">cv2.imread(img_name,cv.IMREAD_GRAYSCALE</code>)
- <code>circles</code>: 輸出偵測到的圓，每一個圓以一組3維浮點數<code style="color : black">x,y,radius</code>向量呈現
- <code>method</code>: [檢測方法](https://docs.opencv.org/4.x/dd/d1a/group__imgproc__feature.html#ga073687a5b96ac7a3ab5802eb5510fe65)。常用為<code>HOUGH_GRADIENT</code>和<code>HOUGH_GRADIENT_ALT</code>
- <code>dp</code>: 累加解析度和圖片解析度的反比。數值越小,圓的檢測越嚴格(若圓形輪廓不明顯，將不會被檢測;或是可能會檢測出很多不正常的圓)。例如<code>dp = 2</code>,代表累加解析度為圖片解析度的一半。
- <code>minDist</code>: 圓心間的最小距離。值越小,可能會檢測到錯誤的圓;值太大,則會錯失檢測。
- <code>param1</code>: 第一個<code>method</code>參數(For <code>HOUGH_GRADIENT</code>和<code>HOUGH_GRADIENT_ALT</code>)。作為較高的的門檻<code>threshold1</code>[@Canny edge detector](https://medium.com/@pomelyu5199/canny-edge-detector-%E5%AF%A6%E4%BD%9C-opencv-f7d1a0a57d19)(<code>threshold2</code>通常為<code>threshold1</code>的3分之1。
- <code>param2</code>: 第一個<code>method</code>參數(For <code>HOUGH_GRADIENT</code>和<code>HOUGH_GRADIENT_ALT</code>)。它是累加解析度的門檻,應用於檢測圓心。值越小,越不容易檢測到圓。
- <code>minRadius</code>: 可被接受最小半徑的圓會被檢測(與圖片有關)。
- <code>maxRadius</code>: 可被接受最大半徑的圓會被檢測(與圖片有關)。

## 實作及其限制
*以此快速了解如何使用*
[unit-test_foto](./unit-test_foto)儲存在同執行檔的路徑層，則會自動提取第一張照片[test1.jpg](./unit-test_foto/test1.jpg)。
三個柱子分別檢測
![detected circles](https://github.com/user-attachments/assets/67b61f66-c2d5-4e5c-a3c9-f048d7355da1)  
  
並分辨其是否滿足要求
>兩圓心距離小於小圓半徑或小圓在大圓裡
