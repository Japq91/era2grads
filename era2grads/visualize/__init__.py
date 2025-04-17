# era2grads/visualize/__init__.py
from .plotter import ERA5Plotter
#from .vectors import VectorPlotter  # Futuro archivo
__all__ = ['ERA5Plotter']  # Controla qué se expone en "from visualize import *"
#__all__ = ['ERA5Plotter', 'VectorPlotter'] # Futuro 
