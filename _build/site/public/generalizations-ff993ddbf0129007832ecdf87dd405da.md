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
1) Elastic Rods. The elastic energy per unit length of a bent steel rod is given by 1
2
Y I/R2
.
Here Y is the Young’s modulus of the steel and I is the moment of inertia of the rod’s cross
section about an axis through its centroid and perpendicular to the plane in which the rod
is bent. Let us assume the rod is only slightly bent into the yz plane and lies close to the z
axis. R is the radius of curvature due to the bending, related to the curvature by
1/R = κ = |T˙
|
where T is the unit tangent vector to the curve and the overdot denotes differentiation with
respect to the arc length s. Show that the elastic energy can be approximated as
U[y] = Z L
0
1
2
Y I (y
00)
2
dz,
where the prime denotes differentiation with respect to z and L is the length of the rod. We
will use this approximate energy functional to discuss two practical problems.