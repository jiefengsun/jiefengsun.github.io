Title: Teaching
Date: 2020-05-18 08:00
Modified: 2021-10-01 08:00
sortorder: 05

##  MECH 564: Fundamentals of Robot Mechanics and Controls

The robotics class is my favorite class so far, and *I was the TA of the class for two years and then instructor of the class for the third year*. To better help the student understand the derivation in the lecture, I developed a series of labs using Matlab to derive the equations in the textbook and then simulate/control robotic manipulators. Thanks to my advisor Dr. Jianguo Zhao's great support during the development of the new course material and thanks to my students who provided numerous good suggestions to help me improve the contents. 


- Textbook: Robot Modeling and Control. Author: Mark W. Spong, Seth Hutchinson, M. Vidyasagar Publisher: Hoboken, NJ : John Wiley & Sons, 2006.
- Reference Book: [Robotics, Vision and Control, By Peter Corke](https://link.springer.com/book/10.1007%2F978-3-319-54413-7)
- Office hour: Monday, Wednesday: 4:15pm-5:15pm

#### Course Contents

1. Introduction to robotics.
2. Robot modeling: Homogeneous representations; Position kinematics, Velocity kinematics (Jacobian).
3. Robot motion planning: Motion representation; Path and trajectory planning
4. Robot dynamics: Euler-Lagrange method for dynamics equation
5. Robot motion control: Joint space approach; Task space approach; Computed torque control.
6. Advanced topics: vision-based control (visual servoing), biologically inspired robotics

#### Final Grade

- Homework                  25%
- Mid Term                  20%
- Final Exam                30%
- Labs                      25%


#### Labs



I believe that students will be better motivated if they can derive the complicated and tedious equations with advanced tools and can visualize the results with a step-by-step coding guide.

After three years of being the TA and then the instructor of the robotics class, I decided to design four labs/tutorials that uses Matlab as a simulation tool to help students simulate and finally simulate and control a Puma 560 robot tracking a circle.

Existing toolboxes such as [Robotic Toolbox by Robotics by Peter Corke](https://link.springer.com/book/10.1007%2F978-3-319-54413-7) can be used to verify our results. 

The labs include the lab handout, demo code, and homework. I will post some recorded lectures later.  Educators can obtain the answers to the homework by reaching out to me.

1. [Lab 1: Introduction to Matlab and Rotational Matrix Manipulation]({static}/images/teaching/robotics-lab1.html)

	- Learn the structures of data and commands in MATLAB™.
	- Gain knowledge and familiarity with the MATLAB™ interfaces (command prompt, script files, M-files, and functions)
	- Learn the ways to get help with MATLAB™ (help command, html help, Google)
	- Solve some example mathematics problems with MATLAB™, and plot the solutions
	- Practice manipulation of rotation and homogeneous transformation matrix
	- Compare MATLAB™ to your Python, C, FORTRAN, MathCAD, Pascal, BASIC… programming experiences

1. [Lab 2: Position and Velocity Kinematics]({static}/images/teaching/robotics-lab2.html)

	- Symbolic Toolbox
	- Derive forward Position/Velocity Kinematics Programming
	- Forward kinematics of a two-link robot. 

1. [Lab 3: Solving Robotics Dynamics]({static}/images/teaching/robotics-lab3.html)

	- Introduction to ODE solving 
	- Use MATLAB ODE solvers to solve sample ODEs. 
	- Solve robotics dynamics (a two link robot and a Puma 560 robot)

<!-- 1. [Lab 4:  Task Level Control of Robotic Manipulator ]({static}/images/teaching/robotics-lab4.html) [The answer of lab 3 homework is removed]

	- Code debuging techniques. Correct your lab 3. 
	- Task level controller. 
	- Tips for the lab 4 homework.  -->




