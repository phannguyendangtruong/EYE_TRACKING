# CÀI ĐẶT MÔI TRƯỜNG CHẠY AI
Thuật toán theo dõi mắt
## Cài đặt Python phiên bản 3.6.8
[Nhấp vô đây để tải Python](https://www.python.org/ftp/python/3.6.8/python-3.6.8-amd64-webinstall.exe)


#### Sau khi tải xuống, hãy tìm tệp thiết lập có tên python-3.6.4.exe trong thư mục tải xuống và chạy nó. Bạn sẽ thấy một cái gì đó như:
![INstall python](https://www.pytorials.com/wp-content/uploads/2017/12/python3.6_installation_1.png)
<space>  <space><space><space><space><space>

#### Nhấp vào Run, bạn sẽ thấy một cái gì đó như:
![INstall python](https://www.pytorials.com/wp-content/uploads/2017/12/python3.6_installation_2.png)


#### Theo mặc định, tùy chọn Add Python 3.6 to PATH không được chọn, hãy đảm bảo rằng nó được chọn sau đó nhấp vào Install Now. Nếu thiết lập thành công, bạn sẽ thấy một cửa sổ như sau:
![INstall python](https://www.pytorials.com/wp-content/uploads/2017/12/python3.6_installation_3.png)

## Cài đặt PIP trên Windows
#### Kiểm tra máy bạn đã có PIP chưa
> pip help
  
#### Nếu nó báo lỗi dưới đây thì bạn phải tiến hành thêm PIP
![INstall python](https://phoenixnap.com/kb/wp-content/uploads/2021/06/check-if-pip-is-installed.png)
 
#### 1. Nhấn phím Windows + R để mở hộp thoại Chạy. Sau đó, gõ “ cmd ” và nhấn Enter để mở cửa sổ Command Prompt.
![INstall python](https://cdn.appuals.com/wp-content/uploads/2018/07/cmd.jpg.webp)

#### 2. Trong cửa sổ Command Prompt, hãy chạy lệnh sau để đặt cài đặt PIP thành biến môi trường:
> setx PATH “% PATH%; C:\Python36\Scripts”

## Cài đặt OPENCV
#### 1. Nhấn phím Windows + R để mở hộp thoại Chạy. Sau đó, gõ “ cmd ” và nhấn Enter để mở cửa sổ Command Prompt.
![INstall python](https://cdn.appuals.com/wp-content/uploads/2018/07/cmd.jpg.webp)

#### 2. Chạy câu lệnh sau:
> pip install opencv-python
  
#### 3. Sau khi opencv cài đặt thành công, bạn gõ lệnh "python"
![python](https://user-images.githubusercontent.com/75264221/138564618-cd07fc66-b1aa-40eb-8a2a-6ff67395e916.jpg)
  
#### 4. Thêm opencv vào python
![cv2](https://user-images.githubusercontent.com/75264221/138564536-ac871f79-3a91-434e-b6e4-e2fe9ce4abfb.jpg)

## Cài đặt Dlib
#### 1. Nhấn phím Windows + R để mở hộp thoại Chạy. Sau đó, gõ “ cmd ” và nhấn Enter để mở cửa sổ Command Prompt.
![INstall python](https://cdn.appuals.com/wp-content/uploads/2018/07/cmd.jpg.webp)
#### 2. Dán đoạn code dưới đây vào terminal
> python -m pip install https://files.pythonhosted.org/packages/0e/ce/f8a3cff33ac03a8219768f0694c5d703c8e037e6aba2e865f9bae22ed63c/dlib-19.8.1-cp36-cp36m-win_amd64.whl#sha256=794994fa2c54e7776659fddb148363a5556468a6d5d46be8dad311722d54bfcf
  
![s1](https://user-images.githubusercontent.com/75264221/139001023-a292b46a-9049-4045-b4bf-f0364a8de95d.jpg)

## Cài đặt numpy
#### Dán đoạn code dưới đây vào cửa sổ cmd
> pip install numpy
  
  
## CHẠY CHƯƠNG TRÌNH
#### Mở project EYE_TRACKING_FPOLY bằng Visual code
#### Chạy lệnh bên dưới bằng của sổ terminal của VSCode
> python .\example.py
  
![s1](https://user-images.githubusercontent.com/75264221/139001667-b49f6a77-b1a3-4225-81b3-db585fb3928f.jpg)

#### Và đây là kết quả, chúc các bạn thành công

 ![s1](https://user-images.githubusercontent.com/75264221/139001922-14c8356c-f0bf-43b7-9c9f-c8fd71e29ec1.jpg)

 
  
  

