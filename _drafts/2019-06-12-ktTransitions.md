---
layout: article
title: Meriam-Wagner and KT transitions
author: adam
---

I'll show you the proof, but before that I want to give you a plausibility argument for it.

Consider our prototypical 2D system-- the XY model. Now, imagine rotating every spin by some angle $\delta$. 

fig1(show spin)  fig2(rotate every spin, different color).

Now, we ask ourselves the million-dollar question: would the physics of this system change?

The answer is no. State 1 will evolve completely the same as State 2 as long as interactions are local (every spin only seeing its neighbors).

Because of this, we know that the thing that controls the time-dynamics of our system, the Hamiltonian H, has to be invariant under global rotations of the angle (it commutes with the 2D rotation operator). If the Hamiltonian is invariant with respect to global rotations, then we know that it costs zero energy to preform this little sleight of hand. 

Now, a global rotation is also just a really, really long distance spin wave (in a very broad sense). You move one spin, and every other spin in the entire universe moves with it. So, we can guess that spin waves is what's called a *soft-mode*: as the wavelength of a spinwave goes to infinity, so to does the energy of the wave.

Now, if we consider our system to be at some temperature, where thermal flucuations are causing spin waves to occur, we also have to realized that long spin waves cost very very little energy (based on our previous argument). These low-energy spin waves also extend very long distances, and will act to destroy any long-range order in the system. 

This is the essential element of the Meriam-Wagner theorem.


