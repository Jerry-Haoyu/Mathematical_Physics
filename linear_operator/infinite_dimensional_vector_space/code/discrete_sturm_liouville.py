import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt

"""
Author: Haoyu Tang
hytang2@illinois.edu
"""

class SturmLiouville:
    def __init__(self,N, p, q=None, grid='forward'):
        A = np.zeros(shape=(N,N))
        if grid == 'forward':
            for i in range(N-1):
                A[i, i] += p[i]
                A[i+1, i+1] += p[i]
                A[i, i+1] -= p[i]
                A[i+1, i] -= p[i]

        if q is not None:
            I = np.eye(N) 
            L = A + q @ I
        else:
            L = A
        
        # Dirchlet Boundary Condition
            L[0,0]=0.0
            L[0,1]=0.0
            L[1,0]=0.0
            L[N-1,N-1]=0.0
            L[N-1,N-2]=0.0
            L[N-2,N-1]=0.0
        self.L = (L * N ** 2)
        self.N = N

    def solve_eigen(self, top_k=10):
        eval, evec = np.linalg.eig(self.L)
        top_k_idx = np.argsort(eval[eval>0])[:top_k]
        return eval[top_k_idx] , evec[:, top_k_idx], top_k_idx
    
    def plot_evec(self, top_k=10, save_path=f"algebra/media/sl_evecs.png"):
        eval, evec, top_k_idx = self.solve_eigen(top_k)
        fig, ax = plt.subplots(2)
        ax[0].set_title(rf"Discretized Eigenfunctions $-\frac{{d^2}}{{dx^2}}y_j(x)=\lambda y_j(x)$ ")
        ax[1].set_title(rf"Analytical Eigenfunctions $-\frac{{d^2}}{{dx^2}}y_j(x)=\lambda y_j(x)$ ")
        plt.subplots_adjust(wspace=0.4, hspace=0.5)

        x = np.linspace(0,1,self.N)
        for j in range(top_k):
            lambda_ = int(np.sqrt(eval[j]/np.pi**2))
            y = evec[:, j] # computed
            y = y / np.sqrt(np.sum(y**2/N)) # normalize
            y_ = np.sin((j+1) * np.pi * x) # analytical
            y_ = y / np.sqrt(np.sum(y**2/N)) # normalize
            ax[0].plot(x, y if y[2]>0 else (-y), label=rf'$\lambda={lambda_}$')
            ax[1].plot(x, y_, label=rf'$\lambda={lambda_}$', linestyle='dashed')
            
        ax[0].legend(fontsize=7, loc='lower left')
        ax[1].legend(fontsize=7, loc='lower left')
        plt.savefig(save_path)
        
if __name__ == "__main__":
    N=5
    p=np.ones(N)
    sl = SturmLiouville(N, p)
    np.set_printoptions(precision=1, suppress=True)
    print(sl.L)
    # eval, evec, idx = sl.solve_eigen()
    # print("\n Expected 1, 2, 3, 4, 5,...  Got :")
    # print(np.sqrt(eval/np.pi**2).astype(int))
    # print("\n")
    # sl.plot_evec(top_k=5)