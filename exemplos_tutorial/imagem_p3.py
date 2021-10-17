def create_img_p3():
    # PPM header
    width = 128
    height = 128
    maxval = 255
    ppm_header = f'P3\n{width}\n{height}\n{maxval}\n'

    # PPM image data (filled with blue)

    f = open("demo_img1.ppm", "w")
    f.write(ppm_header)
    for x in range(0, height):
        for y in range(0, width):
            if x == y:
                f.write(" 0 0 0 ")
            elif (x + y) == height - 1:
                f.write(" 0 0 0 ")
            elif x < y:
                f.write(" 0 0 255 ")
            else:
                f.write(" 0 255 0 ")
        f.write("\n")
    f.close()

