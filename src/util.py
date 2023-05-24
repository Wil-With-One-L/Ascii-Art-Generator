def checkSize(input, width, height):
  if input > width or input > height:
    exit()

def checkBool(input):
  if input not in ['y', 'Y', 'n', 'N']:
    exit()