# 360CamCode
Code repository for the Open Source 360 Camera Project

This repository contains code to capture images and _eventually_ process the raw images for panoramic or spherical panoramic stiching. 

## First spherical panorama:
* Camera white balance is off due to no IR filte on lens
* This was created using 2 images captured with a 180 degree rotation (I only have 1 of the 220 degree lenses currently)
* Created with the free version of [PTGui](https://www.ptgui.com)
* Can be viewed using PTview, google street view app or other 360 spherical viewers
![](http://i.imgur.com/FxKGasV.jpg)


As detailed on the [hardware page](https://github.com/Open360cam/360CamHardware/blob/gh-pages/README.md),
Our key principals are as follows:
* Open source hardware and software to encourage educational use and a developer community
* The primary hardware is to be off the shelf (lenses and image sensor PCBs)
* Simple mechanical mounting, can be assembled without any specialized tools or equipment
* Compatible with mobile computing platforms such as Raspberry Pi or similar
* Cost to be similar to a consumer level 360 camera such as Ricoh Theta ($250-$350)
* Performance to be adequate to create 360 panoramas 

To enable portable imaging, we have developed and tested the cameras on a Raspberry Pi 2 B+ utilizing OpenCV libraries to control and capture images from the cameras. The USB 2.0 cameras from ELP that we selected us the [Sonix SN9C292A](http://www.sonix.com.tw/article-en-995-7860) video controller with USB Video Class compatibility. 

To see examples of images captured with the hardware see: 
* [Field Testing](https://github.com/Open360cam/360CamHardware/wiki/Field-Testing)

Code description:

File | Description 
--- | --- | ---
[Live2CameraDisplay.py](https://github.com/Open360cam/360CamCode/blob/master/Live2CameraDisplay.py) | Live display from two cameras at 800 x 600 resolution. Quits when 'q' is pressed
[FullSizeSnapShot.py](https://github.com/Open360cam/360CamCode/blob/master/FullSizeSnapShot.py) | Live display and captures full res images from both cameras when 'q' is pressed
[FucusUtility.py](https://github.com/Open360cam/360CamCode/blob/master/FocusUtility.py) | Utility for setting lens focus. Crops central region and zooms display. Hit q to close

Current dependancie:

* http://opencv.org
 
Depedancies in progress:
* https://github.com/ktossell/libuvc.git
* https://github.com/pupil-labs/pyuvc.git  (Python UVC)

![V0.02 Prototype](http://i.imgur.com/UVtXb0tm.jpg?1)
![](http://i.imgur.com/9lv8rzXm.jpg)

