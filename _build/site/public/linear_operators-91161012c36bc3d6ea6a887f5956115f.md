# Linear Operators 

## Triangularization 

:::{prf:theorem} Algebraically closed field guarantees triangularizability
Suppose $V$ is a finite-dimensional vector space over an algebraically closed field $\mathbb{F}$, and $T\in \mathcal L(V)$, then $T$ is always triangularizable. 
:::

:::{prf:proof} 
Induction on $n=\dim V$. $n=1$ is always upper triangular, hence always true. 
Suppose the theorem is true for $k < n$. Let $\dim V = n$ and $T\in \mathcal L(V)$. By the lemma $T$ has at least one eigenvalue :$Tv=\lambda v$. Define 
$$
U:=T-I\lambda 
$$
- **Claim**: $\mathrm{range}(U)$ is a subspace of dimension less than $n$. 
    - Indeed since by definition, $U$ is not injective hence not surjective, so $\dim(\mathrm{range}(U)) < n$
:::