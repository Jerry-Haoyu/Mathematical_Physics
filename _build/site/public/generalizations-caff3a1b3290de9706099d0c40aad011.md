# Generalizations 

This section focuses on more general cases. In particular, 
1. **Multiple Constraint**, i.e., in the case of 
$$
J=\int f(x,y_1,y_2,...,y_n,\dot y_1, \dot y_2,...,\dot y_n, \ddot y_1,...)
$$
2. **Variable Endpoints**
In previous cases, we used the key assumption that:
:::{attention} Fixed Endpoint Assumption
The perturbation $\delta y$ is $0$ at endpoints, hence all boundary/surface terms arising from integartion by parts may be ignored.
:::
We now relax this assumption but rather work out boundary conditions based on the stationary condition with variable endpoints. This assumption can in turn be applied to the resulting differential equations. 

3. **Constrained Optimization** Often, the minimization of the action is subjected to physcial constraint. For instance, in the famous *catenary problem*, we need to fix the length of the hanging chain. 

## Multiple Constraint 

## Variable Endpoints

## Exercises
### Elastic Rods
:::{attention} Elastic Rods
- The **elastic energy per unit length** of a bent steel rod is given by $$\frac{1}{2}\frac{YI}{R^2}$$
Here Y is the *Young’s modulus* of the steel and $I$ is the moment of inertia of the rod’s cross section about an axis through its centroid and perpendicular to the plane in which the rod is bent. 

- Let us assume the rod is only slightly bent into the yz plane and lies close to the z axis. R is the radius of curvature due to the bending, related to the curvature by 
$$
\frac{1}{R}=\kappa = |T_z|
$$
where $T$ is the unit tangent vector to the rod. 

#### Problem 0

Show that the elastic energy can be approximated by:
$$
\boxed{
    \boxed{U[y]=\int_0^L \frac12 \left\{ \frac{1}{2} (y'')^2 -\right\}
}
$$

:::{tip} Solution
:::


$$
\boxed{U[y]=\int_0^L \frac12 \left\{ \frac{YL}{2} (y'')^2 - \frac{Mg}{2}(y')^2\right\}dz}
$$

#### 
:::