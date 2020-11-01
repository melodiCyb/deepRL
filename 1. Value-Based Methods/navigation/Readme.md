

## Project Description

In this project, an agent lies in a square world and aims to collect yellow bananas and avoid blue bananas via adjusting its navigation. State space consist to the agent's velocity and ray-based perception of objects around the agent's forward direction. Our task is episodic and using the state space information together with the rewards given below, the agent trained to choose best actions to achieve an average score of +13 over 100 consecutive episodes.

Reward of yellow banana: +1
Reward of blue banana: -1
Dimension of the state space: 37
Available actions (discrete):

0 - move forward.
1 - move backward.
2 - turn left.
3 - turn right.

## Directory Tree

         .
        ├── Navigation.ipynb.            # Walkthrough jupyter notebook      
        │── Report.pdf                   # Project report
        │── checkpoint2.pth              # Trained model
        │── dqn_agent.py                 # Contains Agent Class
        │── model.py                     # Contains QNetwork class 
        │── p1_scores.png                # plot of rewards
        └── Readme.md
## Setup 

1. You can download the pre-built Unity environment from the links below: 

* [Linux](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux.zip)
* [Mac OSX](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana.app.zip)
* [Windows (32-bit)](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86.zip)
* [Windows (64-bit)](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86_64.zip)

Then, place the file in the project folder and unzip the file. 


2. To setup the Python Environment you follow the instructions given in this [link](https://github.com/udacity/deep-reinforcement-learning#dependencies).

## Usage

To reproduce results Navigation.ipynb should be used. It uses Agent and QNetwork classes given in dqn_agent.py and model.py scripts. 

