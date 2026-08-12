# Groups 

In theoretic frameworks of physical sciences, there are all kinds of spaces. We use $\mathbb{R}^3$ to model the world in classical mechanics and electromegnatism. There are also more abstract spaces like space of parameters of a neural network. Group theory studies the structure of these spaces. This chapter act as a quick introduction and primarily serves two reasons:

(1) Provides setup for vector space and tools used in linear algebra proofs 
(2) As a prerequisite of Representation Theory. 

## Groups and Subgroups 
A group $G$ is an algebra structure that is closed. To this aspect, a group is like a biological species. 
When two individual mate and produce an offspring, we would expect
(1) It is still of the same species 
(2) It is different from its parents 
Likewise, in groups, mating is defiend by a binary operation(binary means takes two inputs) $\cdot : G\times G\to G$. It takes parents $g_1,g_2\in G$ as input and returns the offspring $g_3$. 


However, there exists an individual that is special known as the *identity*. When mated with any element in the species, the offspring 

:::{prf:definition} Groups
A group is a tuple $(G,\cdot)$ of a set $G$ equipped with a binary operation $\cdot$ such that they satisfy the **group axiom**:
1. There exists an identity $e$: $\forall g\in G$ $$ eg=ge=g$$
2. Every element has an inverse: $\forall g\in G, \exists g^{-1} $ such that $$gg^{-1}=g^{-1}ge$$
3. $+$ satisfies associativity:$\forall g_1,g_2,g_3\in G$ $$ (g_1g_2)g_3=g_1(g_2g_3)$$
:::

If all elements of the group are commutative with respect to each other, then the group is called **abelian**.
### Examples
1. Additive group of integers modulo $n$
:::{prf:definition} $\mathbb{Z}_n$
This is the group with elements $\{[0]_n,...,[n-1]_n\}$ being the congruence class modulo $n$. The binary operation is addition between congruence classes which can be proven to be well-definied. 
:::
- The identity is $[0]_n$
- Inverse of $[k]_n$ is $[n-k]_n$
- Associativity inheirted from associativity of integer addition 
## Cosets and Normal Subgroup 

### Lagrange's Theorem

## Quotient Group 

### First Isomophism Theorem 