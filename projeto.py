import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,"sol",(100,80),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"mercurio",(100,165),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"venus",(190,170),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"terra",(280,165),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"marte",(370,165),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"jupiter",(550,60),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"saturno",(760,120),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"urano",(960,140),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"netuno",(1100,140),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.imshow("resultado",img)

cv2.waitKey(0)

cv2.imwrite("solarSystemUpdate.jpg",img)

