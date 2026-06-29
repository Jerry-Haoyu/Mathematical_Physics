# Ordinary Differential Equation 
## Linear Equations
Since all linear equations can be reduced to first order, the following model problem is of extreme importance
:::{prf:definition} ODE Model Problem
\begin{equation}
y'=Ay
\end{equation}
:::

As CS people, note this is just a **state-transition matrix** algorithmically. This perspecitve is going to be expolited in the next section which we basically "simulate" the system to get the solution numericaly. 
## Explict and Implicit Method 
*Explicity(Forward)* and *implicit(backward)* is going to be two buzzwords that appear in every page remotely relevant to numerical differential equations. 
Explicit method is the most trivial forward simulation: 
\begin{align*}
y_{t+1} &= y_{t} + Ahy_{t} \\
&= (I+Ah)y_t \\
\end{align*}

Implicit method on the otherhand, has a "circular dependency" where the linear approximation itself depend on the solution and hence require one to solve a linear system:
\begin{align*}
y_{t+1} &= y_{t} + Ay_{t+1} \\
(I-Ah)y_{t+1} &= y_{t} \\
y_{t+1} &= (I-Ah)^{-1}y_{t}
\end{align*}
:::{prf:definition} Explicit and Implict Method For Model Problem
The forward method(explicit method) scheme is:
\begin{equation}
y_{t+1} = (I+Ah)y_t 
\end{equation}
where the backward method(implicit method) cheme is:
\begin{equation}
y_{t+1} = (I-Ah)^{-1}y_t 
\end{equation}
:::
Solving a linear system isn't exactly cheap, hence one would wonder why bother using implict methods at all. To see this we need to do introduce *stability*.
