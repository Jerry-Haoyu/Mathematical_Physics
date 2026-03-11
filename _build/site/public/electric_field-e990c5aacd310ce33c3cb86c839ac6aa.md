---
kernelspec:
  name: python3
  display_name: 'Python 3'
---

# Electric Field 

:::{prf:definition}
An electric field $\mathbf{E}$ is a vector field $\mathbb{R}^{n}\to \mathbb{R}^{n}$, where $\mathbf{E}(\vec x_0)$ is the force experienced by a unit charge(positive test charge) at location $\vec x_0$. 
\begin{equation}
    \mathbf{E}(\vec x_0)=\frac{1}{4\pi \epsilon_0} \int \frac{\rho(\vec x)}{\|\vec x_0-\vec x\|^3}(\vec x_0-\vec x) d\vec x
\end{equation}
where $\rho$ gives the charge density at the location. 
:::

Which simply comes from the coulomb's law. The integral is written with a general sense which can be a summation in the discrete case and a  Riemann integral in other cases.The next two examples illustrate this idea.


:::{prf:example}
 Consider a cube placed at the origin with edge length $1$ a point charge of -1C at each vertex. What is the resulting electric field? 
    \begin{equation}
        \mathbf{E}(\vec x_0)=-\frac{1}{4\pi \epsilon_0 }\sum_{i,j,k\in \{-1,1\}}\frac{(x_0-i,y_0-j,z_0-k)^T}{\|\vec (x_0-i,y_0-j,z_0-k)\|^3}
    \end{equation}
    Which can be easily simulated:
    \begin{figure}[h]
        \centering
        \includegraphics[width=0.5\linewidth]{Electrodynamics/image/cube_point_field.png}
        \caption{Point cube field}
    \end{figure}
:::