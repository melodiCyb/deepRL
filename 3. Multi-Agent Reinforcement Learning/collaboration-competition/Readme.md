## Report

In this environment two agents plays tennis by controlling rackets. Each agent tries to bounce a ball over a net and receives a reward of 0.1 for each success. Otherwise, if an agent cannot catch the ball or throws away, it receives a negative reward -0.01. In this setting, each agent tries to keep the ball in play.

* **Size of the observation space:** 8. 
* **Variables:** Position and velocity of the ball and racket.
* **Actions:**  There are two continous actions consisting to movement toward (or away from)  the net and jumping.
* **Task type:** Episodic.
* **Goal:** Achieving more than 0.5 average scores over 100 episodes to consider the environment is solved.


Each agents has its local observation. After each episode, without using discounting, we add rewards from each agent to obtain their scores and then take the maximum of two scores yielding a single score for each episode. 



## Directory Tree

         .
        ├── Report3.ipynb.                   # Walkthrough jupyter notebook      
        │── Tennis.ipynb                     # Project report
        │── agent_0_actor_checkpoint.pth     # Trained actor model for agent_0
        │── agent_0_critic_checkpoint.pth    # Trained critic model for agent_0
        │── agent_1_actor_checkpoint.pth     # Trained actor model for agent_1
        │──  agent_1_critic_checkpoint.pth    # Trained critic model for agent_1
        │── ddpg_agent.py                   # Contains Agent Class
        │── model.py                     # Contains Actor-Critic model class 
        │── p3_scores.png                # plot of rewards
        └── Readme.md
## Setup 

1. You can download the pre-built Unity environment from the links below: 

* [Linux](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P3/Tennis/Tennis_Linux.zip)
* [Mac OSX](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P3/Tennis/Tennis.app.zip)
* [Windows (32-bit)](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P3/Tennis/Tennis_Windows_x86.zip)
* [Windows (64-bit)](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P3/Tennis/Tennis_Windows_x86_64.zip)

Then, place the file in the project folder and unzip the file. 


2. Then please follow instructions given in this [link](https://github.com/udacity/deep-reinforcement-learning#dependencies) to setup the Python Environment.

## Usage

To reproduce results Tennis.ipynb should be used. It uses Agent and Actor&Critic classes given in ddpg_agent.py and model.py scripts. 