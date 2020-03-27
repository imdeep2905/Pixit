# Pixit
It's downscaled but upscaled :dizzy_face: !
# Contents
1. [Introduction](#Introduction)
2. [How to run](#How-to-run) 
3. [Logic behind pixelating](#Logic-behind-pixelating)
4. [Credits](#Credits)
# Introduction
This is a little project which pixelate the given image.After each run program will show you resultant image and you can save it with desired name.
# How to run
  1. Fulfill ```requirements.txt``` (i.e. ```pip install -r requirements.txt```).
  2. Run with command ```python main.py <file_path>```.
  3. Optional arguments
      * Intensity:  ```python main.py <file_path> -size 20```(Fill 20x20 pixels at once).<br/>
        Default value of size is **8**.
      * Grey: ```python main.py <file_path> -grey```(converts image to greyscale).<br/>
        By Default output images will be same as provided(in terms of channels).
      * Help: ```python main.py --help```(To see help).
  ## Some Examples 
  1. ```python main.py "Test/test1.jpg"``` <br/><br/>
      Original: <br/> 
      <img src = "https://github.com/imdeep2905/Pixit/blob/master/Test/test1.jpg" />
      Output: <br/>
      <img src = "https://github.com/imdeep2905/Pixit/blob/master/Test/test1o.jpg" /><hr/>
      
  2. ```python main.py "Test/test2.jpg" -size 10 -grey ``` <br/><br/>
      Original: <br/> 
      <img src = "https://github.com/imdeep2905/Pixit/blob/master/Test/test2.jpg" />
      Output: <br/>
      <img src = "https://github.com/imdeep2905/Pixit/blob/master/Test/test2o.jpg" /><hr/>
      
  3. ```python main.py "Test/test3.jpg" -size 100 ``` <br/><br/>
      Original: <br/> 
      <img src = "https://github.com/imdeep2905/Pixit/blob/master/Test/test3.jpg" />
      Output: <br/>
      <img src = "https://github.com/imdeep2905/Pixit/blob/master/Test/test3o.jpg" /><hr/>
  
  4. ```python main.py "Test/test4.jpg" -size 6 -grey``` <br/><br/>
      Original: <br/> 
      <img src = "https://github.com/imdeep2905/Pixit/blob/master/Test/test4.jpg" />
      Output: <br/>
      <img src = "https://github.com/imdeep2905/Pixit/blob/master/Test/test4o.jpg" /><hr/>
  
  5. ```python main.py "Test/test5.jpg" -size 20``` <br/><br/>
      Original: <br/> 
      <img src = "https://github.com/imdeep2905/Pixit/blob/master/Test/test5.jpg" />
      Output: <br/>
      <img src = "https://github.com/imdeep2905/Pixit/blob/master/Test/test5o.jpg" /><hr/>
  
  ## Demo Console log
  ```
  C:\Users\Deep Raval\Desktop\Projects\Pixit>python main.py "Test/test4.jpg" -size 6 -grey
  Recieved Image with Shape: (1080, 1920, 3)
  Converting Image to greyscale (if it is not already greyscale)...
  Now shape of the Image is: (1080, 1920, 1)
  Now Converting Image...
  Save ? <y/n>: y
  Enter Name for for file: test4o
  ```
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
