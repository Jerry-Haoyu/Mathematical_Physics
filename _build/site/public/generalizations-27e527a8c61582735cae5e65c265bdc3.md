# Generalizations 

This section focuses on more general cases. In particular, 
1. **Multiple Constraint**, i.e., in the case of 
$$
J=\int f(x,y_1,y_2,...,y_n,\dot y_1, \dot y_2,...,\dot y_n, \ddot y_1,...)
$$
2. **Variable Endpoints**
In previous cases, we used the key assumption that:
:::{attention} Fixed Endpoint Assumption
The perturbation $\delta y$ is $0$ at endpoints, hence all boundary/surface terms arising from integartion by parts may be ignored.
:::
We now relax this assumption but rather work out boundary conditions based on the stationary condition with variable endpoints. This assumption can in turn be applied to the resulting differential equations. 

3. **Constrained Optimization** Often, the minimization of the action is subjected to physcial constraint. For instance, in the famous *catenary problem*, we need to fix the length of the hanging chain. 

## Multiple Constraint 

## Variable Endpoints

## Constraint Optimization 
### Quadratic Form and The Sturm-Liouville Operator 
Consider the problem:
:::{note} Bilinear Form Optimization 
Let $x\in \mathbb{R}^n$, $A\in \mathbb{R^{n\times n}}$ is a **symmetric** matrix, define:
$$
F(x)=\frac12 \langle x,Ax \rangle
$$
Consider the optimization of $F$ constrained on $\|x\|^2=1$ 
:::

We use lagarange multiplier:
$$
(Ax)^T+x^TA-2\lambda x^T &=0 \\
Ax + A^Tx - 2\lambda x &=0 \\
2(A-\lambda I)x&=0 \\
Ax &= \lambda x
$$ 
[^diff]
Subjected to $\|x\|^2=1$. We note that this is an **eigenvalue problem**. Now we consider a special instantiation of $A$.

:::{prf:definition} Discrete Analog of Sturm-Liouville Opeartor 
Define the central-difference operator as:
$$
D=\begin{pmatrix}
1 & 0 & \color{blue}{-1} & 0 & \cdots & 0 \\
0 & 1 & 0 & \color{blue}{-1}  &\cdots & \vdots \\
\color{red}{-1} & 0 & 1 & 0 &\ddots &\vdots  \\
0 & \color{red}{-1} & 0 & \ddots & \ddots & \color{blue}{-1}\\
\vdots & \ddots & \ddots & \ddots & \ddots & 0 \\
0 & \cdots & 0 & \color{red}{-1} &  0 & 1
\end{pmatrix}
$$
which is a tridiagonal matrix with $1$ on the main diagonal and $-1$ on the subdiagonals. 
Define:
$$
L:= D
$$
:::

## Exercises
### Elastic Rods
:::{attention} Elastic Rods
- The **elastic energy per unit length** of a bent steel rod is given by $$\frac{1}{2}\frac{YI}{R^2}$$
Here Y is the *Young’s modulus* of the steel and $I$ is the moment of inertia of the rod’s cross section about an axis through its centroid and perpendicular to the plane in which the rod is bent. 

- Let us assume the rod is only slightly bent into the yz plane and lies close to the z axis. R is the radius of curvature due to the bending, related to the curvature by 
$$
\frac{1}{R}=\kappa = |T_z|
$$
where $T$ is the unit tangent vector to the rod. 

#### Problem 0

Show that the elastic energy can be approximated by:
$$
\boxed{U[y]=\int_0^L \frac12 \left\{ \frac{1}{2} YI(y'')^2 \right\}dz}
$$


#### Problem 1
The rod is used as a column which supports a compressive load $Mg$ directed along the z axis (which is vertical). Show that :

**(a)** when the rod buckles slightly (i.e. bends with both ends remaining on the z axis) the
total energy, including the gravitational potential energy of the loading mass M, can be
approximated by
$$
\boxed{U[y]=\int_0^L \left\{ \frac{YL}{2} (y'')^2 - \frac{Mg}{2}(y')^2\right\}dz}
$$

**(b)** By considering deformations of the form
$$
y(z)=\sum_{n=1}^{\infty} a_n\sin(\frac{n\pi z}{L})
$$
show that the column is unstable to buckling and collapse once 
$$
Mg \geq \frac{\pi^2}{L^2}YI
$$

#### 
:::


:::{tip} Solution to Problem 0 
:class: dropdown
We need a little lemma(or recall from Calculus I):
$$
\kappa = \frac{y''}{(1+y'^2)^{3/2}}
$$

For small perturbation $|y'|\ll 1 $ hence $(1+y'^2)^{\frac32} \approx 1$ hence
$
\kappa = \frac{1}{R}=(y'')
$. Squaring it we have :
$$
\frac{1}{R^2}=(y'')^2
$$
Hence:
$$
dU=\frac12 YI (y'')^2 dz
$$
Integrating get us the desired result.
:::{prf:proof} Proof of lemma
:class: dropdown
If we imagine we traverse along a curve $\Gamma$, the accelearation would be:
$$
r''(z) &= \frac{d}{dz}\left(\frac{dr}{dz}\right) \\
&=  \frac{d}{dz}\left(\frac{ds}{dz}T\right)  \\
&= \frac{d^2s}{dz^2}T + \frac{ds}{dz}\frac{dT}{dz}
$$
Note that $$\left\langle T, \frac{dT}{dz}\right\rangle=0$$
since $|T|=1$. Therefore $r''(z)$ can be decomposed to a tangential component $\frac{d^2s}{dz^2}T$ and a centrepetal component $\frac{ds}{dz}\frac{dT}{dz}$. 
Also, $\frac{dT}{dz}$ is co-linear with our quanitty of interest 
$$\frac{dT}{dz}=\frac{dT}{ds}\frac{ds}{dz}$$
Therefore:
$$
\boxed{r''(z)= \frac{d^2s}{dz^2}T + \left(\frac{ds}{dz}\right)^2 \frac{dT}{ds}}
$$
We can isolate the centrepetal component by apply a cross product:
$$
T\times r''(z) &= T \times \left(\frac{ds}{dz}\right)^2\frac{dT}{dz}
$$
Now :
1. (LHS) $T=(1,0,y')/ds$, hence $r''(z) = (0,0,y'')$. Hence the cross product is:
   $$
    \frac{1}{\sqrt{1+y'^2}} (1,0,y')^T \times (0,0,y'')  = \frac{1}{\sqrt{1+y'^2}}(0,y'',0)^T
   $$
2. (RHS) Since $T, \frac{dT}{dz}$ are orthogonal to each other and both lie in the x-z plane, we have:
   $$
    T \times \left(\frac{ds}{dz}\right)^2\frac{dT}{dz} =  \left(\frac{ds}{dz}\right)^2 \textcolor{brown}{\left|\frac{dT}{dz}\right|} (0,1,0)^T
   $$

Now combining the above two equations, we get:
$$
 \frac{y''}{\sqrt{1+y'^2}}=\left(\frac{ds}{dz}\right)^2  \left|\frac{dT}{dz}\right|
$$
As desired.


:::

:::{tip} Solution to Problem 1
:class: dropdown
:::{figure} media/euler_problem.png
(a) Consider the schemetic above. Suppose $y=0$ for $z\in (L-dL,L)$, then 
$$
L+dL&=\int_0^L \sqrt{1+y'^2}dz \\ 
&\approx \int_0^L 1 + \frac{1}{2}y'^2dz\\
&= L + \int_0^L \frac{1}{2}y'^2dz
$$
Hence $dL=\int_0^L \frac{1}{2}y'^2$. If we consider the gravitational potential energy to be $0$ at $h=L$, then the gravitational potential energy becomes:
$$
-\int_0^L \frac{1}{2}y'^2dz
$$
the negative sign is there to account for compression. Combining with the result from problem 0 we get as desired.


(b) The Euler-Lagrange equation for the total energy functional is:
$$
-\frac{d}{dx}\frac{\partial f}{\partial y'}+\frac{d^2}{dx^2}\frac{\partial f}{\partial y''} &= 0 \\
Mgy^{(2)}+YIy^{(4)} &= 0
$$

Consider a series solution of the form:
$$
y(z)=\sum_{n=1}^{\infty} a_n\sin(\omega_n z)
$$
where $\omega_n = \frac{n\pi}{L}$. We have:

$$
\widehat{\frac{\delta J}{\delta f}} &= \sum_{n=1}^{\infty}  b_n \sin(\omega_n z) \\
&= \sum_{n=1}^{\infty}\underbrace{a_n(YI\omega_n^4-Mg\omega_n^2)}_{b_n}\sin(\omega_n z)
$$

Hence a trivial solution is $a_n=0, \forall n\geq 1$ which corresponds to a *stable, stiff rod*. 

The rod buckles if, the trivial solution is no longer a local minimum, i.e., the hessian is no longer positive-definite. We need to find the hessian in this case.

Define the hessian in the spectral space as:

$$
\widehat H = 
\begin{pmatrix}
\frac{\partial b_{1}}{\partial a_1} & \frac{\partial b_{1}}{\partial a_2} & \cdots \\
\frac{\partial b_{2}}{\partial a_1} & \frac{\partial b_{2}}{\partial a_2} & \cdots \\
\vdots  & & \ddots \\
\end{pmatrix}
$$

which in our case is already diagonalized:

$$
\widehat H = \mathrm{diag}(\{(YI\omega_n^4-Mg\omega_n^2)\}_{n=1}^{\infty})
$$

Local minimum requires positive-definiteness, which is :
$$
YI\omega_n^4 - Mg\omega_n^2 &> 0  \\
M &< \frac{YI}{g}\omega_n^2 
$$

Picking $n=1$(smallest eigenvalue) satisfies the last inequality. 
$$
\boxed{M < \frac{YI\pi^2}{g L^2}}
$$

As desired. 
:::

[^diff]: In step 0, we computed the jacobian of $F:\mathbb{R}^n \to \mathbb{R}$ which is of shape $\mathbb{R}^{1\times n}$(a row vector). Recall that: $$
D_x\langle y_1(x), y_2(x) \rangle  = y_2^TD_xy_1 + y_1^T D_xy_2
$$