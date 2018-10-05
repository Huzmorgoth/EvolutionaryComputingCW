import SwarmPackagePy
from SwarmPackagePy import testFunctions as tf
from SwarmPackagePy import animation, animation3D

alh = SwarmPackagePy.pso(50, tf.ackley_function, -10, 10, 2, 20, w=0.5, c1=1, c2=1)
animation(alh.get_agents(), tf.ackley_function, -10, 10)
animation3D(alh.get_agents(), tf.ackley_function, -10, 10)

alh = SwarmPackagePy.pso(50, tf.sphere_function, -10, 10, 2, 20, w=0.5, c1=1, c2=1)