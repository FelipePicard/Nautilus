# README
These are the deliverables for Nautilus' recruitment process. Following this README you will find brief descriptions of all the repository's contents and instructions on how to use them. More explanations on how the codes work can be obtained by reading the comments on the individual codes.

## mult.py and fibonacci.py 
These python codes are targeted to solve project Euler's first and second problems, which can be found [here.](https://projecteuler.net)

### How to run it?
After cloning this repository, using the terminal, go to the correct folder and type `python mult.py` or `python fibonacci.py`

## championship.py
This deliverable had the goal of testing what we learned about object oriented programming and magic methods. The code should compare the number of points of the competitors and print a ranking based on this parameter.

### How to run it?
Create an object for your contestant (in this case they are surfers) as showed in the example. Don't forget to include their name, number of points, age, nationality, surfboard size and number of won championships.
Afterwards just run the code.

## talker.py, listener.py and oddlistener.py
Talker.py creates a talking node that communicates to a listener node (listener.py) by the same topic (channel). The oddlistener.py has both the talker and the listener in the same script, and sends numbers that increase by 1 each time, but only displays the odd numbers recovered by the listener.

### How to run it?
For these programs you will need to install ROS. A quick guide can be found [here.](http://wiki.ros.org/melodic/Installation/Ubuntu) After that,  you'll need to [create a workspace](http://wiki.ros.org/catkin/Tutorials/create_a_workspace) and add these codes to the `scirpts` folder you will make.

## solar_system


### How to run it?


## model/grabber11
This task evaluated our skills to assemble a "mechanical arm" in the simulation software Gazebo. The claw should open/close if a vertical force is applied to its piston.

### How to run it?


## nemo
Testing our knowledge of OpenCV. This code makes a color segmentation from a video of some clown-fish, generating a mask that only shows the fish's orange color. Very nice demo of what OpenCV can do.

### How to run it?
Just run it as you would do for any other code. Two windows should pop up. One with the original video and one with the masked one. If you have already installed ROS for the previous examples, you probably have OpenCV in your computer, so the code should run smoothly.
