# Euler-Lagrange Equation 

## Differential Equation from Physics
A lot of physical science and engineering is about finding a reduction from a physical problem to differential equations. The newtownian way is to zoom into some local point of the system and derive a set of constraint that holds in the neighborhood. In the case of the vibration of a string, for example, we would find some local segment of string and analyze the tension that acts on it:
$$
T(\sin(\theta_1)-\sin(\theta_2)) = m\frac{\partial^2 u}{\partial t^2}
$$
where $u$ is the vertical displacement from equilibrium. We then take the calculus limit and find out that locally the accelearation of the vertical displacement should be proportional to the curvature. Hence the one-dimensional wave equation:
$$
\frac{\partial^2 u}{\partial t^2}=a^2 \frac{\partial^2 u}{\partial x^2}
$$[^pp]

The Lagrangian way is the opposite, we recognize some global objective the system need to be optimized toward, i.e., minimizing the lagragian $L=T-V$ where $T$ is *kinetic energy* and $V$ is *potential energy*. Then, by introduce some perturbation, we extract a constraint which also manifest itself as a differential equation. The following sections descirbes this process in detail. 

:::{attention} Newtonian and Lagrangian Mechanics
- Newtonian mechanics compute the balance of forces locally and obtain differential equation through $$F=m\frac{d^2\mathbf{x}}{dt^2}$$
- Lagrangian mechanics translate the physics into some global optimization problem  and reduce to differential equation through the Euler-Lagrange equation 
  $$
    \frac{\partial L}{\partial y}- \frac{d}{dx}\frac{\partial L}{\partial y'}=0
  $$

:::


## Functional : A global optimization objective
A functional in *calculus of variation* is a map from a function to a real number, i.e., $J:C^{\infty} \to \mathbb{R}$. In particular, it mostly comes in some sort of a integral. The simplest form being analgous to that of the lagrangian:

:::{math}
:label: basicfunctional
J[y] = \int_{x_1}^{x_2} f(x,y,y')dx
:::

The above example suffice to establish the explict connection of {ref}`basicfunctional`to Lagrangian: 
:::{prf:example} The lagrangian for the vibrating string
Let $u$ be deviation from the equilibrium position 
1. **The kinetic energy**: 
   $$
        T=\frac{1}{2}\int_{0}^L \rho u_t(x,t)dx
   $$
   where $L$ is the length of the string 
2. **The potential energy**:
    $$
        V=\frac{1}{2}k\int_{0}^L {1+u_x^2} dx
    $$[^pe]

The lagrangian is hence:
$$
L=\int_0^L \frac{1}{2} \left(\rho u_t(x,t) - k(1+u_x^2)\right)
$$
:::{figure} media/vs.png
The potential energy of a vibrating string. 

:::

It sometimes also appears to be more complex, for instance, 
1. **Depedence on mutliple independent variable**
   $$
   J[y] = \int_{\Omega} f(x_1,x_2,...,x_n, y, y_{x_1},y_{x_2},...,y_{x_n}) d{\mathbf{x}}
   $$
   where $\Omega \subset \mathbb{R}^n$
2. **Dependence on higher derivatives**
    :::{math} 
    :label: hdfunctional
        J[y] = \int_{x_1}^{x_2} f(x,y,y^{(1)},y^{(2)},...,y^{(m)})dx
    :::
3. **Multiple Dependent Variable**
    The three ways of extending the {ref}`basicfunctional` can of course, be mixed. 

We now scrutinize how exactly we optimize {ref}`hdfunctional`.

## Euler-Lagrange Equation
:::{prf:theorem} Euler-Lagrange Equation
$y$ is a stationary point for 
$$
J[y] = \int_{x_1}^{x_2} f(x,y,y^{(1)},...,y^{(n)})dx
$$
iff:
$$
\boxed{\frac{\partial f}{\partial y} -\sum_{j\geq 1} \frac{d}{dx}\frac{\partial f}{\partial y^{(j)}}=0}
$$
The boxed equation is known as the **Euler-Lagrange Equation**
:::


## First Integral
:::{prf:definition} First Integral
Suppose 
$$
    y^{(n)}=f(x,y,y^{(1)},...,y^{(n-1)})
$$

is an ordinary differential equation of order $n$. We can define an equivalent $n$-dimensional system by letting:
$$
y_1 &= y \\
y_2 &= y^{(1)} \\
\vdots \\
y_{n} &= y^{(n-1)}
$$
Denote by:
$$
\frac{dy_i}{dx}=f_i(x,y_1,...,y_n)
$$
Now suppose $f$ is:
   1. Continous about $x,y_1,...,y_n$
   2. Continuously differentialbe about $y_1,...,y_n$
   
Define  the *first integral* of the $n^{\text{th}}$-order problem to be a function $I=I(x,y_1,...,y_n)$ that also satisfies the above two requirements , and furthermore has the definitive property:
$$
I(x,y_1,...,y_n)=\text{Constant}
$$
along solution curves $\Gamma=(y_1(x),y_2(x),...,y_n(x))$ with the constant determined by the solution curve.
:::



We are confronted by the higher-order ordinary differential equation:
:::{math}
:label: ele
\frac{\partial f}{\partial y} -\frac{d}{dx}\left( \frac{\partial f}{\partial y}\right)=0
:::
The compute the first integral of this equation is to rewrite the above to obtain an equation of the form:
$$
\frac{d}{dt}I(x,y,y',...)=0
$$
The strategy is to compute the difference between {ref}`ele` and the exact differential:
$$
\frac{df}{dx}=\frac{\partial f}{\partial x} + \sum_{j\geq 0}\frac{\partial f}{\partial y^{(j)}}\frac{dy^{(j)}}{dx}=\frac{\partial f}{\partial x} +\frac{\partial f}{\partial y}\frac{dy}{dx}+\frac{\partial f}{\partial y^{(1)}}\frac{dy^{(1)}}{dx}+\cdots 
$$
If we multiply {ref}`ele` by $y'$ and subtract the two equations we get:

$$
\frac{df}{dx}-y'\left\{\frac{\partial f}{\partial y} - \frac{d}{dx}\left( \frac{\partial f}{\partial y'}\right)\right\} =\frac{\partial f}{\partial x} + \textcolor{cyan}{y''\frac{\partial f}{\partial y'}+ y'\frac{d}{dx}\left( \frac{\partial f}{\partial y'}\right)}-\sum_{j\geq 2}\frac{\partial f}{\partial y^{(j)}}\frac{dy^{(j)}}{dx}
$$
:::{tip} The particular form that allows easy first integral
If we assume $f$ is only dependent on $y,y'$, the above becomes $f(y,y')$, then 
$$
\sum_{j\geq 2}\frac{\partial f}{\partial y^{(j)}}\frac{dy^{(j)}}{dx} &= 0\\ 
\frac{\partial f}{\partial x} &=0
$$
:::
Now:
$$
\frac{df}{dx}-\underbrace{y'\left\{\frac{\partial f}{\partial y} - \frac{d}{dx}\left( \frac{\partial f}{\partial y'}\right)\right\}}_{0}&= \frac{d}{dx}\left(y'\frac{\partial f}{\partial y'}\right)
$$
Hence:
$$
\frac{d}{dx}\left(f-y'\frac{\partial f}{\partial y'}\right)=0
$$
We have sucesfully obtained the first inetgral:
$$
I(y,y)=f-y'\frac{\partial f}{\partial y'}
$$




## Exercises 
### Euler-Lagrange Equation for Multiple Independent Variables
**Prove** that:
:::{prf:theorem} Euler-Lagrange Equation
Consider the functional 
$$
J[y]=\int f(x_1,x_2,...,x_n,y_{x_1},y_{x_2},...,y_{x_n})d\mathbf{x}
$$
Show that the stationary is acheived iff:
$$
\frac{\partial f}{\partial y} - \sum_{i}\frac{d}{dx}\left(\frac{\partial f}{\partial y_{x_i}}\right)
$$
:::

---


### Fermat's Principle [^fp]
:::{note} Fermat's Principle 
The path taken by a ray of light between any two point makes stationary the travel time between those points. 
:::
We also define:
:::{prf:definition} Refractive Index
A medium is characterized by the speed of light traveling through. Specifically, the refractive index is defined by $n=\frac{c}{\text{speed of light traveling in the medium}}$
:::

:::{attention} **Problem 1** Light Propagtes in Straight Line in Homogenous Media
1. **Show that light propagates along a stragiht line in homogenous media.**
:::

:::{tip} *Solution*
:class: dropdown
Since $n$ is independent of position in homogenous media, make stationary the travel time is equivalent to make stationary the length of the path taken. Now the problem is equivalent to optimizing:
$$
\int_{x_1}^{x_2} \sqrt{1+y'^2}dx
$$
Note:
$$
f_y = 0 \quad f_y' = \frac{y'}{\sqrt{1+y'^2}}
$$
The Euler-Lagrange equation is, therefore:
$$
    \frac{}{}
    \frac{d}{dx}\left[ \frac{y'}{\sqrt{1+y'^2}}\right] &= 0 \\
    \frac{y'}{\sqrt{1+y'^2}} &= C_1
$$
Note the L.H.S is a non-constant function of $y'$, hence:
$$
y'= C_2 \Longrightarrow y=C_2x+C_3
$$
:::

:::{attention} **Problem 2** Snell's Law 
Consider the propagation of light from a flat slab of glass of refractive index $n_1$ into to
another with refractive index $n_2$. By examining paths that need not be differentiable
at the flat interface, establish Snell’s law: 
$$
n_1\sin(\theta_1) = n_2\sin(\theta_2)
$$
:::

:::{tip} *Solution*
:class: dropdown
We consider the first point at $(x_1, 0)$, the second point at $(x_2,y_2)$ where $x_1<0<x_2$. The time taken is hence:
$$
\int_{x_1}^{x_2} \frac{1}{v(x)}\sqrt{1+y'^2}dx
$$
where:
$$v(x)=
\begin{cases}
    c/n_1 &\text{if } x<0 \\
    c/n_2 &\text{if } x>0
\end{cases}
$$
The Euler-Lagrange equation is:
$$
0 + \frac{d}{dx}\left( \frac{y'}{v(x)\sqrt{1+y'^2}} \right)=0
$$
Hence:
$$
 \frac{y'}{v(x)\sqrt{1+y'^2}} =C
$$
For $x<0$, we have:
$$
 \frac{1}{v(x)}\frac{y'}{\sqrt{1+y'^2}} = \frac{n_1}{c}\sin(\theta_1) = C_1
$$
For $x>0$, we have:
$$
 \frac{1}{v(x)}\frac{y'}{\sqrt{1+y'^2}} = \frac{n_2}{c}\sin(\theta_2) = C_2
$$
Hence:
$$
n_1\sin(\theta_1)=n_2\sin(\theta_2)
$$
**Question:** If we flip the axis we would get $n_1\cos\theta_1=n_2\cos\theta_2$, why is that wrong?
:::


:::{attention} **Problem 3** General Snell's law
 A planar light ray propagates in an layered medium with refractive index $n(x)$. Use Fermat’s principle to establish a generalized Snell’s law:
$$
n(x)\sin(\psi(x))=\text{constant}
$$
by finding the equation for stationary paths for
$$
F_1=\int n(x)\sqrt{1+y'^2}dx
$$
(Here the prime denotes differentiation with respect to x.) Repeat this exercise with $x,y$ swapped by finding a similar equation for the stationary paths of
$$
F_2=\int n(y)\sqrt{1+y'^2}dx
$$
By using suitable definitions of the angle of incidence $\psi$, in each case show that the two formulations of the problem of a layered medium give physically equivalent answers.
(In the second formulation you will find it easiest to use the first integral.)
:::


### Drums and Membranes [^fp]
The shape of a distorted drumskin is described by the
function $h(x, y)$, which gives the height to which the point $(x, y)$ of the flat undistorted drumskin is displaced.

:::{attention} **Problem 1** Area of distorted drumskin
Show that the area of the distorted drumskin is equal to 
$$
A[h] = \int dxdy \sqrt{1 + \partial_x h^2 + \partial_y h^2}
$$
:::
:::{tip} *Solution* 
:class: dropdown
Consider the area differntial $dA=ds_x ds_y$ where $ds_x=\sqrt{1+\partial_x h^2}dx$ and $ds_y=\sqrt{1+\partial_y h^2}dy$ hence 
$$dA=\sqrt{1+\partial_x h^2 + \partial_y h^2 + (\partial_x h\partial_y h)^2}dxdy$$
since $\partial_x h\partial_y h\in \mathcal{O}(d\rho^2)$ where $d\rho = \sqrt{dx^2 + dy^2}$ we can drop it. As desired. 
:::

:::{attention} Area for small distortion
 Show that for small distortions, the area reduces to
 :::{math}
 :label: afsd
    A[h]=\frac{1}{2}\int dxdy |\nabla h|^2 + \text{constant} 

:::

:::{tip} *Solution*
:class: dropdown
Recall the generalized binomial theorem:
$$
(1+x)^{\alpha}=1+\alpha x + \frac{\alpha(\alpha-1)}{2!}x^2+\cdots + \frac{\alpha(\alpha-1)...(\alpha-n+1)}{n!}x^n + \cdots 
$$
for $|x|<1$. 
As a result:
$$
(1+x)^{1/2}=1+\frac12 x + \mathcal{O}(x^2)
$$
Assume a small perturbation, in particular, assume $|\nabla h|^2 \ll 1$, then
$$
\sqrt{1+|\nabla h|^2} = 1 + \frac12 |\nabla h|^2 +  \mathcal{O}(|\nabla h|^4)
$$
As a result,
$$
A[h]=\frac12 \int dxdy |\nabla h|^2 + \underbrace{\int dxdy}_{\text{constant}}
$$

:::

:::{attention} **Problem 3**  
Show that if $h$ satisfies the two-dimensional Laplace equation then $A$ is stationary with
respect to variations that vanish at the boundary.
:::

:::{tip} *Solution*
:class: dropdown
We need that the Euler-Lagrange equation for {ref}`afsd` is equivlanet to the tow-dimensional Laplace equation. That is simple: let $f(x,y,h, h_x,h_y)=h_x^2 + h_y^2$,
$$
\frac{\partial f}{\partial h} + \frac{d}{dx}\left(\frac{\partial f}{\partial h_x}\right) + \frac{d}{dy}\left(\frac{\partial f}{\partial h_y}\right) &= 0 \\
 0 + 2\left(\frac{dh_x}{dx} +  \frac{dh_x}{dx}\right) &= 0\\
 \nabla^2 h &=0
$$
:::

:::{attention} **Problem 4**  
 Suppose the drumskin has mass $\rho_0$ per unit area, and surface tension $T$. Write down
the Lagrangian controlling the motion of the drumskin and derive the equation of
motion that follows from it.
:::

:::{tip} *Solution*
:class: dropdown
The kinetic term is given by:
$$
T=\frac12 \int_{\Omega} dxdy \rho_0h_t^2
$$

The potential term is: [^st]
$$
    V=\int_{\Omega} dxdy T|\nabla h|^2
$$

Hence the lagrangian is:
$$
L &= T-V \\
&= \int_{\Omega} dxdy \left\{\frac12 \rho_0h_t^2 - T|\nabla h|^2 \right\}
$$

Computing the various derivatives:
$$
\frac{\partial L}{\partial h}=0 \quad \frac{\partial L}{\partial h_t}=\rho_0 h_t \quad \frac{\partial L}{\partial h_x}=-2Th_{x} \quad \frac{\partial L}{\partial h_y}=-2Th_{y}
$$
:::



[^pp]: Here $a$ is a physical parameter intrinsic to the string, i.e., $\sqrt{T}{\rho}$ where $T$ is the tension at equilibrium adn $\rho$ is the density.

[^pe]: It is tempting for some of us who are not trained as a physics student to write the potential energy as $\frac12 \left(\int_a^b \sqrt{1+u_x^2}dx\right)^2$. The rationale is as follows: if we pause at a moment and straigten the vibrating string as a line. Then we observe how much elongation had happened and use hooke's law on the entire string. This is physically wrong since the elongation happens inhomogenously hence we have to apply hooke's law locally and integrate. Also mathematically, 
$$
\left(\int f\right)^2 =\int f^2 
$$
iff $f$ is some constant function. The general relatinoship can be obtained from Cauchy-Shwarz inequality by taking $f=\sqrt{1+u_x^2}$ and $g=1$
$$
\left(\int_0^L \sqrt{1+u_x^2}\right)^2 \leq \int_0^L 1+u_x^2 dx
$$

[^fp]: From Dr. P.Draper's homework problems for PHYS 508(*Mathematical Physics I*) at UIUC.
[^st]: The key to solve this problem is actually to realize that surface tension has the dimension $[F]/[L]=[E]/[L]^2$, in otherword, surface tension is precisely the perunit potential energy due to "stretching"/"distorsion" by construction. 