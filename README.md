# Pixit
![Demo]()<br>
# Contents
1. [Introduction](#Introduction)
2. [How to run](#How-to-run) 
3. [Logic behind pixelating](#Logic-behind-pixelating)
4. [Credits](#Credits)
# Introduction
This is a little project which pixelate the given image<br>
# How to run
  1. Fulfill ```requirements.txt``` (i.e. ```pip install -r requirements.txt```).
  2. Run with command ```python main.py <file_path>```.
  3. Optional arguments
      * Intensity:  ```python main.py <file_path> -size 20```(Fill 20x20 pixels at once).
      * Grey: ```python main.py <file_path> -grey```(converts image to greyscale).
      * Help: ```python main.py --help```(To see help).
  <br>
  Some Examples:
  

# Logic behind pixelating
As we know images are simply array of pixels. For ex. a RGB image of resolution ```1333x688``` can be viewed as an array of shape ```(1366, 768, 3)```(last 3 for seprate Red, green and blue pixels).Now let's take ```SIZE = 10 ``` and pixelate the image of same size.
<br>
First let's start with first pixel (i.e. ```(0, 0, 0-3)```) and give square with ```10x10``` starting from selected pixel same pixel value.Now next we must select pixel which is atleast SIZE distance away from current pixel(i.e ```(11, 0, 0-3)``` in this case). After repeating this process for whole image we can pixelate an image. 
<br>
I hope you understood.
<br>
P.S.: I know it's better to give square mean value of pixel.But, hey this also looks good.xD
# Credits

Contributors :computer: : 
   * [Deep Raval](https://github.com/imdeep2905)

Without these excellant libraries :heart: this would not have been possible.
   * opencv-python
   * numpy
   * matplotlib
