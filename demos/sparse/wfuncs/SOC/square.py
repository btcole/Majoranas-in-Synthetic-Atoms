import time
import scipy.sparse.linalg as spLA

import majoranaJJ.operators.sparsOP as spop
import majoranaJJ.lattice.neighbors as nb
import majoranaJJ.lattice.shapes as shps
import majoranaJJ.etc.plots as plots

Nx = 100
Ny = 100
ax = 2      #unit cell size along x-direction in [A]
ay = 2      #unit cell size along y-direction in [A]

coor = shps.square(Nx, Ny)
NN = nb.NN_Arr(coor)
NNb = nb.Bound_Arr(coor)

alpha = 0.0   #Spin-Orbit Coupling constant: [eV*A]
gammaz = 0 #Zeeman field energy contribution: [T]
V0 = 0.0 #Amplitude of potential : [eV]
mu = 0 #Chemical Potential: [eV]

start = time.time()
H = spop.H0(coor, ax, ay, NN, mu = mu,  gammaz = gammaz)
print("H shape: ", H.shape)

num = 20 # This is the number of eigenvalues and eigenvectors you want
sigma = 0 # This is the eigenvalue we search around
which = 'LM'
energy, states = spLA.eigsh(H, k = num, sigma = sigma, which = which)

plots.state_cmap(coor, energy, states, n = 0, title = 'Ground State')
end = time.time()
print("Time taken to plot probability map for lattice of size {} = {} [s]".format(coor.shape[0], end-start))
