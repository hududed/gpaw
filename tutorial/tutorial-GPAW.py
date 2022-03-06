# creates: h2.emt.traj
from ase import Atoms
# from ase.calculators.emt import EMT
from ase.build import molecule
from ase.optimize import QuasiNewton
from gpaw import GPAW


# system = Atoms('H2', positions=[[0.0, 0.0, 0.0],
#                                 [0.0, 0.0, 1.0]])

# Atoms.set_cell((6.0, 6.0, 6.0))
# Atoms.center()

system = molecule('H2O', vacuum=3.0)
# system.set_cell((6.0, 6.0, 6.0))
# system.center()

calc = GPAW()

system.calc = calc

opt = QuasiNewton(system, trajectory='h2o.gpaw.traj')

opt.run(fmax=0.05)