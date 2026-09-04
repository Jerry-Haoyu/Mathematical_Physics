# Measure 

It will be inevitable to step on some measure \& integration theory in dealing with *Partial Differential Equations* and *Stochastic Processes*. This chapter acts as a brief introduction. 

## $\sigma$-Algebra 
### Motivation
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

The question would be, when can we find such a function. Untrivially, this is not possible when $A\subset P(X)$, in otherword, it is not possible to define a sense of volume on arbitrary set. What if $X=\mathbb{R}$, does the nice properties of $\mathbb{R}$ help? Sadly, also no. 

We comprimise a little, and constraint ourselve to a particular family of subset of $P(X)$. It turns out that this sepcific family, called "$\sigma$-algebra" allows us to define measure upon.


# Construction of Measure

## The big picture
The general idea of constructing measure is, in crude terms:
1. Find a collection of set that has a clear notion of size 
2. Make the collection closed in finite set operations by generating an algebra on the collection. 
3. Approximate arbitrary subsets using element in the algebra, hence get a notion of size on arbtirary subsets 
4. Make the notion of size truely a measure by restricting to a special collection of subset.
   
More concretely the collection of set with clear notion of size need to have a certain structure called *elementary collection of set*(denoted by $\mathcal E$).  *Elementary collection* has a special property: it can be promoted to an algebra $\mathcal A$ by disjoint union. Now the notion of size on $\mathcal E$ can be exteneded to the algebra $\mathcal A$, creating a so-called *pre-measure* which possess *countable additivity* on $\mathcal A$. Then the process of approximating arbitrary set using elementary class
is called the construction of an *outer-measure*. During the process, we looses *countable additivity* as it is reduced to *countable subadditivity*. Finally we obtain a true *measure* by restricting the *outer-measure* on a special collection of subset called the *Caratheory $\sigma$-algebra*.

Observe how the notion of size ripens:
$$
\text{Stage 1: $\boxed{|\cdot|:\mathcal E \to \mathbb{R}^+}$} 
&\longrightarrow \text{Stage 2: $\boxed{\mu_0: \mathcal A \to  \mathbb{R}^+}$} \\ 
&\longrightarrow \text{Stage 3: $\boxed{\mu^* : P(X)\to \mathbb{R}^+}$} \\ 
&\longrightarrow \text{Stage 4: $\boxed{\mu: S \to \mathbb{R}^{+}}$}
$$
1. *Stage 1 to 2*: Expand the domain to ensures closedness and obtains *countable-additivity*; Lacks the ability to take arbtirary subset as input 
2. *Stage 2 to 3*: Expand the domain to arbitray subset but as a cost *countable additivity* deterioates to *countable subadditivity*. 
3. *Stage 3 to 4*: Shrink the domain; This is now a **complete measure**



## Elementary collection and pre-measure
:::{prf:definition} Elementary Collection of set
An **elementary collection** of set is a collection of set $\mathcal E \in P(X)$ such that:
1. **(Contains null)** $\varnothing \in \mathcal E $
2. **(Closed under intersection)** If $E,F\in \mathcal E$ then $E\cap F\in \mathcal E$
3. **(Closed by disjoint union under complement)** If $F\in \mathcal E$ then exists disjoint subsets $E_j\in \mathcal E$ such that $F^c = \cup_j E$
:::
## Outer Measure
So how do we actually construct measures no matter what set we are working on?(Though in this book we are really interested in just $\mathbb{R}^n$). A general guidline is:
1. Find some *elementary set* $\mathcal{E}$ where premeasure is defined on the disjoint uniont of $\mathcal{E}$.
2. Define the measure of arbitrary subset $A\in P(X)$ as the the size of "smallest" cover of $A $ using the elementary set:
:::{math}
:label: omfml
\inf \left\{\sum_{\nu=1}^{\infty} \rho(E_{\nu}): E_{\nu}\in \mathcal{E}, A\subset \bigcup_{\nu=1}^{\infty} E_{\nu}\right\}
:::
More generally we can define an *outer measure* as follows:
:::{prf:definition} Outer Measure
:label: omdf
An outer measure on an non-empty set $X$ is a function $\mu^* : P(X)\to [0,\infty]$ such that:
- $\mu^*(\varnothing)=0$
- If $A\subset B$, then $\mu^*(A)<\mu^*(B)$
- $\mu^*(\cup_{\nu}A_{\nu})\leq \sum_{\nu} \mu^* (A_{\nu })$
:::
We note that property (2),(3) are both derived properties of measure. So we can think the definition of outer measure as a relaxation of measure: take out countable additvity and adds back two derived property. In addition,  We note that [](omfml) obeys [](omdf)
:::{attention} Exercise
Show that [](omfml) indeed defines an outer measure [](omdf).
:::
How do we then obtain measure from outer measure? We note that what outer measure lacks is finite additivity, so we can further ask, is there a collection of subset $\mathcal {M}\subset P(X)$ such that $\mu^*$ is actually finitey additive? The answer is actually YES! However this seems rather arbitrary:
$$
\mathcal M = \{A\subset X: \mu^*(F)=\mu^*(F-A)+\mu^*(A\cap F), \forall F \subset X\}
$$
We call elements of $\mathcal M$ **$\mu^*$-measureable**. In plain English, this saying $A$ can "split measure" arbitrary $F\subset X$ by measuring the intersection and the complement separetly and add them together. 
:::{prf:theorem} Carathéodory's Theorem
If $\mu^*$ is an outer measure of $X$ then 
1. the collection of **$\mu^*$-measureable** sets:
$$
\mathcal M = \{A\subset X: \mu^*(F)=\mu^*(A^c \cap F)+\mu^*(A\cap F), \forall F \subset X\}
$$
is a $\sigma$-algebra. 
1. $\mu^*|_{\mathcal M}$ is a **complete measure**
:::



We first show a small lemma:
:::{prf:lemma} $\mathcal M$ is closed under finite union and $\mu^{*}$ is finitely additive on $\mathcal M$
Let $\mu^{*}$ be an outer measure:
1. Suppose $A,B\in \mathcal M$ then $$A\cup B\in \mathcal M$$
2. Suppose $A,B\in \mathcal M$, $A\cap B=\varnothing$ $$\mu^{*}(A \cup B) = \mu^*(A)+\mu^*(B)$$
:::

:::{prf:proof} proof of lemma
:class: dropdown
1.(**$\mathcal M$ is closed under finite union**) It suffice to show that $A \cup B$ split measure every subset in $X$. That is, $\forall F\subset X$
$$
\mu^*(F)=\mu^*(F\cap(A\cup B)) + \mu^*(F\cap(A\cup B)^c)
$$
Since $\mu^*$ has subadditivity by definition, we only need to show:
$$
\mu^*(F)\geq \underbrace{\textcolor{red}{\mu^*(F\cap(A\cup B))} + \textcolor{blue}{\mu^*(F\cap(A\cup B)^c)}}_{I}
$$
where we denoted the quantity to be bounded as $I$. Now note that we can expand the two term again by subadditivity to get:
$$
\textcolor{red}{\mu^*(F\cap A \cap B) + \mu^*(F\cap A \cap B^c)+\mu^*(F\cap A^c \cap B)} + \textcolor{blue}{\mu^*(F\cap A^c \cap B^c)}\geq I
$$
Now we note that $B\in \mathcal M$ hence $B$ can split measure any set, including $F\cap A\subset X$ and $F\cap A^c \subset X$. Hence: 
$$
\mu^*(F\cap A) +\mu^*(F \cap A^c)\geq I
$$
But $A \in \mathcal M$ therefore:
$$
\mu^*(F)\geq I
$$

2.(**$\mu^{*}$ is finitely additive on $\mathcal M$**)
First use that $A\in \mathcal M$
$$
\mu^*(A\cup B) &= \mu^*((A\cup B)\cap A) +  \mu^*((A\cup B)\cap A^c) \\
&= \mu^*(A\cup (A\cap B))  +  \mu^*(A^c \cap B)
$$
Now use disjointness to conclude: $A\cap B=\varnothing, A^c \cap B = B$ hence:
$$
\mu^*(A\cup (A\cap B))  +  \mu^*(A^c \cap B) &= \mu^*(A)+\mu^*(B)
$$
:::

:::{prf:proof} proof of Carathéodory
We only need to upgrade "finite" to "countable" in the previous argument.
 
:::

# The Pragmatic Casestudy
## Lebesgue-Stieltjes Measure
The most useful set that we would like to equip a measure with is, unarguably, the real numbers $\mathbb{R}$. 
### The half-intervals 
Recall that we would start with an elementary collection that has a clear notion of size. We define the **h-intervals**:
$$
H=\{(a,b]:a<b, a,b\in \mathbb{R}\}
$$

We define a terminology here:
:::{prf:definition} Borel Sets
Let $X$ any metric space, the $\sigma$-algebra genereated by the family of open sets in $X$ is called the **Borel $\sigma$-algebra**, denoted by $\mathcal B_{X}$
:::

:::{exercise} h-intervals generate $\mathcal B_{\mathbb{R}}$
Check $H$ is an elementary set and so it generates an algebra. Furthermore, show that the $\sigma$-algebra generated by $\match$ $\mathcal B_{\mathbb{R}}$
:::
### Construction of a premeasure 