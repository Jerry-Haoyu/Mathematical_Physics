---
kernelspec:
  name: python3
  display_name: 'Python 3'
---

# Poisson Equation 
:::{tip} Interactive Visualization !
This notebook contain interactive visualization that needs binder connection. Please click the **power button on the top right corner** before you start reading ! Establishing the connection and building the container takes a while, so clicking it before you read would make sure the interactive code to be ready to run when you scroll on to them.
:::
## 2D Poisson Equation 
Let $\Omega \subset \mathbb{R}^2$, we consider the Poisson equation with homogenous boundary condition:
:::{prf:definition} 2D Poisson Equation with Homogenous Boundary Condition
:::{math} 
:label: 2dpoihb
  -\Delta u &= f(x,y) \qquad (x,y)\in \Omega \\
  u(x,y) &= 0 \qquad (x,y)\in \Gamma_1 \\
  \frac{\partial u}{\partial \nu}(x,y) &= 0 \qquad (x,y)\in \Gamma_1
:::
where $\Gamma_1\cup \Gamma_2 = \partial \Omega$ such that both $\Gamma_1, \Gamma_2$ is measure-zero. $\nu$ is the outward normal vector.


## Spectral Method 
Let $$
u(x,y)=\int_{-\infty<\omega_1,\omega_2<\infty>>}\left\{\int_{-\infty<x,y<\infty}f(x,y) \exp(-i(\omega_1x+\omega_2y)) \right \}
$$



## Finite-Element Method(FEM)
### The Tent Function 
We consider the 

#### Viualizing the Tent Basis 
:::{tip} 
If you have not do so, click the power button on the top right corner. 
After everything builds up, you can click the start button ▶️. You should see two sliders showing up below.
- The resolution slider determines how "dense" these tent basis are in filling the domain. Lower resolution means larger and less tents and vice versa. 
- The position slider let you adjust which particular basis function you are watching. In otherword, where the "tent" is located in the domain $\Omega$ 
:::
```{code-cell} 
:tags: ["hide-input"]
import sys
from pathlib import Path
import ipywidgets as wdgt

sys.path.append("src")

from src.twoDPoissonFEM import twoDPoisson

slider_resol = wdgt.FloatSlider(value=3.0, min=1.0, max=6.0, step=1.0)
slider_pos = wdgt.FloatSlider(value=0.0, min=0.0, max=36.0, step=1.0)

def plot(resolution, position):
    resolution, position = int(resolution), int(position)
    solver = twoDPoisson(0,10.0,0,10.0,resolution=resolution, f=lambda x : x)
    if position < resolution * resolution:
        tent_basis = solver.get_basis(position)
        fig, ax = solver.init_plot()
        ax.scatter(solver.grid_x, solver.grid_y, color='red')
        ax.plot_surface(solver.basis_x, solver.basis_y, tent_basis, cmap='coolwarm')

wdgt.interactive(plot, resolution=slider_resol, position=slider_pos)
```


<!-- We define:
:::{prf:definition} Dirchlet Integral
Let $u\in C^2(\Omega), v\in C^{\infty}(\Omega)$, define the bilinear form on $H^1(\Omega)$ to be
$$
a(u,v) := \int_{\Omega}\nabla u \nabla v
$$
::: -->

We can show that:
:::{prf:proposition} 
Suppose $u \in C^2(\bar \Omega)$ is a solution of {ref}`2dpoihb`, then $\forall v \in H^1_{\Gamma_1}(\Omega)$, we have:
$$
\int_{\Omega}\nabla u \nabla v=\int_{\Omega} fv
$$
:::
:::{prf:proof}
We first show *Green's Formula*(change of variable):
$$
\int_{\Omega}v \Delta u = \int_{\partial \Omega} v \frac{\partial u}{\partial \nu} - \int_{\Omega} \nabla u \nabla v
$$
:::

This motivates us to define a solution in a weaker sense. Since $a(u,v)=(f,v)$ is a necessary condition of $u$, how about making every $u$ that satisfies this equation a "weak solution"(or generalized solution)?

We first define the space that our weak solution would reside:
$$
 H^1_{\Gamma_1}(\Omega)=\{f\in H^1(\Omega): f=0 \text{ on } \Gamma_1 \}
$$