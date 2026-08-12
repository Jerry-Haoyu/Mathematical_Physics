# Measure 

It will be inevitable to step on some measure \& integration theory in dealing with *Partial Differential Equations* and *Stochastic Processes*. This chapter acts as a brief introduction. 

## Sigma Algebra 

In physics, the task of finiding "volume" is ubquitous. For instance in computing mass, charge, the integral would resemble:
$$
\int (\cdot ) dV 
$$
In some sense, this $dV$ is a function $dV:E\to \mathbb{R}$ which computes the volume of $E\subset \mathbb{R}^n$, a tiny control volume we are interested in.  It would be very natural to ask for this function to satisfy:

:::{prf:definition} Measure
Suppose $X$ is a set. Let $\mu: A \to \mathbb{R}$ where $A\subset P(X)$ such that:
- $$\mu(\varnothing)=0 $$
- **(countable additivity)** $E_1,E_2,....$ is a countable inifnite sequence of disjoint, then:
$$
\mu(\cup_j E_j)=\sum_j \mu(E_j)
$$
Then we call $\mu$ a measure. 
:::

The question would be, when can we find such a function. Untrivially, this is not possible when $A\subset P(X)$, in otherword, it is not possible 



