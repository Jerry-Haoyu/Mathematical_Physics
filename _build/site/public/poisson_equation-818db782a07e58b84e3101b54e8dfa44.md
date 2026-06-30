---
kernelspec:
  name: python3
  display_name: 'Python 3'
---

# Poisson Equation 

## Finite-Element Method(FEM)
### The Tent Function 



```{code-cell}
import sys
from pathlib import Path
import ipywidgets as wdgt

# Calculates the absolute path to your 'src' directory
sys.path.append("src")

from src.twoDPoissonFEM import twoDPoisson

slider_resol = wdgt.FloatSlider(value=3.0, min=1.0, max=6.0, step=1.0)
slider_pos = wdgt.FloatSlider(value=0.0, min=0.0, max=36.0, step=1.0)

def plot(resolution, position):
    resolution, position = int(resolution), int(position)
    solver = twoDPoisson(0,10.0,0,10.0,resolution=resolution, f=lambda x : x)
    if position < resolution * resolution:
        tent_basis = solver.get_basis(position)
        fig, ax = solver.init_plot()
        ax.scatter(solver.grid_x, solver.grid_y, color='red')
        ax.plot_surface(solver.basis_x, solver.basis_y, tent_basis, cmap='coolwarm')

wdgt.interactive(plot, resolution=slider_resol, position=slider_pos)
```