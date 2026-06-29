# Fourier Series 

## $C_{2\pi}$  Space

$C_{2\pi}$  is a space of functions that is $2\pi$-periodic. This is precisely the space of functions we are going to expand by fourier series. 

:::{prf:definition} $C_{2\pi}$  Space
$C_{2\pi}$ is an infinite-dimensional vector space spanned by $\{e^{ikt}\}_{k\in\mathbb{Z}}$. It is also an inner product space endorsed with the inner product:
$$\langle f,g \rangle = \frac{1}{2\pi}\int_{0}^{2\pi} fg^*dt$$
:::

where $g^*$ denotes the *complex conjugate* of $g$.

An elementary observation is that  $\{e^{ikt}\}_{k\in\mathbb{Z}}$ is orthonormal:

$$\frac{1}{2\pi}\int_0^{2\pi}e^{ik_1t}e^{-ik_2t}=\delta_{k_1k_2}$$

:::{prf:proof}
:class: dropdown

Since $$\frac{1}{2\pi}\int_0^{2\pi}e^{ik_1t}e^{-ik_2t} &= \frac{1}{2\pi}\int_0^{2\pi}e^{i(k_1-k_2)t}$$
$$
\frac{1}{2\pi}\int_0^{2\pi}e^{i(k_1-k_2)t} = \frac{1}{2\pi}\int_0^{2\pi}\cos(k_1-k_2)t + i\sin(k_1-k_2)t
$$
If $k_1=k_2$ then it's clear we get $1$. Otherwise, since both cosine and sine component above have period $\frac{2\pi}{k_1-k_2}$ hence $2\pi$ is always a multiple:
$$
\frac{1}{2\pi}\int_0^{2\pi}e^{i(k_1-k_2)t}(k_1-k_2)\underbrace{\int_0^{2\pi}\cos(t)}_{0}+i(k_1-k_2)\underbrace{\int_0^{2\pi} \sin(t)}_{0}
$$
:::

This immediately gives fourier series expansion:
$$
f=\sum_{k\in\mathbb{Z}}\langle f, \exp(-ikt)\rangle \exp(ikt)
$$

### Algebra 
Recall that we can construct vector space(denoted $V$) from fields(denoted by $\mathbb{F}$) by stacking elements from the field together. Valid operators include addition of vector and scalar multiplications. *Algebra* takes one more step and introduce "vector-vector" multiplications:
:::{prf:definition} Algebra
An **algebra** is a vector space equipped with a binary operatation $V\times V\to V$ that is *commutative*, *associative* and *distributive*. 
:::


In this section, we show that the infinite dimensional vector space $C_{2\pi}$ spanned by $\{e^{ik\pi}\}_{k\in\mathbb{Z}}$ equipped with convolution 