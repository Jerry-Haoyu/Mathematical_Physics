# Wave Equation 
The $d$-dimensional wave equation is given by the form:
$$
u_{tt} = a^2 \nabla^2 u + f(\mathbf{x},t)
$$
where $u(\mathbf{x,t}): \mathbb{R}^d\times \mathbb{R}\to \mathbb{R}$.  
The one dimensional wave equation $u_{tt}=a^2u_{xx}$ very naturally arise in modeling of a *vibrating string*. 
## The Vibrating String 


Consider a horinzontally placed string with length $L$. We make the following assumptions

:::{attention} Assumptions
1. Suppose at equilibrium the tension is a constant $T$. As the string vibrate at small amplitude, we can assume at arbitrary  position the tension is a constant and takes the value of the equilibrium tension $T$. 
2. The string vibrates in the vertical direction, i.e., no horizontal stretching 
3. Let $\rho(x)$ be the density distribution of the string.


:::
Now to model the vibration mathematically, **we place the string along the $x$-axis, let $u(x,t)$ be the vertical displacement of the string at position $x$ from equilibrium position at time $t$.**
### The Lagrangian Way 
It's clear that the kinetic energy of the string should be given by:
$$
K=\frac{1}{2}\int_0^L mu_tdx
$$