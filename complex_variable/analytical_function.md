---
kernelspec:
  name: python3
  display_name: 'Python 3'
---

# Analytical Function 

## Real Derivative and Complex Derivative
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

Complex derivative, on the other hand, is defined as:

:::{prf:definition}
Let $f:\mathbb{C} \to \mathbb{C}$ be a complex function. The **derivative** of $f$ at $z_0$ is defined as
\begin{equation}
    \frac{df}{dz}({z_0})= \lim_{\Delta z\to 0}\frac{f(z_0 + \Delta z) -f(z_0)}{\Delta z}
\end{equation}
Or,
\begin{equation}
    \frac{df}{dz}({z_0})= \lim_{\Delta z\to 0}\frac{u(z+\Delta z) -u(z)}{\Delta z} + \lim_{\Delta z\to 0}\frac{v(z+\Delta z) -v(z)}{\Delta z} i
\end{equation}
where $u : \mathbb{C} \to \mathbb{R}$ is the real part of the complex function and $v$ being the complex part.
:::

This is *very different* from $f:\mathbb{R}^2 \to \mathbb{R}^2$! For the following two reasons:

:::{error} Difference 1: Division
:label: division
If we insist write the same definition for the real analog(i.e. denote a complex number $a+bi$ as $a \choose b$, $f_1\leftrightarrow u, f_2\leftrightarrow v$), then the above definition would look like:
\begin{equation}
\lim_{(x,y)^T \to (x_0,y_0)^T}
\begin{pmatrix}
\frac{\partial f_1}{\partial (x, y)} \\
\frac{\partial f_2}{\partial (x, y)}
\end{pmatrix}
\end{equation}
Which doesn't make sense at all(Although one could argue $\frac{\partial f_i}{\partial (x,y)}$ is just $(\nabla f_i)^T$ but that's merely symbolic. What would division by a vector mean?).
:::

:::{error} Difference 2 : Mixing Of Components
:label: mixing-of-components
To make it worse, even if we pretend such notation is sensible, they are still different. The limit of the real part $\lim_{\Delta z\to 0}\frac{u(z+\Delta z)-u(z)}{\Delta z}$(which we hoped to correspond to $\frac{\partial f_1}{\partial (x,y)}$) has a complex part and similarily the limit of the complex part also has a real part! This means the components are naturally mixing. 
:::

So the real difference is that complex number should be viewed as a whole where division is well-defined. For me, if I ever found it hard to convince myself $\mathbb{R}^2 \to \mathbb{R}^2$ is different from $\mathbb{C} \to \mathbb{C}$, I would try to answer the question "why can't we use $(a,b)$ to denote a+bi"?. This tend to clear things up.

The next example illustrate this key difference:
:::{prf:example} A not differentiable complex function with its real analog differentiable
Consider $f(x+iy)=x^2 + iy$. The real analog([Interactive Plot Of The Real Analog](#non-differentiable-complex-ex)) is:
\begin{equation}
f\begin{pmatrix}
x \\
y
\end{pmatrix}= 
\begin{pmatrix}
x^2 \\
y
\end{pmatrix}
\end{equation}
This function is clearly differentiable since the jacobian is:
$$\begin{pmatrix}
2x & 0 \\
0 & 1
\end{pmatrix}$$
which clearly continuous(component-wise) for all $x,y$. 


However, this is not true for the complex analog. We now show the complex function is not differentiable at $0\in \mathbb{C}$.

Suppose it is, then the two limits below should be equal at $0\in \mathbb{C}$:
```{math}
:label:complex_derivative_limit
\lim_{\Delta x\to 0}\frac{f(x_0 + \Delta x + y_0i) -f(x_0 + y_0 i)}{\Delta x} = \lim_{\Delta y\to 0}\frac{f(x_0 + (y_0 +\Delta y)) -f(x_0 + y_0 i)}{i\Delta y }
```
But computing the limit tells us that:
$$
2x_0 \neq 1
$$
Unless $x_0 = \frac{1}{2}$. Hence the function is only differentiable on the line $x_0=\frac12$.


One might ask, doesn't the seem problem exists for the real analog? It's quite obvious the answer is no, since we never compute a single limit of a finite difference. 

In a way, $\mathbb{C} \to \mathbb{C}$ is like $\mathbb{R}\to \mathbb{R}$, we define the derivative to be the limit of finite difference. Yet the limits

$$
\lim_{\Delta z\to 0}\frac{u(z+\Delta z) -u(z)}{\Delta z}, \lim_{\Delta z\to 0}\frac{v(z+\Delta z) -v(z)}{\Delta z} 
$$
resembles the $\mathbb{R}^2 \to \mathbb{R}$ where we expect the result to be independent of direction. That's why the real analog is fundamentally different from the complex function itself.
:::

```{code-cell} python
:tags: ["hide-input"]
#| label: non-differentiable-complex-ex
import matplotlib.pyplot as plt
import numpy as np
import ipywidgets as wdgt

slider = wdgt.FloatSlider(value=1, min=1, max=3, step=0.5)

def plot(r):
    fig, ax = plt.subplots()
    X, Y = np.meshgrid(np.linspace(-r, r, 10), np.linspace(-r, r, 10))
    ax.quiver(X, Y, X**2, Y)
    plt.show()

wdgt.interactive(plot, r=slider)
```

## Cauchy-Riemann Condition
Expanding [](complex_derivative_limit), we would get:
```{math}
\lim_{\Delta x\to 0} \frac{f(x_0+\Delta x + y_0i) - f(x_0+y_0i)}{\Delta x} &= \lim_{\Delta y\to 0} \frac{f(x_0 + (y_0+\Delta yi)) - f(x_0+y_0i)}{\Delta y} \\

\lim_{\Delta x\to 0}\frac{u(x_0+\Delta x, y_0)-u(x_0,y_0)}{\Delta x} + i \frac{v(x_0+\Delta x, y_0)-v(x_0,y_0)}{\Delta x} &=  
\lim_{\Delta y\to 0}\frac{u(x_0, y_0+\Delta y)-u(x_0,y_0)}{i\Delta y} + i \frac{v(x_0, y_0+\Delta y)-v(x_0,y_0)}{i\Delta y}\\

\frac{\partial u}{\partial x}+i\frac{\partial v}{\partial x} &= -\frac{\partial u}{\partial y}i + \frac{\partial v}{\partial y}
```
Note that this equation essentially unwind the "mixing of components" we mentioned in [](mixing-of-components). Hence we get:

```{math}
:label: cr
\boxed{\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y} \qquad 
\frac{\partial v}{\partial x} =  - \frac{\partial u}{\partial y}}
```

This is known as the Cauchy-Riemann Condition(C-R condition).

Let's recall what had happened so far, we discussed the idea of complex derivative being a limit of finite difference leading to computing limits of the form $\mathbb{R}^2\to \mathbb{R}$(two input, one output) which puts additional restriction on differentiability. To be more specific, in order for these limit to exists, the value of the limit must be invariant of directions approaching the point of interest $x_0, y_0$. Considering the specific direction along the real and complex axis we get the so-called CR condition. 

We have effectively shown that CR condition is *necessary* for complex differentiability. It turns out however, that CR condition is also *sufficient*. 

:::{prf:theorem} Cauchy-Riemann
A complex function $f:\mathbb{C} \to \mathbb{C}$ is differentiable at $z_0=x_0+iy_0$ iff it satisfies the *Cauchy-Riemann condition*:
1. $u,v\in C^1$(continously differentiable)
   
2. The partial derivatives satisfy
$$
\frac{\partial u}{\partial x} &= \frac{\partial v}{\partial y} \\
\frac{\partial u}{\partial y} &= -\frac{\partial v}{\partial x}
$$
In which case, the derivative is:
$$
\frac{\partial f}{\partial z} &= \frac{\partial u}{\partial x} + i \frac{\partial v}{\partial x} \\
&= \frac{\partial v}{\partial y} - i \frac{\partial u}{\partial y}
$$
:::
:::{prf:proof} CR condition is sufficient
We need to show, $\forall \epsilon >0$,  $\exists \delta >0$ such that $|\Delta z|<\delta$ implies :
$$
\left| \frac{f(z_0+\Delta z)-f(z_0)}{\Delta z} - \left(\frac{\partial u}{\partial x} + i\frac{\partial v}{\partial x}\right) \right| < \epsilon
$$
We consider the linaer approximation of $f(z_0+\Delta z)-f(z_0)$ around $z_0$:
$$
f(z_0+\Delta z)-f(z_0)&=\textcolor{blue}{u(x_0+\Delta x,y_0+\Delta y)-u(x_0,y_0)} + i[\textcolor{red}{v(x_0+\Delta x, y_0+\Delta y)-v(x_0,y_0)}]
\\ &+ O(\Delta x^2) + iO(\Delta y^2) \\
&= \textcolor{blue}{\frac{\partial u}{\partial x}\Delta x +\frac{\partial u}{\partial y} \Delta y} +i\left(\textcolor{red}{\frac{\partial v}{\partial x}\Delta x +\frac{\partial v}{\partial y}\Delta y} \right) \\ &+ O(\Delta x^2)+iO(\Delta y^2) \\
&= \left(\textcolor{blue}{\frac{\partial u}{\partial x}}+i\textcolor{red}{\frac{\partial v}{\partial x}}\right)\Delta x+\left(\textcolor{blue}{\frac{\partial u}{\partial y}} + i\textcolor{red}{\frac{\partial v}{\partial y}}\right)\Delta y\\ &+ O(\Delta x^2)+iO(\Delta y^2) \\
$$
We need to expose $i\Delta y$, hence we rewrite the third term in the last equation above:
$$
\left(\textcolor{blue}{\frac{\partial u}{\partial y}} + i\textcolor{red}{\frac{\partial v}{\partial y}}\right)\Delta y \longrightarrow \left(\textcolor{blue}{-\frac{\partial u}{\partial y}}i + \textcolor{red}{\frac{\partial v}{\partial y}}\right)i\Delta y
$$
Therefore:
$$
f(z_0+\Delta z)-f(z_0) &=  \left(\textcolor{blue}{\frac{\partial u}{\partial x}}+i\textcolor{red}{\frac{\partial v}{\partial x}}\right)\Delta x+\left(\textcolor{blue}{-\frac{\partial u}{\partial y}}i + \textcolor{red}{\frac{\partial v}{\partial y}}\right)i\Delta y\\ &+ O(\Delta x^2)+iO(\Delta y^2) 
$$
Now applying CR condition:
$$
f(z_0+\Delta z)-f(z_0) &=  \left(\textcolor{blue}{\frac{\partial u}{\partial x}}+i\textcolor{red}{\frac{\partial v}{\partial x}}\right)\Delta x+\left(\textcolor{red}{\frac{\partial v}{\partial x}}i + \textcolor{blue}{\frac{\partial u}{\partial x}}\right)i\Delta y\\ &+ O(\Delta x^2)+iO(\Delta y^2)  \\
&= \textcolor{blue}{\frac{\partial u}{\partial x}}\left(\Delta x + i\Delta y\right) + i\textcolor{red}{\frac{\partial v}{\partial x}}(\Delta x+i\Delta y)
\\ &+ O(\Delta x^2)+iO(\Delta y^2) \\
&= \left(\textcolor{blue}{\frac{\partial u}{\partial x}} + i\textcolor{red}{\frac{\partial v}{\partial x}}\right)\underbrace{(\Delta x +i\Delta y)}_{\Delta z}\\
&+ \underbrace{O(\Delta x^2)+iO(\Delta y^2)}_{O(|\Delta z|\Delta z)} \\
$$
Therefore the quotient is:
$$
 \frac{f(z_0+\Delta z)-f(z_0)}{\Delta z} =\textcolor{blue}{\frac{\partial u}{\partial x}} + i\textcolor{red}{\frac{\partial v}{\partial x} }+O(|\Delta z|)
$$
and thus the quanity we want to control is:
$$
\left| \frac{f(z_0+\Delta z)-f(z_0)}{\Delta z} - \left(\frac{\partial u}{\partial x} + i\frac{\partial v}{\partial x}\right) \right|=O(|\Delta z|)
$$
By definition of big-O, $O(|\Delta z|)<C|\Delta z|$ for $|\Delta z|\in \mathbb{R}$. Hence $\forall \epsilon >0$, we can pick $\delta =\frac{\epsilon}{C}$ such that $O(|\Delta z|)<C\delta =\epsilon$
:::

## Analytical Function
Now we are ready for the definition of **analytic function**. 
:::{prf:definition} Analytic Function on Entire Function
- A complex function $f:\mathbb{C} \to \mathbb{C}$ is **analytic at $z_0$** if it is differentiable at $z$ and a neighborhood of $z$. 
- A function that is differentiable thourhgout some open set $\Omega \in \mathbb{C}$ is **analytic in $\Omega$**
- A function that is analytical throughout $\mathbb{C}$ is called **entire**.
:::
Analytic is a much more restrictive property than merely differentiable(since it requires differentiability in the neighborhood). For instance, we can easily construct complex functions that is differentiable on *infinitely many points* in $\mathbb{C}$ but analytic *nowhere*. 
:::{prf:example} Differentiable on infinite many points but analytic nowhere
Suppose we want the function to be differentiable on $y=x$ and $y=-x$. Then we can, by CR, let:
$$
\frac{\partial u}{\partial x} =2x, \frac{\partial v}{\partial y} = 2y
$$
and 
$$
\frac{\partial v}{\partial x} =-2x, \frac{\partial u}{\partial y} = 2y
$$
A easy choice would just be:
$$
f&=x^2+y^2 +i(y^2-x^2) \\
&= zz^*+i\left(\frac{z^2+{z^*}^2}{2}\right)
$$
:::
:::{attention} Quick Exercise
:label: ananowhere
Do you see why the above function is analytical nowhere?
:::
:::{tip} Solution to [](ananowhere)
:class: dropdown
Every open set in $\mathbb{C}$ contains *some* point not on $y=x$ or $y=-x$
:::