def triangle(x,y):
    if x>=50 and x<=85:
        xInT= x-50
        ymin = xInT*2+60
        if y<=130 and y>=ymin:
            return True
        else:
            return False
    else:
        return False

def cercle(x,y):
    XinR = x-130
    YinR = y-90
    xmin = 110
    xmax = 150
    ymin = 70
    ymax = 110

    if XinR <0:
        ymin-=(130-x)
        ymax-=(130-x)

    if XinR >0:
        ymin-=(130-x)
        ymax-=(130-x)
    if YinR <0:
        xmin-=(90-y)
        xmax-=(90-y)
    if YinR >0:
        xmin-=(90-y)
        xmax-=(90-y)
    if x>= 110 and x<= 150 and y >= 70 and y <= 110:
      if x>=xmin and x<=xmax and y>=ymin and y<=ymax:
        return True
      else:
        return False
    else:
        return "out of bounds"

