# Linear Differential Operator 
### The Sturm-Liouville Operator 
The **Sturm-Liouville operator** is a linear differential operator of the form
$$
L=-\frac{d}{dx}\left(p\frac{d}{dx}y\right)+q\frac{d}{dx}
$$

We've shown that the Sturm-Liouville opeartor is self-adjoint with appropriate boundary condition in the sense that:
$$
\langle u, Lv \rangle &= \langle L^*u, v \rangle 
$$
hence it is analgous to self-adjoint operator in finite-dimensional vector spaces, which as symmetric matrix representation when the underlying field is real. We now make this connection explicit, i.e., actually constructing the discretized, finite-dimensional matrix representation of the Sturm-Liouville Operator.

### Bilinaer Form Optimization Gives Eigenvalue Problem
Instead of directly discretizing $L$, we aim to find a matrix $L$ such that discretizes the bilinear form:
$$
\int y^*Ly dx \rightarrow y^T
$$
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
Subjected to $\|x\|^2=1$. We note that this is an **eigenvalue problem**. Now our goal is to find a symmetric matrix $[L]$ such


[^diff]: In step 0, we computed the jacobian of $F:\mathbb{R}^n \to \mathbb{R}$ which is of shape $\mathbb{R}^{1\times n}$(a row vector). Recall that: $$
D_x\langle y_1(x), y_2(x) \rangle  = y_2^TD_xy_1 + y_1^T D_xy_2
$$