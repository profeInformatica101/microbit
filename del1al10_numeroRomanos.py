from microbit import *

img_0 = "non est"
img_1 = Image("00900:00900:00900:00900:00900") #I
img_2 = Image("09090:09090:09090:09090:09090") #II
img_3 = Image("90909:90909:90909:90909:90909") #III
img_4 = Image("90909:90909:90999:90090:90090") #IV
img_5 = Image("09090:09090:09990:00900:00900") #V
img_6 = Image("09099:09099:09999:00909:00909") #VI
img_7 = Image("90999:90999:99999:09099:09099") #VII
img_8 = Image("90999:90999:99999:09999:09999") #VIII
img_9 = Image("90909:90909:90090:90909:90909")#IX
img_10 = Image("09090:09090:00900:09090:09090")#X

numeros = [img_0, img_1, img_2, img_3, img_4, img_5,img_6,img_7,img_8,img_9,img_10]

for img_n in numeros:
    display.show(img_n)
    sleep(1000)

