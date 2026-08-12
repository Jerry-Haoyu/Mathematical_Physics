# Linear Differential Operator 
### The Sturm-Liouville Operator 
The **Sturm-Liouville operator** is a linear differential operator of the form
$$
\mathcal L=-\frac{d}{dx}\left(p\frac{d}{dx}y\right)+q\frac{d}{dx}
$$

We've shown that the Sturm-Liouville opeartor is self-adjoint with appropriate boundary condition in the sense that:
$$
\langle u, \mathcal Lv \rangle &= \langle \mathcal L^*u, v \rangle 
$$
hence it is analgous to self-adjoint operator in finite-dimensional vector spaces, which as symmetric matrix representation when the underlying field is real. We now make this connection explicit, i.e., actually constructing the discretized, finite-dimensional matrix representation of the Sturm-Liouville Operator.

### A Discrete Analog
Let's consider a concrete SL opeartor defined on $[0,1]$ with Dirchlet boundary condition $y(0)=y(1)=0$. Instead of directly discretizing $\mathcal L$, we aim to find a matrix $L$ such that discretizes the quadratic form:
$$
F(y)=\int y\mathcal Ly dx \rightarrow \hat y^TL\hat y
$$
First we note that:
:::{math}
:label: func
F(y) &= \int_0^1 y\left(-\frac{d}{dx}\left(p\frac{d}{dx}y\right) + qy\right) dx \\
&= \int_0^1 -y \frac{d}{dx}\left(p\frac{d}{dx}y\right)dx+\int_0^1 qy^2dx  \\
&= -\left\{\cancel{\left[yp\frac{dy}{dx}\right]_0^1} - \int p\left(\frac{dy}{dx}\right)^2 \right\} + \int_0^1 qy^2dx \\
&= \int_0^1 py'^2 + qy^2 
:::
Now we discretize $y, p, q$ to $N$-dimensional arrays:
$$
\hat y &= [y_1,...,y_N] \\
\hat p &= [p_1,...,p_N] \\
\hat q &= [q_1,...,q_N]
$$
Using forward difference we get:
$$
\hat y =\left(\frac{y_{i+1}-y_i}{h}\right)^2
$$
Rewrite the integral as a finite sum we obtain a discretized version of [](func):
$$
\boxed{\hat F(\hat y)=\sum_{i=1}^N h p_i\left(\frac{y_{i+1}-y_i}{h}\right)^2 +q_iy_i^2}
$$
Our goal is now to find a matrix $ L$ such that $\hat y^TL\hat y=\hat F(\hat y)$. Rewrite $\hat F(\hat y)$:
$$
\hat F(\hat y) =\sum_{i=1}^N Np_i(y_{i+1}^2 -2y_{i+1}y_i +y_i^2)+\frac{1}{N}q_iy_i^2
$$
We can split $L=L_1+L_2$ such that 
1. $\hat y^T L_1 \hat y = \sum_{i=1}^N Np_i(y_{i+1}^2 -2y_{i+1}y_i +y_i^2)$ 
2. $\hat y^T L_2 \hat y = \sum_{i=1}^N \frac{1}{N}q_iy_i^2$. 
   
**(Constructing $L_1$)**
Let's first deal with $L_1$. Consider the $2\times 2$block with the upperleft corner at $(i,i)$ that should 
represent $Np_i(y_{i+1}^2 -2y_{i+1}y_i +y_i^2)$. This is easy:
$$
A_i=Np_i\begin{pmatrix}
1 & -1\\
-1 & 1 \\
\end{pmatrix}
$$
To assemble $L_1$ we can overlap $A_i$ along the diagonal of $L$ with a stride of $1$. Concretely:
```
for i=1,...,N-1
    L[i,i] += Np_i
    L[i+1,i+1] += Np_i
    L[i,i+1] -= Np_i 
    L[i+1,i] -= Np_i
```
:::{prf:example}
A quick example for $N=4$:
$$4\begin{pmatrix}
p_1 & -p_1 & 0 & 0 \\
-p_1 & p_1+p_2 & -p_2 &0 \\
0 & -p_2 & p_2+p_3 & -p_3 \\
0 &  0 & -p_3  & p_3
\end{pmatrix}$$
:::

**(Constructing $L_2$)** 
$L_2$ is purely diagonal and is easier to derive. Since it only has quadratic term $y_i^2$, at each row $i$ we only need to include $y_i$. Hence:
$$
L_2 = \frac{1}{N}\begin{pmatrix}q_1 & & \\
& \ddots & \\
& & q_N
\end{pmatrix}
$$

**(Assembly $L_1+L_2$)**
It is clear that $L$ should look like:

$$
L=N\begin{pmatrix}
p_1&  -p_1 & & &  \\
-p_1& p_1+p_2 &  -p_2 & &  \\
&  \ddots  &  \ddots &   \ddots &   \\
&  &-p_{N-1} &p_{N-1}+p_{N} & -p_N  \\
& & &-p_N & p_N \\
\end{pmatrix} 
+ 
\frac{1}{N}\begin{pmatrix}q_1 & & \\
& \ddots & \\
& & q_N
\end{pmatrix}
$$
However, since we are dealing with concrete operators with accompanying domain and boundary condition, we need to encoorperate the Dirchelt boundary condition $y(0)=1, y(1)=0$ into $L$. To do so we need to zero-out the first row and column of $L$. Hence finally we get:
:::{prf:proposition}
The Sturm-Liouville Operator on $[0,1]$ with Dirchlet boundary condition $y(0)=y(1)$ can be discretized as 
:::{math}
:label: discreteSL
L=N\begin{pmatrix}
0 &0 & & &  &\\
0 &p_1+p_2 & -p_2& & & \\
&-p_2&  \ddots &\ddots & -p_{N-1}& \\
& & \ddots &-p_{N-1} & p_{N-1}+p_N &0 \\
& & & &0 & 0\\
\end{pmatrix} 
+ 
\frac{1}{N}\begin{pmatrix}0 & & & & \\
& q_2 & & & \\
&  & \ddots& & \\
& & & q_{N-1} & \\
& &  & & 0  \\
\end{pmatrix}

:::
We can see that $L$ is indeed a symmetric real matrix(Hermitian)!
We can do a quick example to showcase that $L$ is indeed a discretization of $\mathcal L$. 
:::
:::

<!-- 
:::{note} Optimizing $x^TAx$ gives $Ax=\lambda x$
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
Subjected to $\|x\|^2=1$. We note that this is an **eigenvalue problem**. 
 -->



[^diff]: In step 0, we computed the jacobian of $F:\mathbb{R}^n \to \mathbb{R}$ which is of shape $\mathbb{R}^{1\times n}$(a row vector). Recall that: $$
D_x\langle y_1(x), y_2(x) \rangle  = y_2^TD_xy_1 + y_1^T D_xy_2
$$