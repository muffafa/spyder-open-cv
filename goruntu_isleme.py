import cv2
import matplotlib.pyplot as plt

fotograf_sayisal = cv2.imread('DSC03847.JPG',0)
# # fotograf_sayisal = cv2.imread('/Users/muffafa/Desktop/DSC03847.JPG')


# Ortalama filtre
blur_avg = cv2.blur(fotograf_sayisal, (5,5))

# Gauss filtre
blur_gauss = cv2.GaussianBlur(fotograf_sayisal, (5,5), 1)


plt.figure(figsize=(12,4))
plt.subplot(1,3,1), plt.imshow(fotograf_sayisal, cmap='gray'), plt.title("Orijinal")
plt.subplot(1,3,2), plt.imshow(blur_avg, cmap='gray'), plt.title("Ortalama Filtre")
plt.subplot(1,3,3), plt.imshow(blur_gauss, cmap='gray'), plt.title("Gauss Filtre")
plt.show()

