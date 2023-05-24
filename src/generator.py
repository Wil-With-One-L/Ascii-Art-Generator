import cv2
import util
import ascii
 
def getPixelsInSection(image, section_x, section_y, section_size): 
  pixels = []
  start_x = section_x * section_size
  start_y = section_y * section_size
  for x in range(start_x, start_x + section_size):
    for y in range(start_y, start_y + section_size):
      pixels.append(image[y, x])
  return pixels

image = cv2.imread('Images/link.jpeg')

output = open('Output/output.txt', 'w')

img_height = image.shape[0]
img_width = image.shape[1]

# -----------------

section_size = int(input(f'resolution (number of pixels/character): '))
rev = input('photonegative? [Y] / [N]: ')

util.checkBool(rev)
util.checkSize(section_size, img_width, img_height)

if rev == 'Y' or rev == 'y':
  rev = True
elif rev == 'N' or rev == 'n':
  rev = False

x_sections = img_width // section_size
y_sections = img_height // section_size

for y in range(0, y_sections):
  line = ''
  for x in range(0, x_sections):
    pixels = getPixelsInSection(image, x, y, section_size)
    line += ascii.getAscii(pixels, rev)
    line += ' '
  output.write(line + '\n')