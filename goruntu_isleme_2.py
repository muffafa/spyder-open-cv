import cv2
import matplotlib.pyplot as plt

fotograf_sayisal = cv2.imread('DSC03847.JPG')
fotograf_sayisal_gri = cv2.imread('DSC03847.JPG',0)


print('normal')
print(fotograf_sayisal)

print('gri')
print(fotograf_sayisal_gri)

# =============================================================================
# #bgr  -> bgr
# cv2.imshow('adsf', fotograf_sayisal_gri)
# 
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# =============================================================================


# bgr -> rgb
fotograf_sayisal_rgb = cv2.cvtColor(fotograf_sayisal, cv2.COLOR_BGR2RGB)
fotograf_sayisal_gri_rgb = cv2.cvtColor(fotograf_sayisal_gri, cv2.COLOR_BGR2RGB)


#plt.figure(figsize=(12,4))

plt.subplot(1,2,1)
plt.imshow(fotograf_sayisal_rgb)
plt.title('Normal')

plt.subplot(1,2,2)
plt.imshow(fotograf_sayisal_gri_rgb)
plt.title('Gri')

plt.show()