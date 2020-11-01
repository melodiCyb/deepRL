


## Description

In this environment, we are given a double-jointed arm can move to target locations. For each time step, if agent's hand is in the target location 0.1 reward is provided. The agent tries to maintain its poisiton at this goal location as long as possible. 


* **Size of the observation space:** 33
* **Variables:** Position, rotation, velocity, and angular velocities of the arm
* **Actions:**  Each action is a vector with four numbers, corresponding to torque applicable to two joints. Every entry in the action vector should be a number between -1 and 1.
* **Task type:** Episodic.
* **Goal:** Achieving more than 30 average scores over 100 episodes to consider the environment is solved.




## Directory Tree

         .
        ├── Report2.ipynb.                   # Walkthrough jupyter notebook      
        │── Continuous_Control.ipynb           # Project report
        │── actor_checkpoint.pth             # Trained actor model 
        │── critic_checkpoint.pth            # Trained critic model
        │── ddpg_agent.py                   # Contains Agent Class
        │── model.py                     # Contains Actor-Critic model class 
        │── p2_scores.png                # plot of rewards
        └── Readme.md
## Setup 

1. You can download the pre-built Unity environment from the links below: 


 **_Version 1: One (1) Agent_**
  * [Linux](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/one_agent/Reacher_Linux.zip)
  * [Mac OSX](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/one_agent/Reacher.app.zip)
 * [Windows (32-bit)](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/one_agent/Reacher_Windows_x86.zip)
   * [Windows (64-bit)](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/one_agent/Reacher_Windows_x86_64.zip)


Then, place the file in the project folder and unzip the file. 


2. Then please follow instructions given in this [link](https://github.com/udacity/deep-reinforcement-learning#dependencies) to setup the Python Environment.

## Usage

To reproduce results Continous_Control.ipynb should be used. It uses Agent and Actor&Critic classes given in ddpg_agent.py and model.py scripts. 