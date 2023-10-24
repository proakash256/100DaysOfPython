import colorgram

colors = colorgram.extract('image.jpg', 50)
color_list = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    color_list.append((r, g, b))
color_list.pop(0)
color_list.pop(0)
