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


## Solving $Ly=0$ with constant coefficients 

## $Ly=0$ with general $a_\nu(x)$


:::{exercise} 1-dimensional Scattering Problem
:label: 1dscat
Consider the 1d Schrodinger equation:
$$
-\frac{d^2\psi}{dx^2}+V\psi = E\psi 
$$
This is an eigenvalue problem of the operator $H=-\frac{d^2}{dx^2}+V$:
$$
H\psi = E\psi 
$$
Where $V$ has finite support $[-a, a], a\in \mathbb{R}$. Denote:
1. $L:=\{x\in \mathbb{R}:x<-a\}$
2. $R:=\{x\in \mathbb{R}:x>a\}$

**Problems**:
1. Show that in $L,R$, the general solution to the formal operator $H-E$ where $E=k^2$ is:
$$
\psi_k &=A\exp(ikx)+B\exp(-ikx) \quad x\in L  \\
\psi_k &=C\exp(ikx)+D\exp(-ikx) \quad x\in R
$$
2. Now consider two asymptotic boundary condition:
$$
\begin{cases}
\Pi_L: D=0, x\to \infty \\
\Pi_R: C=0, x\to -\infty
\end{cases}
$$
where $\Pi_L$ depicts a left-incident wave with no incoming wave from the right and $\Pi_R$ is the opposite. Show that the solution(in $L,R$) for the BC $\Pi_1$ is:
$$
\psi_k(x) = \begin{cases}
\exp(ikx)+ r_L\exp(-ikx) & x\in L \\
t_L\exp(ikx) & x\in R
\end{cases}
$$
Similarily, for $\Pi_2$:
$$
\psi_k(x)=\begin{cases}
t_R\exp(ikx)& x\in L \\
r_R\exp(ikx) + \exp(-ikx) & x\in R
\end{cases}
$$
where $t, r$ denotes the *transmission* and *reflection* coefficient.
3. Note that $\psi_k^*$ is also a solution. Use properties of Wronskian to shwo that:
   $$
    |t_{L/R}|^2 + |r_{R/L}|^2=1
   $$
:::

:::{solution} 1dscat
Fix a $k$, form the Wronskian:
$$
\begin{vmatrix}
\exp(ikx)+r_L\exp(-ikx) &   \exp(-ikx)+r_L\exp(ikx) \\
ik\exp(ikx)-ikr_L\exp(-ikx) & ik\exp(ikx)-ikr_L\exp(-ikx)
\end{vmatrix}
$$
:::
