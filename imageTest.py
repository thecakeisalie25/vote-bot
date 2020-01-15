from ImageKit import ImgKit as imgkit
import typing
# import 
logo = imgkit.imread("fullblackPix.png")
red = imgkit.Image.new("RGBA", (4096,4096), (255, 0, 0, 255))
green = imgkit.Image.new("RGBA", (4096,4096), (0, 255, 0, 255))
logoredgreen = imgkit.Image.composite(red, green, logo)
imgkit.Image.getmodebandnames(imgkit.Image.modes)
imgkit.imshow(imgkit.get_band(logoredgreen, "R"))