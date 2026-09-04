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
Suppose $X$ is a set. Let $\mu: A \to \mathbb{R}$ where $A\in P(X)$ such that:
- $$\mu(\varnothing)=0 $$
- **(countable additivity)** $E_1,E_2,....$ is a countable inifnite sequence of disjoint, then:
$$
\mu(\cup_j E_j)=\sum_j \mu(E_j)
$$
Then we call $\mu$ a measure. 
:::

The question would be, when can we find such a function. Trivially we can obtain such property by sending every $A$ to $0$. However, for more practical purposes of modeling the world, we would like nicer properties. In particular, let's consider this compeletly reasonable demand on $\mathbb{R}^n$.

:::{prf:example} Measure on $\mathbb{R}^n$ and Vitali's Set
:::


:::{exercise} Open Set as a Topology [^hw_mineyev]
:label: Open Set as a Topology
1. Let $\mathcal{B}$ be the family of all open intervals in $\mathbb{R}$, i.e. subsets of the form$$(a, b) := \{c \in \mathbb{R} \mid a < c < b\}$$for all $a, b \in \mathbb{R}$ with $a < b$. Let $\mathcal{T}(\mathcal{B})$ be the family of all arbitrary unions of elements in $\mathcal{B}$, i.e.,$$\mathcal{T}(\mathcal{B}) := \left\{ \bigcup_{B \in \mathcal{B}'} B \mathrel{\Big\vert{}} \mathcal{B}' \subseteq \mathcal{B} \right\}$$Prove that $\mathcal{T}(\mathcal{B})$ is a topology on $\mathbb{R}$. (This "$\mathcal{B}$" stands for a "base" = "basis" of a topology.)
   
2. For $\mathcal{B}$ and $\mathcal{T}(\mathcal{B})$ as above and any $U \in \mathcal{T}(\mathcal{B})$ (i.e., any open set), prove that there exists a countable family $\mathcal{B}'' \subseteq \mathcal{B}$ (of open intervals) such that $U = \bigcup_{B \in \mathcal{B}''} B$. (Hint: it might help to prove first that the union of any family of open intervals containing a given $x \in \mathbb{R}$ is a generalized open interval in the sense that it is of the form $(a, b)$, $(-\infty, a)$ or $(a, \infty)$ for some $a, b \in \mathbb{R}$. Or do this any other way.)

3. For $\mathcal{T}(\mathcal{B})$ as above, prove that $\mathcal{T}(\mathcal{B}) \subseteq \mathcal{B}_{\mathbb{R}}$, the Borel $\sigma$-algebra on $\mathbb{R}$. (This "$\mathcal{B}$", confusingly, stands for "Borel".)
4.  Use the above to give a full proof of Proposition 1.2 on p. 22 in [F].
5.   Also deduce that $\mathcal{M}(\mathcal{B}) = \mathcal{M}(\mathcal{T}(\mathcal{B})) = \mathcal{B}_{\mathbb{R}}$.
:::


:::{solution} Open Set as a Topology
1. We prove that $\mathcal{T}(\mathcal{B})$ is a topology on $\mathbb{R}$.

- **Property 1: $\emptyset, \mathbb{R} \in \mathcal{T}(\mathcal{B})$**
  - $\emptyset = \cup_{B \in \emptyset} B$ (empty union), so $\emptyset \in \mathcal{T}(\mathcal{B})$
  - $\mathbb{R} = (-\infty, \infty)$ is a generalized open interval, hence $\mathbb{R} \in \mathcal{T}(\mathcal{B})$. More explicitly, we can cover it by $\cup \{(a,a+1),(-a-1,-a)\}_{a=0}^{\infty}$

- **Property 2: Closed under arbitrary unions**
  - If $\{U_\alpha\}_{\alpha \in I} \subseteq \mathcal{T}(\mathcal{B})$, then each $U_\alpha = \cup_{B \in \mathcal{B}_\alpha} B$ for some $\mathcal{B}_\alpha \subseteq \mathcal{B}$
  - Then $\cup_{\alpha \in I} U_\alpha = \cup_{\alpha \in I} \left(\cup_{B \in \mathcal{B}_\alpha} B\right) = \cup_{B \in \cup_\alpha \mathcal{B}_\alpha} B \in \mathcal{T}(\mathcal{B})$

- **Property 3: Closed under finite intersections**
  - By induction on the number $n$ of sets.
  - **Base case** ($n=1$): Trivial, $U \in \mathcal{T}(\mathcal{B})$.
  - **Inductive step**: Assume $U_1 \cap \cdots \cap U_n \in \mathcal{T}(\mathcal{B})$ for any $n$ sets in $\mathcal{T}(\mathcal{B})$. 
    For $n+1$ sets, write $(U_1 \cap \cdots \cap U_n) \cap U_{n+1}$. By induction hypothesis, $U_1 \cap \cdots \cap U_n = \cup_{i \in I}(a_i, b_i)$ 
    for some countable collection of open intervals. Then 
    $$(U_1 \cap \cdots \cap U_n) \cap U_{n+1} = \left(\cup_{i \in I}(a_i, b_i)\right) \cap U_{n+1} = \cup_{i \in I}((a_i, b_i) \cap U_{n+1})$$
    Each $(a_i, b_i) \cap U_{n+1}$ is an intersection of an open interval with a union of open intervals, which is 
    a finite union of open intervals (or empty). Hence $(U_1 \cap \cdots \cap U_{n+1}) \in \mathcal{T}(\mathcal{B})$.

Therefore $\mathcal{T}(\mathcal{B})$ is a topology on $\mathbb{R}$.

---

2. Suppose $\mathcal B' \subseteq \mathcal B$ and 
$$
U=\bigcup_{B\in \mathcal B'} B
$$
where $\mathcal B'$ can be uncountable. We would like to show $\exists \mathcal B''$ that is countable such that 
$$
U=\bigcup_{B\in \mathcal B^{''}} B
$$
We now show a specfic way to construct $\mathcal B''$ from $\mathcal B'$. Define:
$$
\mathcal B_x = \{(a,b)\in \mathcal B' : x\in (a,b)\}
$$
Clearly $\mathcal B_x \subseteq \mathcal B'$. Now proceed with the following procedure(an "infinite algorithm")on the construction of $\mathcal B''$
```{prf:algorithm}
**Input**: A potentially uncountable set of open intervals $\mathcal B'$ such that $\cup \mathcal B'=U$

**Output**: A countable set of open intervals $\mathcal B''$ such that $\cup \mathcal B''=U$
1. $\mathcal B'' = \varnothing$
2. **While** $\exists x\in U$,  $x\notin \cup \mathcal B''$ : 
    1. Compute $(c,d)=\bigcup_{B\in \mathcal B_x} B$ where $c,d$ is in extended real number system.
    2. **If** $c,d\in \mathbb{R}$:
        1.  $\mathcal{B}_x'=\{(c,d)\}$
    3. **Else if** $c\in \mathbb{R}, d=\infty$:
        1. $\mathcal{B}_x'\gets \{(c,[c])\}\cup \{[c],[c]+j\}_{j=1}^{\infty}$
    4. **Else** 
        Other cases follows as (3)
    5. $\mathcal B'' = \mathcal B'' \cup \mathcal B_x '$

3. **Return** $\mathcal B''$
```
where $[c]$ picks the closes integer towards the right of the real axis. 
Note we implicitly invoked the claim below in computing $(c,d)$:
- $\boxed{\textbf{Cliam 1}}$ The union of arbitrary family of open intervals containing $x\in \mathbb{R}$ is a *generalized open interval* 
  $$\bigcup_{B\in \mathcal B_x} B\in \{(c,d): c,d\in \mathbb{R}\cup \{\infty, -\infty\}\}$$
  - I claim the union is just $(c,d)$ where $c=\inf \{a:(a,b)\in \mathcal B_x\}$ and $d=\sup \{b:(a,b)\in \mathcal B_x\}$ where we allow $\infty$ and $-\infty$. Clearly $(c,d)$ covers $\cup \mathcal B_x$. It suffice to show $\cup \mathcal B_x $ covers $(c,d)$. Suppose $\exists y \in (c,d)$ and $y\notin \cup \mathcal B_x$. This means $\cup \mathcal B_x$ has a hole and there must exists a pair of open interval in $\mathcal B_x$ that is disjoint, contradicting that all open intervals in $\mathcal B_x$ contains $x$(in that case no pair should be disjoint).

Now what's left to show is (1) Only countable number of $\mathcal B_x'$ is needed. (2) each $\mathcal B_x'$ is countable. The later is obvious by construction. The former can be argued by countability of $\mathbb{Q}$. Pick a $q\in \mathbb{Q}$ in one of the open interval of $\mathcal B_x'$, this is always possible by density of rationals. Suppose uncountable $\mathcal B_x'$ is needed to cover $\cup \mathcal B''$ then $U=\cup \mathcal B''$ would contain uncountable number of rationals. This finishes the proof.

---

3. By definition, $\mathcal B_{\mathbb{R}}$ is the smallest $\sigma$-algebra containing $\mathcal T(\mathcal B)$. Therefore the inclusion holds by construction.
   
--- 
4. We only need to show (b), (c), and (e) since (a) and (d) are generalized open 
   intervals and are actually shown by (5).

**Case (b): Closed intervals** $\mathcal{E}_2 = \{[a,b]: a < b\}$
- $\mathcal{M}(\mathcal{E}_2) \subseteq \mathcal{B}_\mathbb{R}$: Note that $[a,b] = \cap_{j=1}^{\infty}(a-1/j, b+1/j)$ 
  is a countable intersection of open intervals, so $\mathcal{E}_2 \subset \mathcal{B}_\mathbb{R}$.
- $\mathcal{B}_\mathbb{R} \subseteq \mathcal{M}(\mathcal{E}_2)$: $(a,b) = \cup_{j=1}^{\infty}[a+1/j, b-1/j]$ 
  is a countable union of closed intervals, so $\mathcal{B} \subset \mathcal{M}(\mathcal{E}_2)$ and hence 
  $\mathcal{B}_\mathbb{R} = \mathcal{M}(\mathcal{B}) \subset \mathcal{M}(\mathcal{E}_2)$.

**Case (c): Half-open intervals** $\mathcal{E}_3 = \{(a,b]: a < b\}$
- $\mathcal{M}(\mathcal{E}_3) \subseteq \mathcal{B}_\mathbb{R}$: $(a,b] = (a,b) \cup \{b\}$ where $(a,b) \in \mathcal{B}_\mathbb{R}$ 
  and $\{b\} = \cap_{j=1}^{\infty}(b-1/j, b+1/j) \in \mathcal{B}_\mathbb{R}$.
- $\mathcal{B}_\mathbb{R} \subseteq \mathcal{M}(\mathcal{E}_3)$: $(a,b) = \cup_{j=1}^{\infty}(a, b-1/j]$ 
  is a countable union of half-open intervals, so $\mathcal{B} \subset \mathcal{M}(\mathcal{E}_3)$ and hence 
  $\mathcal{B}_\mathbb{R} \subset \mathcal{M}(\mathcal{E}_3)$.

**Case (e): Closed rays** $\mathcal{E}_7 = \{[a,\infty): a \in \mathbb{R}\}$
- $\mathcal{M}(\mathcal{E}_7) \subseteq \mathcal{B}_\mathbb{R}$: $[a,\infty) = \cap_{j=1}^{\infty}(a-1/j, \infty)$ 
  is a countable intersection of open rays (generalized open intervals), so $\mathcal{E}_7 \subset \mathcal{B}_\mathbb{R}$.
- $\mathcal{B}_\mathbb{R} \subseteq \mathcal{M}(\mathcal{E}_7)$: $(a,b) = (a,\infty) \cap (-\infty,b)$ where 
  $(a,\infty) = \cup_{j=1}^{\infty}[a+1/j,\infty)$ and $(-\infty,b) = \mathbb{R} \setminus [b,\infty)$ are in $\mathcal{M}(\mathcal{E}_7)$, 
  so $\mathcal{B} \subset \mathcal{M}(\mathcal{E}_7)$ and hence $\mathcal{B}_\mathbb{R} \subset \mathcal{M}(\mathcal{E}_7)$.

Cases (c'), (e') follow by symmetry.

 
--- 
5. We only need to show 
$$
\mathcal B &\subseteq \mathcal M(\mathcal T(\mathcal B)) \\
\mathcal T(\mathcal B) &\subseteq \mathcal M( \mathcal B)
$$
- The former is trivial since $\mathcal B \subseteq \mathcal T(\mathcal B)\subseteq \mathcal M(\mathcal T(\mathcal B)$
- The later can be shown using (2). $\mathcal M(\mathcal B)$ contains all countable unions of open intervals $\mathcal B$ while $\mathcal T(\mathcal B)$ contains arbitrary union. (2) bridges the gap by claiming the arbitrary union can actually be replaced by countable union. 
:::

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

# Casestudy: Lebesgue-Stieltjes Measure
The most useful set that we would like to equip a measure with is, unarguably, the real numbers $\mathbb{R}$. 
## Starting Point: The half-intervals 
Recall that we would start with an elementary collection that has a clear notion of size. We define the **h-intervals**:
$$
H=\{(a,b]:a<b, a,b\in \mathbb{R}\}
$$

We define a terminology here:
:::{prf:definition} Borel Sets
Let $X$ any metric space, the $\sigma$-algebra genereated by the family of open sets in $X$ is called the **Borel $\sigma$-algebra**, denoted by $\mathcal B_{X}$
:::

:::{exercise} h-intervals generate $\mathcal B_{\mathbb{R}}$
Check $H$ is an elementary set and so it generates an algebra $\mathcal A$. Furthermore, show that the $\sigma$-algebra generated by $\mathcal A$ is   $\mathcal B_{\mathbb{R}}$
:::

Another terminology:
:::{prf:definition} Elementary Decomposition
Suppose $A\in \mathcal A$, since $\mathcal A=\mathcal M(H)$ we can find finite disjoint h-intervals $\{I_j\}_{j=1}^N=\{(a_j,b_j]_j\}_{j=1}^N$ such that:
$$
A=\bigcup_{j=1}^N I_j
$$
Then $\{I_j\}$ is an **elementary decomposition** of $A$.
:::


We define size on $H$ as follows:
:::{note} Notion of Size on h-intervals
Let $F:\mathbb{R}\to\mathbb{R}$ be increasing and right-continous, let $(a,b]\in H$, then:
$$
|(a,b]|=F(b)-F(a)
$$
Note when $F(x)=x$, we get the common notion of length of interval. 
:::

The next step is to extend this notion of size to $\mathcal A=\mathcal M(H)$. 
## Step 1: Construction of a premeasure 
Now we have an algebra $\mathcal A$ where elements of the algebra $A\in \mathcal A$ has an elementary decomposition $A=\{I_j\}$ to h-intervals $I=(a_j,b_j]$, which is equipped with a notion of size $b_j-a_j$. A natural way to define the notion of size for $A$ is hence:
$$
\mu_0(A) = \sum_{j=1}^N |I_j| =\sum_{j=1}^N F(b_j)-F(a_j)
$$
We claim that $\mu_0$ is actually a *pre-measure* on $\mathcal A$.
:::{prf:proposition}
Let $F:\mathbb{R}\to\mathbb{R}$ to be a right-continuous, increasing function. Define $\mu_0$ as 
$$
\mu_0 : \mathcal A &\to \mathbb{R} \\
\bigcup_{j=1}^N A &\mapsto \sum_{j=1}^N [F(b_j)-F(a_j)]
$$
where $\{I_j\}=\{(a_j,b_j]\}$ is an elementary decomposition. Then $\mu_0$ is a premeasure on $\mathcal A$.
:::

:::{prf:proof} $\mu_0$ is a pre-measure
We first need to show that $\mu_0$ is actually well-defined[^well-defined]. Then we illustrate:
1. Empty set has zero measure 
2. Non-negativity 
3. Finite additivity 
4. Countable additivity
where only $(1),(2),(4)$ is truely required. But $(3)$ is used in the proof of $(4)$.
:::


[^well-defined]: Note that in definiting a notion of size $\mu_0$ on $A\in \mathcal A$, we requires $A$ to have a concrete representation $\cup_j I_j$. If the result is independent on 
how we choose this representation(i.e. different elementary decomposition$\{I_j\}$), then this notion of size is indeed fundamentally correct. Otherwise if $\mu_0$ is dependent on how we choose representation, then it is not a credibe notion of size. Such "representational invariance" is called *well-definedness* in mathematics. 
[^hw_mineyev]: This problem is selected from *Professor Igor Mineyev*'s homework from MATH 540(Real Analysis) in Fall 2026 at UIUC.