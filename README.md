# Bayes-filter

In this problem, we are given a robot operating in a 2D grid world. Every cell in the grid world is characterized by a color (0 or 1). The robot is equipped with a noisy odometer and a noisy color sensor. Given a stream of actions and corresponding observations, a Bayes filter is implemented to keep track of the robot’s current position. The sensor reads the color of the cell of the grid world correctly with probability 0.9 and incorrectly with probability 0.1. At each step, the robot can take an action to move in 4 directions (north, east, south, west). Execution of these actions is noisy, so after the robot performs this action, it actually makes the move with probability 0.9 and stays at the same spot without moving with probability 0.1. When the robot is at the edge of the grid world and is tasked with executing an action that would take it outside the boundaries of the grid world, the robot remains in the same state with probability 1. 

Initially, uniform prior is assumed on all states. 
<!-- 
# Transition matrices:
Trajectory and flight path | A* Path, Waypoints, and Trajectory | Position vs Time plot | 
--- | --- | --- | ---
![21e6f494-a303-4ab3-a6dd-37c47b201980](https://user-images.githubusercontent.com/68454938/224440295-287aad1f-1925-49dd-ad02-a0ca440a9d93.png) |
![423cc7e8-836d-40cf-8063-b2359bcecb1b](https://user-images.githubusercontent.com/68454938/224440304-a6d7a6b0-9fa7-4cc3-bedb-89fad3d52815.png)| ![0917c84f-da17-4ea9-a7db-ca3b2079ed8b](https://user-images.githubusercontent.com/68454938/224440315-1d67cbbf-1a64-484e-8b6d-46070a979caf.png) | ![6c190f97-d406-4382-b0d7-e2cafbca7a3b](https://user-images.githubusercontent.com/68454938/224440323-ca0f68aa-e782-4e12-a58c-0b70f1d63004.png)
 -->
