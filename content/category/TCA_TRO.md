Title: TCA TRO
Date: 2021-02-18 08:00
Modified: 2021-10-1 08:00
Category: Research Paper Support Info
Tags: TRO

## **A General Framework for Physics-based Modeling of various Twisted-and-Coiled Actuators**

### Introduction

This is the supporting page of the paper titled "Physics-based Modeling of Twisted-and-Coiled Actuators Using Cosserat Rod Theory" that is accepted and will be published on ** IEEE Transactions on Robotics**. You can download the preprint of the paper [here]({static}/pdfs/sun2022physics.pdf)

The purpose of this page is to help readers better understand our paper. It will be very helpful for readers who want to implement the simulation or use our model. 

It contains the following parts

- Supporting Multimedia

- Derivation using Matlab

- Simulation tutorial and source code

### Supporting Multimedia


<iframe width="480" height="360" src="https://www.youtube.com/embed/_2ka1khKXDw" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

* The supporting Multimedia provides a visible presentation of the simulation.


### Derivation using Matlab

Some derivations are pretty lengthy, and derivations using Matlab are provided to reduce the burden. To run the demos, please first download the [all subfunctions](https://github.com/jiefengsun/TCA_TRO/tree/main/01_functions). The source code of the derivation is also [available](https://github.com/jiefengsun/TCA_TRO). The source code is in .mlx (live script) format. 

- [Derive the reference strains and boundary conditions for a helical TCA]({static}/images/TRO/reference_strain_helix.html). It includes how to set up the $u^*$ and $v^*$. 

- [Derive the reference geometric curvature and torsion for a conical TCA]({static}/images/TRO/Conical_spiral.html).

- [Transform the external wrench to the body frame]({static}/images/TRO/wrench_transform.html). 

- [Derive using Love's equation]({static}/images/TRO/love_equation.html), it includes how we transform the wrench to the body frame from the global frame. 

- [Derive using "Infenitesmal Strain Theory"]({static}/images/TRO/CST_Rod.html), it is corresponding to Sec. III(B) in the paper. 

- [Derive directly using CST ]({static}/images/TRO/CST_direct.html), it is corresponding to Appendix III(C) in the paper. 

- [Derive the curvatre and the torsion of a conical TCA]({static}/images/TRO/Conical_spiral.html)

- For readers who do not have a Matlab environment, please go to [CodeOcean for an online demo](https://codeocean.com/capsule/2199241/tree). Please email me for any questions!
 

### Want to Learn More about the Rod Model?

Here are some resources to help you learn rod model

- [Dr. John Till's tutorial on Cosserat rod simulation from Dr. Caleb Rucker's group](https://github.com/JohnDTill/ContinuumRobotExamples). This is a good tutorial more focus on numerical implementation and is suitable for researchers with a background in robotics.
	
- [Dr. Oliver M. O’Reilly's website on Rode model formulation](https://rotations.berkeley.edu/site-information/). Good for researchers who have a background in (continuum) mechanics. It is more focused on the theoretical formulation. 

- [PyElastica from Gazzola Lab at UIUC](https://www.cosseratrods.org/#about). It explains the discrete elastic rod. The good thing is that they have implemented it in Python, which is free to run.

- Classic Books
	- Antman, Stuart S. "Problems in nonlinear elasticity." Nonlinear Problems of Elasticity (2005): 513-584.
	- Love, A. E. H., "A Treatise on the Mathematical Theory of Elasticity, 4th ed.", Cambridge University Press, Cambridge (1927).
	








