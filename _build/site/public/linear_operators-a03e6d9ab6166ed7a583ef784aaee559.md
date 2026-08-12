# Linear Operators 

## Triangularization

:::{prf:proposition} Existence of eigenvalue in vector spaces on algebraically closed field
Suppose $V$ is a finite-dimensional vector space over an algebraically closed field $\mathbb{F}$, and $T\in \mathcal L(V)$, then $T$ has at least one eigenvalue
:::

With this key proposition in hand, we can already algorithmically construct a triangular matrix representation for $T\in \mathcal L(V)$ where $V$ is over algebraically closed $\mathbb{F}$.The idea being we can **recursively** find an eigenvalue and factor it out:
:::{note} Algorithm
1. $m\gets 1, T_1\gets T$
2. $\lambda[]$
3. While $m < n$:
   1. Find an eigenvalue, eigenvector pair $\lambda_m$ of $T_m$ and its coresponding eigenvector $v$
   2. $\lambda[m]=\lambda_m$
   3. Factor out $\lambda$ : $T_{m+1}\gets T_m-\lambda I$.
   4. $m\gets m+1$
:::

:::{prf:theorem} Algebraically closed field guarantees triangularizability
Suppose $V$ is a finite-dimensional vector space over an algebraically closed field $\mathbb{F}$, and $T\in \mathcal L(V)$, then $T$ is always triangularizable. 
:::

:::{prf:proof} 
:class: dropdown
Induction on $n=\dim V$. $n=1$ is always upper triangular, hence always true. 
Suppose the theorem is true for $m < n$. Let $\dim V = n$ and $T\in \mathcal L(V)$. By the lemma $T$ has at least one eigenvalue :$Tv=\lambda v$. Define 
$$
U:=T-I\lambda 
$$
- **Claim**: $\mathrm{range}(U)$ is a subspace of dimension less than $n$. 
    - Indeed since by definition, $U$ is not injective hence not surjective, so $\dim(\mathrm{range}(U)) < n$.
As a result of the claim and the inductive hypothesis, $U$ is *triangularizable*. 

Let $\beta = \{v_1,...,v_m\}$ be such a basis so that $[U]_{\beta}$ is upper triangular. 
Now:
$$
Tv=(T-I\lambda)v + \lambda v =Uv+\lambda v
$$
Since $U$ is triangularizable, $\forall j \leq m$, $Uv_j\in \langle v_1,...,v_j \rangle$. Now $\lambda v_j $ clealry also lands in $\langle v_1,...,v_j \rangle$. As a result, 

$$
Tv_j \in \langle v_1,...,v_j \rangle
$$

As desired.
:::