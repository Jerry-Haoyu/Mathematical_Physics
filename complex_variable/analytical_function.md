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

If such $A$ exists then it must equal to to the **Jacobian** $Df(x_0)$ defined as:
$$
\left(\frac{\partial f_i}{\partial x_j}(x_0)\right)_{ij} \in \mathbb{R}^{m\times n}
$$

Furthermore, the sufficient condition for this linear transforamtion $A$ to exists is given by the following theorem:

:::{prf:theorem}
If $f:\mathbb{R}^n\to \mathbb{R}^m$, then $Df(a)$ eixsts iff all $D_jf^{i}(x_0)$ exist in an open set containing $x_0$ and if each function $D_jf^i$ is continous at $x_0$.
Rmk. we call such $f$ **continously differentiable**
:::


:::{prf:definition}
Let $f:\mathbb{C}\to \mathbb{C}$
:::

```{code-cell}
import matplotlib.pyplot as plt
import numpy as np
import ipywidgets as wdgt

slider = wdgt.FloatSlider(value=1.0, min=1.0, max=10.0, step=2.0)


def plot(r):
    fig, ax = plt.subplots()
    X, Y = np.meshgrid(np.linspace(-r, r, 10), np.linspace(-r, r, 10))
    ax.quiver(X, Y, X**2, Y**2)
    plt.show()

wdgt.interactive(plot, r=slider)
```