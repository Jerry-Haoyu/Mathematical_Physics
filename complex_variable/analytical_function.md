---
kernelspec:
  name: python3
  display_name: 'Python 3'
---

# Analytical Function 
A complex function $f:\mathbb{C}\to \mathbb{C}$ resembles, more or less, functions like $\mathbb{R}^2\to \mathbb{R}^2$. For instance, the complex exponential $f(z)=\exp(z)$ would be more or less similar to 
$$
    f\begin{pmatrix}
        x \\
        y
    \end{pmatrix} = 
    \begin{pmatrix}
        \exp(x)\cos(y) \\
        \exp(x)\sin(y)
    \end{pmatrix}
$$

Since the complex version can be rewritten as $\exp(z)=\exp(x+iy)=\exp(x)(\cos(y) + i\sin(y))$. 

However, there does exist crucial differencies. Recall for real functions $(\mathbb{R}^2, \mathbb{R}^2)$, they are differentiable if there exists a linear transformation $A\in \mathcal L (\mathbb{R}^2, \mathbb{R}^2)$ such that:
$$
    \lim_{x\to x_0} \frac{\|f(x_0+h)-f(x_0) - Ah\|}{\|h\|}=0
$$



:::{prf:definition}
Let $f:\mathbb{C}\to \mathbb{C}$
:::