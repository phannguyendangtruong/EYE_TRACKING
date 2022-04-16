import cv2
from gaze_tracking import GazeTracking
from gaze_tracking.eye import Eye

# khoảng cách từ máy ảnh đến vật thể (khuôn mặt) được đo
# centimet
Known_distance = 76.2
 
# chiều rộng của khuôn mặt trong thế giới thực hoặc Mặt phẳng đối tượng
# centimet
Known_width = 14.3
 
# Colors
GREEN = (0, 255, 0)
RED = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
 
# defining the fonts
fonts = cv2.FONT_HERSHEY_COMPLEX
 
 #--



# đối tượng nhận diện khuôn mặt
face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
 

# chức năng tìm độ dài tiêu cự
def Focal_Length_Finder(measured_distance, real_width, width_in_rf_image):
 
   # tìm độ dài tiêu cự
    focal_length = (width_in_rf_image * measured_distance) / real_width
    return focal_length
 
# chức năng ước tính khoảng cách
def Distance_finder(Focal_Length, real_face_width, face_width_in_frame):
 
    distance = (real_face_width * Focal_Length)/face_width_in_frame
 
    # trả lại khoảng cách
    return distance
 
 
def face_data(image):

    face_width = 0  # làm cho chiều rộng khuôn mặt bằng 0
 
    # chuyển đổi hình ảnh màu so với hình ảnh thang màu xám
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
    # phát hiện khuôn mặt trong ảnh
    faces = face_detector.detectMultiScale(gray_image, 1.3, 5)
 
    # vòng qua các khuôn mặt phát hiện trong hình ảnh
    # nhận tọa độ x, y, chiều rộng và chiều cao
    for (x, y, h, w) in faces:
      
        # vẽ hình chữ nhật trên khuôn mặt
        cv2.rectangle(image, (x, y), (x+w, y+h), GREEN, 2)
 
        # nhận chiều rộng khuôn mặt tính bằng pixel
        face_width = w
 
    # trả lại chiều rộng khuôn mặt tính bằng pixel
    return face_width
 
 
# đọc tham chiếu_image từ thư mục
ref_image = cv2.imread("E:\Thi\ResFres\BIO-ID Dataset\BioID_0000.jpg")
 
# find the face width(pixels) in the reference_image
ref_image_face_width = face_data(ref_image)
 
# lấy tiêu điểm bằng cách gọi "Focal_Length_Finder"
# chiều rộng khuôn mặt trong tham chiếu (pixel),
# Đã biết_distance (cm),
# known_width (cm)
Focal_length_found = Focal_Length_Finder(
    Known_distance, Known_width, ref_image_face_width)
 
print(Focal_length_found)
 
# hiển thị hình ảnh tham khảo
cv2.imshow("ref_image", ref_image)

# khởi tạo đối tượng máy ảnh để chúng tôi
# có thể lấy khung từ nó
cap = cv2.VideoCapture(0)
 

# vòng lặp qua khung, đến từ
# máy ảnh / video
while True:
 
   # đọc khung hình từ máy ảnh
    _, frame = cap.read()
    
    # gọi hàm face_data để tìm
    # chiều rộng của khuôn mặt (pixel) trong khung
    face_width_in_frame = face_data(frame)
 

    # kiểm tra nếu mặt bằng 0 thì không 
    # tìm khoảng cách
    if face_width_in_frame != 0:
       
        # tìm khoảng cách bằng hàm gọi
        # Cần chức năng tìm khoảng cách khoảng cách
        # đối số này là Focal_Length,
        # Đã biết_ width (cm),
        # và Đã biết_distance (cm)
        Distance = Distance_finder(
            Focal_length_found, Known_width, face_width_in_frame)
 
        # vẽ đường làm nền của văn bản
        cv2.line(frame, (30, 30), (230, 30), RED, 32)
        cv2.line(frame, (30, 30), (230, 30), BLACK, 28)
 
        # Vẽ Văn bản trên màn hình
        cv2.putText(
            frame, f"Distance: {round(Distance,2)} CM", (30, 35),
          fonts, 0.6, GREEN, 2)
 
    # hiển thị khung trên màn hình
    cv2.imshow("frame", frame)
 
   
    if cv2.waitKey(1) == ord("q"):
        break
 
# hiển thị khung trên màn hình
cap.release()
 
# closing the the windows that are opened
cv2.destroyAllWindows()