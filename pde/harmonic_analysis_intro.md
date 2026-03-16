---
kernelspec:
  name: python3
  display_name: 'Python 3'
---

# Basic Ideas in Harmonic Analysis 

This section is about the necessary calculus needed before we dive in. We first discuss vector field in a greater generality. 

## Tensor Field 

:::{prf:definition}
Let $\Omega \in \mathbb{F}^d$, a *tensor field* is a function $\Phi : \Omega \to X$ where $X=\bigotimes_{i=1}^n \mathbb{F}^{d_i}$
:::

For us CS people, this is somewhat easy to understand. It's just a map from a 1D array to multi-dimensional array. There are two kind of dimensions here,
one is the number of dimensions ($n$ in the above definition). The other is the the acutal dimension $d_i$s. 

### Gradient of Tensor Field 

:::{prf:definition}
The **gradient** is the unique map $\nabla : C^{\infty}(\mathbb{R}^d, \otimes_{i=1}^n \mathbb{R}^{d_i}) \to C^{\infty}(\mathbb{R}^d, \otimes_{i=1}^{i+1}  \mathbb{R}^{d_i})$ 
satisfying:
$$
u\cdot \nabla f(x)= \lim_{\epsilon\to 0}\frac{f(x+\epsilon u) - f(x)}{\epsilon}
$$
for every $x\in \mathbb{R}^d$ and unit vector $u\in \mathbb{R}^d$
:::

:::{prf:example}
Consider $f(x,y)=(x^2+y^2, xy)$. Gradient is just the transpose of the jacobian:

\begin{equation}
\nabla f = 
\begin{pmatrix}
    2x & 2y \\
    y & x   \\
\end{pmatrix}^T 
\end{equation}
Note $f: \mathbb{R}^2 \to \mathbb{R}^2$ but $\nabla f : \mathbb{R}^2 \to \mathbb{R}^2 \otimes \mathbb{R}^2$
:::


```{code-cell}
import torch
print(torch.__version__)
```




