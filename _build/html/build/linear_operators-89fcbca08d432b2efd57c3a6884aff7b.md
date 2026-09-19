# Linear Operators


# Change of basis
Let $V$ be a finite-dimensional vector space of dimesnion $n$. Let $\beta=\{e_1,...,e_n\}$ and $\beta'=\{e_1',...,e'_n\}$ be both basis for $V$. We are interested in change reprentation of $x\in V$ from using $\beta$ to $\beta'$. To do this we need to know how $e_j\in \beta$ can be represented using $\beta'$:
$$
e_\nu = a_{\nu}^{\mu} e_{\mu}' 
$$
Here coefficientcs $a_{\nu}^{\mu}$ can be orgainized into a matrix. The matrix $a_{\nu}^{\mu}$ looks like:

$$
\begin{pmatrix}
a_1^1 & a_2^1 & \cdots & a_n^1\\
\vdots &\vdots  & &\vdots\\
a_n^1 & a_n^1 & \cdots & a_n^1\\
\end{pmatrix}
$$

## Contravariant Transformation
There are two interpretations of $a_{\nu}^{\mu}$:

1. **($a_{\nu}^{\mu}$ transform $\beta'$ to $\beta$)** This is the definition above:
$$
e_\nu = a_{\nu}^{\mu} e_{\mu}' 
$$
2. **($a_{\nu}^{\mu}$ transform representation in $\beta$ to $\beta'$)** 
Now for arbitrary $x\in V$, we have:
$$
x=c'_{\nu}e'_{\nu}=c_{\nu}e_{\nu} =c_\nu (a_{\nu}^{\mu} e_{\mu}' )=(c_\nu a_{\nu}^{\mu}) e_{\mu}' 
$$
from which we recognize:
$$
c_{\nu}'=(c_{\nu}a_{\nu}^{\mu})
$$

We note that the matrix has *opposite* effect on basis and representation. This is actually intuitive: in order to represent the vector in new basis $\beta'$, we will have to write the old basis $e_\nu \in \beta$ using linear combinations of the new basis $e_{\mu}'$. The later which effectively transforms basis in $\beta'$ to $\beta$. For this reason, the representation is said to be transformed **contravariantly**.



:::{note} Notation
The matrix $a_{\nu}^{\mu}$ is commonly denoted by $[I]_{\beta}^{\beta'}$ in math textbooks. Therefore:
- Transform in represenation is denoted by:
$$
[x]_{\beta'}=[I]_{\beta}^{\beta'}[x]_{\beta}
$$
- Transform in matrix representation of operator is given by:
$$
[T]_{\beta}=[I]_{\beta'}^{\beta}[T]_{\beta'}[I]_{\beta}^{\beta'}
$$
:::


# Triangularization

:::{prf:proposition} Existence of eigenvalue in vector spaces on algebraically closed field
Suppose $V$ is a finite-dimensional vector space over an algebraically closed field $\mathbb{F}$, and $T\in \mathcal L(V)$, then $T$ has at least one eigenvalue
:::


:::{prf:theorem} Algebraically closed field guarantees triangularizability
Suppose $V$ is a finite-dimensional vector space over an algebraically closed field $\mathbb{F}$, and $T\in \mathcal L(V)$, then $T$ is always triangularizable. 
:::
