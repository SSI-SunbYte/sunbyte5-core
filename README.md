# SunbYte V Core 

This is the main repository for the SunbYte 5 mission in which this repo contains:
- Sun tracking pub-sub system

---

# What the Project Is

- This program will create a publisher for a sun tracking system for the SunbYte V mission
- This allows the sun to be tracked and will publish the pixel offset for any subscribers to read from
---

# How It Works

- The program uses OpenCV to idenitfy the location on the sun in the current frame (frame provided via a webcam) and then calculates the offset of the sun in pixels which is then publshed
- The position of the sun in the frame is calculated using the hough circle algorithm which has its offset calculated from the centre of the frame 
- The publisher is setup using ROS2 to publish the calculated offset of the sun from the latest processed frame 

---

# Engineering Decisions

OpenCV and ROS2  in python was used for accomplishing this due to the ease of using python and openCV. C++ was considered for the programming language however was opted out of due to the sheer complexity of C++ compared to Python Python puts performance restrictionw on the program compared to C=+ due to it being an interpreted rather than compiled language but should be satisfactory for the project. ROS (v1) was considered but ultimatley dropped due to it reaching EOL as of May 2025


# Tech Stack

- Languages used: Python
- Frameworks/libraries: ROS2, OpenCV, NumPy

---

# How to Run the Project

- Prerequisites: OpenCV, NumPy, ROS2, Python
- How to start/run the project:
- Example commands:

---