import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import chart_studio.tools as tls

Z = np.linspace(1,118,118)
rho = np.linspace(0,300,300*100)
theta = np.linspace(0,2*np.pi,2*np.pi*10)
a0 = {1:1.0078} # Amstrong
psi100 = 1/np.sqrt(np.pi)*(Z[1]/a0[Z[1]])^3/2*np.exp(-rho)
fig = px.scatter_plot(psi100,r="rho")
fig.show()
a = np.linspace(0,2*np.pi,2*np.pi*10)