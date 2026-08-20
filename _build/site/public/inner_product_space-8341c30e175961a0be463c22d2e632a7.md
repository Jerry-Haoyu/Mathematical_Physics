# Inner Product Space

# Distribution and Test Functions
## Continous Indexing

## Duality Pairing

## Exercises
:::{exercise} $\delta$ is a ring homomorphism
:label: delta_as_ring_homomorphism

Consider $\mathcal T$ and $\mathbb{R}$ as two rings. 

**1. Prove that $\delta$ preserves ring multiplication**
$$
f\delta(x)=f(0)\delta(x)
$$
```{figure} media/T'_as_module.png
```

**2. Distribution Derivative of $f\delta$**
Show that the distribution derivative of $f\delta$ is $$
(f\delta,\partial \psi) = -(f(0)\delta'(x), \psi)
$$
:::




:::{solution} delta_as_ring_homomorphism
<!-- :class: dropdown -->
1. $\forall g\in \mathcal T$, we have:
$$(f\delta)[g] &= \delta[fg] \\
&=f(0)g(0) \\
&= f(0)
$$
As desired. 
1. First show using the ring homomorphism result:
$$
(f\delta, \psi) &= (f(0)\delta, \psi) \\
                &= -(\partial f(0)\delta,\psi) \\
                &= -(f(0)\delta'(x),\psi)
$$
We can also show
:::

# Formal adjoint 

# Concrete Adjoint 

## The Sturm-Liouville Operator 
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

**Numpy Implementation**
This can easily be translated to naive `numpy` code:
:::{code} python

class SturmLiouville:
    def __init__(self,N, p, q=None, grid='forward'):
        A = np.zeros(shape=(N,N))
        if grid == 'forward':
            for i in range(N-1):
                A[i, i] += p[i]
                A[i+1, i+1] += p[i]
                A[i, i+1] -= p[i]
                A[i+1, i] -= p[i]

        if q is not None:
            I = np.eye(N) 
            L = A + q @ I
        else:
            L = A
        
        # Dirchlet Boundary Condition
            L[0,0]=0.0
            L[0,1]=0.0
            L[1,0]=0.0
            L[N-1,N-1]=0.0
            L[N-1,N-2]=0.0
            L[N-2,N-1]=0.0
        self.L = (L * N ** 2)
        self.N = N

    def solve_eigen(self, top_k=10):
        eval, evec = np.linalg.eig(self.L)
        top_k_idx = np.argsort(eval[eval>0])[:top_k]
        return eval[top_k_idx] , evec[:, top_k_idx], top_k_idx
:::

**Example: $-\frac{d^2}{dx^2}$ as a Matrix**
We can do a quick example to showcase that $L$ is indeed a discretization of $\mathcal L$. 
:::{prf:example} -$\frac{d^2}{dx^2}$
We have already seen that the opeartor:
$$
T=-\frac{d^2}{dx^2}, D(T)=\{y,Ty \in L^2[0,1]:y(0)=y(1)=0\}
$$
has eigenvalues and eigenvectors:
$$
y_j(x) &=\sqrt{2}\sin j\pi x \\
\lambda_j &= j^2\pi^2 
$$
for $j=1,2,3...$. The problem is that, can we solve a matrix eigenvalue problem to recover exactly the same result?
Indeed we can! Passing $p=-1$ and $q=0$ gets us:
$$
L=N\begin{pmatrix}
0 & 0 & &  &  \\
0 & 2 & -1 & &  \\
 & -1 & \ddots & \ddots & \\
& & \ddots & 2 & -1  &\\
& & & -1& 2 & 0\\
& & & & 0 & 0 \\
\end{pmatrix}
$$

and solving the matrix eigenvalue problem $$L\hat y &= \lambda \hat y$$ gets us:
[^normalization]
:::{figure} media/sl_evecs.png

:::

:::{exercise} 
1. We discretized $L$ based on the quadratic form $\int_0^1 y\mathcal L y dx$, hence $\hat y^T L\hat y$ should coincide with $\int_0^1 y\mathcal L y dx$. Come up with at least 2 functions and 2 operators that satisfy the requirment($L^2(0,1),y(0)=y(1)=0$). Compute the quadratic form analytically and numericaly. Cheeck that the results are the same.
2. Remove the masking code snippet(which implements Dirchlet boundary condition) in the naive SL class `SturmLiouville`. What is the resulting eigenvectors? Explain the result.
3. Try coming up with different discretization with center difference or back difference. Implemet it in `python`
 or `julia`.
   - Is the resulting matrix $L$ still symmetric ? 
   - Center differencing scheme results in a numerical artifcat, what is the numerical artifact? Try explaining why such artifact occur(*Hint: Note that even and oddd indicies are decoupled*)
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

[^normalization]: Since iterative eigensolvers gives eigenvectors of arbitrary magnitude $v_j=a\sin(j\pi(x))$, we need to normalize properly by 
    1.Ensure $a>0$ 
    1. Divide by $\sqrt{\sum y_i^2 h} $