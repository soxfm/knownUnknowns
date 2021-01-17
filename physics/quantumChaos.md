# Quantum Chaos
---
Quantum chaos is a branch of physics which studies how chaotic classical dynamical systems can be described in terms of quantum theory. The primary question that quantum chaos seeks to answer is: "What is the relationship between quantum mechanics and classical chaos?" The correspondence principle states that classical mechanics is the classical limit of quantum mechanics, specifically in the limit as the ratio of Planck's constant to the action of the system tends to zero. If this is true, then there must be quantum mechanisms underlying classical chaos (although this may not be a fruitful way of examining classical chaos). If quantum mechanics does not demonstrate an exponential sensitivity to initial conditions, how can exponential sensitivity to initial conditions arise in classical chaos, which must be the correspondence principle limit of quantum mechanics?

In seeking to address the basic question of quantum chaos, several approaches have been employed:
  1. Development of methjods for solving quantum problems where the pertubartion cannot be considered small in pertubartion theory and where qunatum numbers are large.
  2. Correlating statistical descriptions of eigenvalues(energy levels) with the classical behaviour of the same Hamiltonina ( system )
  3. Semiclassical methods such as periodic-orbit theory connecting the classical trajectories of the dynamical system with quantum features.
  4. Direct application of the correspondence principle.

### Quantum meachnics in no-perturbative regimes

For conservative systems, the goal of quantum mechanics in non-perturbative regimes is to find the eigenvalues and eigenvectors of a Hamiltonian of the form

    H = H s + ε H n s , {\displaystyle H=H_{s}+\varepsilon H_{ns},\,} H=H_{s}+\varepsilon H_{{ns}},\,

where H s {\displaystyle H_{s}} H_{s} is separable in some coordinate system, H n s {\displaystyle H_{ns}} H_{ns} is non-separable in the coordinate system in which H s {\displaystyle H_{s}} H_{s} is separated, and ϵ {\displaystyle \epsilon } \epsilon is a parameter which cannot be considered small. Physicists have historically approached problems of this nature by trying to find the coordinate system in which the non-separable Hamiltonian is smallest and then treating the non-separable Hamiltonian as a perturbation.

Finding constants of motion so that this separation can be performed can be a difficult (sometimes impossible) analytical task. Solving the classical problem can give valuable insight into solving the quantum problem. If there are regular classical solutions of the same Hamiltonian, then there are (at least) approximate constants of motion, and by solving the classical problem, we gain clues how to find them.

Other approaches have been developed in recent years. One is to express the Hamiltonian in different coordinate systems in different regions of space, minimizing the non-separable part of the Hamiltonian in each region. Wavefunctions are obtained in these regions, and eigenvalues are obtained by matching boundary conditions.

Another approach is numerical matrix diagonalization. If the Hamiltonian matrix is computed in any complete basis, eigenvalues and eigenvectors are obtained by diagonalizing the matrix. However, all complete basis sets are infinite, and we need to truncate the basis and still obtain accurate results. These techniques boil down to choosing a truncated basis from which accurate wavefunctions can be constructed. The computational time required to diagonalize a matrix scales as N 3 {\displaystyle N^{3}} N^3, where N {\displaystyle N} N is the dimension of the matrix, so it is important to choose the smallest basis possible from which the relevant wavefunctions can be constructed. It is also convenient to choose a basis in which the matrix is sparse and/or the matrix elements are given by simple algebraic expressions because computing matrix elements can also be a computational burden.

A given Hamiltonian shares the same constants of motion for both classical and quantum dynamics. Quantum systems can also have additional quantum numbers corresponding to discrete symmetries (such as parity conservation from reflection symmetry). However, if we merely find quantum solutions of a Hamiltonian which is not approachable by perturbation theory, we may learn a great deal about quantum solutions, but we have learned little about quantum chaos. Nevertheless, learning how to solve such quantum problems is an important part of answering the question of quantum chaos. 

### Recent directions

One open question remains understanding quantum chaos in systems that have finite-dimensional local Hilbert spaces for which standard semiclassical limits do not apply. Recent works allowed for studying analytically such quantum many-body systems.[10][11]

The traditional topics in quantum chaos concerns spectral statistics (universal and non-universal features), and the study of eigenfunctions (Quantum ergodicity, scars) of various chaotic Hamiltonian H ( x , p ; R ) {\displaystyle H(x,p;R)} H(x,p;R).

Further studies concern the parametric ( R {\displaystyle R} R) dependence of the Hamiltonian, as reflected in e.g. the statistics of avoided crossings, and the associated mixing as reflected in the (parametric) local density of states (LDOS). There is vast literature on wavepacket dynamics, including the study of fluctuations, recurrences, quantum irreversibility issues etc. Special place is reserved to the study of the dynamics of quantized maps: the standard map and the kicked rotator are considered to be prototype problems.

Works are also focused in the study of driven chaotic systems,[12] where the Hamiltonian H ( x , p ; R ( t ) ) {\displaystyle H(x,p;R(t))} H(x,p;R(t)) is time dependent, in particular in the adiabatic and in the linear response regimes. There is also significant effort focused on formulating ideas of quantum chaos for strongly-interacting many-body quantum systems far from semiclassical regimes. 