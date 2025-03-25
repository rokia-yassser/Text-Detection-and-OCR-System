import easyocr
import cv2
import matplotlib.pyplot as plt 
img_path='D:\AI_ML\ocr\warning-construction-zone-symbol-sign-on-white-background-free-vector.jpg'
img=cv2.imread(img_path)


reader=easyocr.Reader(['en'])
results = reader.readtext(img)
print(results)
for (bbox, text, prob) in results:
    (top_left, top_right, bottom_right, bottom_left) = bbox
    top_left = tuple(map(int, top_left))
    bottom_right = tuple(map(int, bottom_right))

    # Draw rectangle around detected text
    cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 2)
    cv2.putText(img, text, (top_left[0], top_left[1] - 10), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)   
       
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.axis('off')  # Hide axis
plt.show()
