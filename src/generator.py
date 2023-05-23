import cv2
# import util
import ascii
 
image = cv2.imread('Images/no_fish_please.png')

output = open('Output/test_output.txt', 'w')
output.write('test')

img_height = image.shape[0]
img_width = image.shape[1]

size = input('size: ')