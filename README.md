TDPS

This paper presents a simple framework and data set, which provides the test source code of partio1 &amp; partio2 for the TDPS project, corresponding to the patrol task and the color recognition task respectively.

The image of the input algorithm is taken by the rasberry PI CSI camera. It is suggested that the original 500 W Camera with 640 x 480 pixels be used here. Their corresponding groundtruth is in the directory' gd'

You can collect your own images and mark their groundtruth for training.

But not all of the pixels need to be used. We use the method of intercepting some of the pixels to improve the speed of raspberry pie. (Applying the idea of PWM)

Note that this project only provides a framework for training and testing algorithms

video

videos that can be used to test the algorithm are collected. The predicted results will also be recorded.
