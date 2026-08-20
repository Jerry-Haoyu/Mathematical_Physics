# Complex Integrals
In lieu with the flow field interpretation of complex functions, generalizing the line integral for complex functions is very natural:
:::{prf:definition} Complex Integral
Let $f:\mathbb{C}\to \mathbb{C}$ be a continous complex function and $\Gamma$ is a smooth path in $\mathbb{C}$, then the limit on the R.H.S exists and we define the L.H.S
integral by the limit.
$$\int_{\Gamma} f(z)dz:=\lim_{\Delta z_i\to 0}\sum f(\xi_i)(z_{i+1}-z_i)$$
where $\xi_i \in (z_i,z_{i+1})$
:::
We can compte the integral by computing two standard real line integrals:
$$
\int_{\Gamma} f(z)dz &=\int_{\Gamma} (u+iv)(dx+idy) \\
&=\int_{\Gamma} (udx-vdy) + i\int_{\Gamma} (vdx+udy)
$$
We can define $A=(u,-v)$ and $B=(v,u)$ and $r=(dx,dy)$:
$$
\int_{\Gamma} f(z)dz = \int_{\Gamma} A\cdot dr + i\int_{\Gamma}B\cdot dr
$$