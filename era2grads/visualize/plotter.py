import matplotlib.pyplot as plt
import xarray as xr

class ERA5Plotter:
    @staticmethod
    def plot_contour(data: xr.DataArray, title: str = ""):
        """Genera un plot de contorno."""
        fig, ax = plt.subplots()
        data.plot.contourf(ax=ax, levels=20)
        ax.set_title(title)
        return fig
