def ascii(reverse):
  chars = "$$$$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1[]?-_+~<>i!lI;:,\"^`\'.        "
  if reverse:
    return chars[::-1]
  return chars

def getLuminance(pixel):
  return (0.33 * pixel[2]) + (0.5 * pixel[1]) + (0.16 * pixel[0])

def getAverageLuminance(pixels):
  sum = 0
  for p in pixels:
    sum += getLuminance(p)
  return sum / len(pixels)

# returns an ascii character based on the average luminance of a section of pixels
def getAscii(pixels, rev):
  chars = ascii(rev)

  lum = getAverageLuminance(pixels)
  ratio = lum / 255
  idx = int(ratio * len(chars))

  return chars[idx]