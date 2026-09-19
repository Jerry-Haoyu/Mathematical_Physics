# Linear Operators 

# $L^p$ Space 
:::{prf:definition} $L^p$ space
Let $(X,\Sigma, \mu)$ be a measure space and $1\leq p\leq \infty$. The space $L^p(X,\mu)$ is the set of all measurable functions from $X$ to $\mathbb{R}$ or $\mathbb{C}$ such that $\int_X |f(x)|^p d\mu < \infty$. 
- Note $L^p$ is a *normed space* with norm:
$$
\|f\|_{L_p}=\left(\int_X |f|^p d\mu\right)^{1/p}
$$
$p$
- It is *complete*, hence it is a Banach Space
:::