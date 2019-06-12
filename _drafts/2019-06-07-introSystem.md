---
layout: article
title: Introduction to the XY Model
author: adam
---


If you are familiar with undergraduate physics, you can think of the XY model being a generalization of the 2D ising model, but instead of having spin-up or spin-down, you now have spin-all-around.

So why is it useful? Why are people interested in it?

The answer to these questions can be broadly lumped under two contexts.
## 1-Intrinsic Interest (mathematical physics)
Regardless of how well the XY model actually maps to anything in the real world, there is ongoing interest in studying it's fundamental properties. For instance, I was surprised (considering how old physics is) that the question of whether or not the XY dynamically scales was only really settled in the late-90s. (Brief digression, when I say something dynamically scales, I mean that there is one and only one length scale in the system and its evolution in time evolves
deterministically.)
Part of why the XY model is so interesting is because it is also so perverse. Things in 2D tend to be weird (see 2D turbulence where the energy cascade is inverted), and it generally involves logarithms (show results for 2D electrostatics, logarithmic divergence never goes to zero).

This can be formalized somewhat in the Merriam-Wagner theorem, which puts the weirdness of 2D on a more firm footing. 


But I'm just a dumb experimentalist, so I'm more interested in 2.

## 2-A Physical Model
It turns out you can map a lot of really interesting systems to the XY model. The behaviour of super-fluid helium, 2D electrostatics, etc. You can even map the Sine-Gordon equation to the XY model, making it a great toy model for those of us doing quantum field theory.

But we'll be focussing on (in my opinion) the most direct application of the XY model to a physical system: tilted smectic liquid crystals.

### tilted smectic [liquid crystals]
A liquid crystal is just how it sounds. It has crystalline order, but it also flows like a fluid. When you think of a crystal, you probably imagine something like graphene-- clear crisp platonic hexogons tiling the plane. This is an example of a crystal where the order parameter is related to space-- from a liquid to a crystal, the distance between neighboring atoms goes from being ambiguous to completely fixed.
However, you can also define other order parameters. For instance, if you weren't dealing with points (atoms) but with rods, you could ask, how well are my rods aligned? By dealing with order parameters that aren't directly related to spatial transformations, you can have an 'aligned' phase that still has the spatial structure and properties of a liquid.[:1]
nematic order parameter picture
### tilted [smectic liquid crystals]

A smectic liquid crystal has another twist to it. Not only is there an order parameter tracking the alignment of the molecular rods, but there is actually a spatial-order parameter! The smectic liquid crystal orders like a crystal along the z-axis. This still allows us the loophole that it can flow like fluid in the x-y plane.

This makes smectic liquid crytals particularly good 2D sandboxes[:2], because all the dynamics are confined to the 2D plane.
fig of smectic crystal
### [tilted smectic liquid crystals]

The final ingrediant in our realization of the XY model is the tilt. 

What would you see if you stared down the barrel of a pool noodle? You'd see a circle. The only way we can get the 'spin' of the XY model is to have an object that is somehow anisotropic. 

By tilting the pool noodle, we can define an object that is same as a spin (show how this is notated in films.)






