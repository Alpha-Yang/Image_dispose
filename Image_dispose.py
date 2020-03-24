import cv2
import matplotlib.pyplot as plt
import numpy as np

def cv_show(name,img):
    cv2.imshow(name,img)  # 显示图片，可以多个窗口
    cv2.waitKey(0) # 窗口停止时间，毫秒级，0表示任意键结束
    cv2.destroyAllWindows()

# img=cv2.imread('image\lena.jpg')  # 读取图片的RGB参数
# cv_show('image',img)
# size=img.shape # 获取矩阵的维度
# img=cv2.imread('image\lena.jpg',cv2.IMREAD_GRAYSCALE) # 灰度处理：读取灰度参数
# cv_show('lena_gray',img)
# cv2.imwrite('image\lena_gray.png',img) # 保存图片

# # 处理视屏
# video=cv2.VideoCapture('image/test.mp4') # 捕捉摄像头，用数字来控制不同的设备，例如外接通常为400
# # 检查是否正确打开
# if video.isOpened():
#     open, frame = video.read()
# else:
#     open=False
#
# while open:
#     ret, frame=video.read()
#     if frame is None:
#         break
#     if ret==True:
#         gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)   # 转换视屏颜色
#         cv2.imshow('result',gray)
#         if cv2.waitKey(10) & 0xFF==27:  # waitkey代表视屏播放时间，0xFF==27相当于键盘上的Esc键退出
#             break
# video.release()
# cv2.destroyAllWindows()

# 截取部分图像数据
img=cv2.imread('image\lena.jpg')
# lena_new=img[0:200,0:200]
# cv_show('lena_new',lena_new)
# cv2.imwrite('image\lena_new.png',lena_new) # 保存图片
# # 颜色通道提取
# b,g,r=cv2.split(img)
# # 只保留R
# cur_img=img.copy()
# cur_img[:,:,0]=0
# cur_img[:,:,1]=0
# cv_show('R',cur_img)
# cv2.imwrite('image\lena_R.png',cur_img) # 保存图片

# # 边界填充
# top_size,bottom_size,left_size,right_size = (50,50,50,50) # 表示拓充上下左右的宽度
# replicate = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, borderType=cv2.BORDER_REPLICATE)
# reflect = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size,cv2.BORDER_REFLECT)
# reflect101 = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv2.BORDER_REFLECT_101)
# wrap = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv2.BORDER_WRAP)
# constant = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size,cv2.BORDER_CONSTANT, value=0)
#
# plt.subplot(231), plt.imshow(img, 'gray'), plt.title('ORIGINAL')
# plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('REPLICATE')
# plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('REFLECT')
# plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title('REFLECT_101')
# plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('WRAP')
# plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('CONSTANT')
# plt.savefig('image/image_filling.png')
# plt.show()

# # 数值计算
# img_cat=cv2.imread('image/cat.jpg')
# img_car=cv2.imread('image/car.png')
# img_cat2=img_cat+10
# img_sum=img_cat+img_cat2 # 相当于%256
# img_sum2=cv2.add(img_cat,img_cat2)
#
# # 图像融合
# # print(img_cat.shape,img_car.shape)
# img_car=cv2.resize(img_car,(500,414))
# # img_car=cv2.resize(img_car,(0,0),fx=1,fy=3)
# res=cv2.addWeighted(img_cat,0.6,img_car,0.4,0)
# # cv_show('fusion',res)
# plt.imshow(res)
# plt.show()