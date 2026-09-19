# Linear Differential Operator 

## The Formal Linear Differential Operator 
We define the differentian opeartor as:
:::{prf:definition} Differentiation Opeartor
Let $D:L^2[a,b]\to L^2[a,b]$ be the mapping defined by:
$$
D(u)=\frac{d}{dx}u
$$
for all $u\in L^2[a,b]$
:::
Now we can define the *formal linear operator* by some opeartor algebra:
:::{prf:definition} Formal linear differential operator
Let $p(x)$ be any polynomial over $\mathbb{C}$ of positive degree:
$$
p(x)=a_\nu x^\nu
$$
where $a_{\nu}$ are functions of $x$. Define $L:=p(D)$ as the **formal linear differential operator** that correspond to the **auxillary polynomial $p$**:
$$
L=a_\nu D^{\nu}
$$
The **order** of $L$ is given by the order of $p$.
:::
We call it *formal* since we want to contrast with *concrete* linear differential opeartor which is a formal opeartor endorsed with boundary conditions(This convention is used in *Mathematical Physics by Michael Stone and Paul Goldbart*). We can think of the difference between them as:
- The **nullspace of formal opeartor** is the space of general solution of homogenous diffferential equation 
- The **nullspace of concrete operator** is the space of particular solution to homogenous differential equation with boundary conditions

We'll explore the nullspace of formal operators with a bit more detail now.
### Nullspace of formal operator 
We first observe something very nice about solutions to homogenous differential equations: they belong to $C^{\infty}$(infinitely differentiable). 
#### The Bootstrapping Lemma 
:::{prf:lemma} 
Let $L$ be a formal operator of order $n$. Suppose the coefficients of the auxillary polynomial are $k$ times continously differentiable($a_{\nu}\in C^k$) then $\forall y\in \mathrm{Null}(L)$, $y$ is at least $k+n$ times contiously differentiable.
:::
:::{prf:proof}
Suppose $y\in \mathrm{Null}(L)$, note trivially $y\in C^n$. Then:
$$
a_0y+a_1y^{(1)}+a_2y^{(2)}...+a_n y^{(n)} &=0 \\
y^{(n)} &= -(b_0y+b_1y^{(1)}+b_2y^{(2)}...\underbrace{b_{n-1}{y}^{n-1}}_{\in C^{\min(k, 1)}})
$$
Where $b_{\nu}=a_{\nu}/a_{n}$. Now $b_{\nu}\in C^k$ by closedness under polynomial division. Also $y^{(\nu)} \in C^{n-\nu}$ hence the R.H.S is at least one time continously differentiable(the bottle neck being $a_{n-1}y^{(n-1)} \in C^{\min(k, 1)}$). Therefore $y^{(n)}\in C^1$. But this implies $y\in C^{n+1}$ hence we repeat the above argument to get $y^{(\nu)}\in C^{n+1-\nu}$. The R.H.S has the bottleneck $a_{n-1}y^{(n-1)}\in C^{\min(k, n+1-(n-1))}=C^{\min(k, 2)}$. We can repeat this procedure $m$ times and yield that $y^{(n)}\in C^{\min(k, m)}$. This means the best we can get is $y^{(n)}\in C^k$ or $y\in C^{n+k}$(after which the coeficient becomes the bottleneck).
:::
:::{prf:corollary} 
If the coefficients are in $C^{\infty}$ then $y\in \mathrm{Null}(L)$ are in $C^{\infty}$. 
:::
#### Nullspace of $L$ is an $n$-dimensional subspace of $C^{\infty}$

## Linear Independence: Wronskian 
:::{exercise} 1-dimensional Scattering Problem
Consider the 1d Shrodinger equation:
$$
-\frac{d^2\psi}{dx^2}+V-E\psi = E\psi 
$$

:::

## Solving $Ly=0$ with constant coefficients 

## $Ly=0$ with general $a_\nu(x)$

