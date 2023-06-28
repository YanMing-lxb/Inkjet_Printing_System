import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


class PathDisplay(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = QVBoxLayout(self)

        self.figure = plt.figure(figsize=(8, 6))
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        self.toolbar = NavigationToolbar(self.canvas, self)
        self.layout.addWidget(self.toolbar)

        self.dynamic_ax = self.figure.add_subplot(111, projection='3d')
        self.line = None

        self.UpdatePathDisplay(pd.DataFrame())

    def UpdatePathDisplay(self, data, mesh_density=10):
        if data.empty:
            return

        self.line = None

        self.dynamic_ax.clear()

        X = data['X']
        Y = data['Y']
        Z = data['Z']

        self.dynamic_ax.set_xlabel('X', color='black')
        self.dynamic_ax.set_ylabel('Y', color='black')
        self.dynamic_ax.set_zlabel('Z', color='black')

        x_min, x_max = X.min(), X.max()
        y_min, y_max = Y.min(), Y.max()
        z_min, z_max = np.nanmin(Z), np.nanmax(Z)

        self.dynamic_ax.set_xlim(x_min, x_max)
        self.dynamic_ax.set_ylim(y_min, y_max)
        self.dynamic_ax.set_zlim(z_min, z_max)

        # Create meshgrid based on data range and density
        x_range = np.linspace(x_min, x_max, mesh_density)
        y_range = np.linspace(y_min, y_max, mesh_density)
        X_mesh, Y_mesh = np.meshgrid(x_range, y_range)

        # Calculate Z values for the meshgrid based on data range
        z_mesh = np.interp(X_mesh.flatten(), X, Z)
        z_mesh = z_mesh.reshape(X_mesh.shape)

        self.dynamic_ax.scatter(X, Y, Z, c='blue', alpha=0.5)
        self.dynamic_ax.plot_surface(X_mesh, Y_mesh, z_mesh, cmap='viridis', edgecolor='none', alpha=0.3)

        if self.line is None:
            self.line, = self.dynamic_ax.plot([], [], [], color='black', linestyle='dashed')

        self.line.set_data(X, Y)
        self.line.set_3d_properties(Z)

        self.dynamic_ax.figure.canvas.draw()