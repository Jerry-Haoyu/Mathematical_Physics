# Least Square 

Suppose we have a dataset $\mathcal D = [(x_1,y_1),...,(x_n, y_n)]$, and by some prior knowledge we know there exists some relationship $y=kx + b$ in the dataset, the question is, how to find this particular relationship ? 

In otherword, we would like $(k,b)$ to be able to predict $y$ based on $x$ that best adhere to the relationship implied by the dataset $\mathcal D$. The $L_2$ error of this predictor with respect to $\mathcal D$ is:
$$
\sum_i (y_i-(kx_i+b))^2
$$
We know that we can reformulate this in matrix language:

