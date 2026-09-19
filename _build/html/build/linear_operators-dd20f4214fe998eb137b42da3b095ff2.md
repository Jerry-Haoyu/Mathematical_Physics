# Linear Operators 

# $L^p$ Space 
:::{prf:definition} $L^p$ space
Let $(X,\Sigma, \mu)$ be a measure space and $1\leq p\leq \infty$. The space $L^p(X,\mu)$ is the set of all measurable functions from $X$ to $\mathbb{R}$ or $\mathbb{C}$ such that $\int_X |f(x)|^p d\mu < \infty$. 
- Note $L^p$ is a *normed space* with norm:
$$
\|f\|_{L_p}=\left(\int_X |f|^p d\mu\right)^{1/p}
$$
$p$ can be the symbol $\infty$ with the norm defined as:
$$
\|f\|_{L_{\infty}} = \inf\{C\in \mathbb{R}_{\geq 0} : |f(x)|<C, \forall x\}
$$
- It is *complete*, hence it is a Banach Space
:::

# Linear Operators 
:::{prf:definition} Linear Operators 
Let $T$ be a map betwen two normed space $X$ and $Y$. $T$ is linear if:
$$
T(x+\lambda y) = T(x) +\lambda T(y)
$$
$\forall x,y \in X, \lambda \in K$
:::

:::{prf:definition} Bounded Operators 
Let $T$ be a map betwen two normed space $X$ and $Y$. $T$ is bounded if $\exists C>0$:
$$
\|T(x)\|_Y\leq C\|x\|_X
$$
$\forall x \in X$
:::

:::{prf:proposition} Continuous and Bounded are equivalent for Linear Operator 
The following are equivalent:
1. If $X$ and $Y$ are normed spaces and $T:X\to Y$ is a linear map which is continuous from $X$ to $Y$
2. $T$ is bounded 
:::

:::{prf:proof}
- Suppose $T$ is linear and continous, $\forall x_0 \in X$, $\forall \epsilon > 0$, consider the open ball around $x_0$ with radius $\epsilon$ $B_{\epsilon}$. Then:
T(B_{\epsilon}^o)
$$
:::