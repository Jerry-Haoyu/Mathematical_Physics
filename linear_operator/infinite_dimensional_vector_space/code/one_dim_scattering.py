import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def solve_scattering_cap(N=1200, L=20.0, E=0.8, cap_width=4.0, eta=2.0):
    x = np.linspace(-L, L, N)
    dx = x[1] - x[0]
    
    # 1. Physical potential (Gaussian barrier)
    V_phys = 1.0 * np.exp(-x**2)
    
    # 2. Construct Polynomial CAP W(x)
    W = np.zeros(N)
    x_l, x_r = -L + cap_width, L - cap_width
    
    W[x < x_l] = eta * ((x_l - x[x < x_l]) / cap_width)**2
    W[x > x_r] = eta * ((x[x > x_r] - x_r) / cap_width)**2
    
    # 3. Non-Hermitian Hamiltonian (hbar=1, m=1)
    D2 = (np.diag(-2 * np.ones(N)) + 
          np.diag(np.ones(N-1), 1) + 
          np.diag(np.ones(N-1), -1)) / (dx**2)
    
    H = -0.5 * D2 + np.diag(V_phys - 1j * W)
    
    # 4. Inject an incoming wave source e^{i k x} from left boundary
    k = np.sqrt(2 * E)
    source = np.zeros(N, dtype=complex)
    src_idx = np.argmin(np.abs(x - x_l))
    source[src_idx] = np.exp(1j * k * x[src_idx])
    
    # 5. Solve linear system (E*I - H) * psi = source
    A = E * np.eye(N, dtype=complex) - H
    psi = np.linalg.solve(A, source)
    
    return x, V_phys, W, psi

if __name__ == "__main__":
    x, V, W, psi = solve_scattering_cap(N=1200, L=20.0, E=0.8)
    
    re_psi = np.real(psi)
    im_psi = np.imag(psi)

    # Setup 3D Plot
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.set_box_aspect((0.1, np.max(re_psi)-np.min(re_psi), np.max(im_psi)-np.min(im_psi)))

    # 1. Plot the main 3D complex trajectory (x, Re(psi), Im(psi))
    ax.plot(x, re_psi, im_psi, label=r'$\psi(x)$ (3D Helix)', color='royalblue', lw=2)

    # 2. Projections on wall planes for visual clarity
    z_floor = np.min(im_psi) - 0.1
    y_back = np.max(re_psi) + 0.1

    # Re(psi) projected onto the floor
    ax.plot(x, re_psi, zs=z_floor, zdir='z', color='teal', alpha=0.35, label=r'Re($\psi$) floor projection')
    
    # Im(psi) projected onto the back wall
    ax.plot(x, np.full_like(x, y_back), im_psi, color='coral', alpha=0.35, label=r'Im($\psi$) wall projection')

    # Labels and view settings
    ax.set_xlabel('Position x')
    ax.set_ylabel(r'Re($\psi$)')
    ax.set_zlabel(r'Im($\psi$)')
    ax.set_title(r'3D Trajectory of Complex Wavefunction $\psi(x) = \text{Re}(\psi) + i\,\text{Im}(\psi)$')
    
    # Adjust viewing angle (elev=elevation angle, azim=azimuthal angle)
    ax.view_init(elev=25, azim=-150)
    ax.legend(loc='upper right')
    
    plt.tight_layout()
    plt.show()