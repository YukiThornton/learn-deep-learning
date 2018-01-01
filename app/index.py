# from ch01 import simple_graph
# simple_graph.show()
#
# from ch02 import and_gate, nand_gate, or_gate, xor_gate
# and_gate.print_and()
# nand_gate.print_nand()
# or_gate.print_or()
# xor_gate.print_xor()
#
# from ch03 import step_function, sigmoid, relu
# step_function.draw()
# sigmoid.draw()
# relu.draw()
#
# from ch03 import neuralnet_forward
# import numpy as np
# neuralnet_forward.forward_and_print(np.array([1.0, 0.5]))
#
# from ch03.mnist_show import img_save, get_any_image
# img_save(get_any_image())
#
# from ch03.neuralnet_mnist import execute, batch
# execute()
# batch(100)

# from ch04.gradient import create_gradient_graph, create_descent_graph
# create_gradient_graph()
# create_descent_graph()

# from ch04.gradient_simplenet import execute
# execute()

from ch04.train_neuralnet import train
train()

print("Done!")
