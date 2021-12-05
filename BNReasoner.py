import sys
import networkx as nx
from typing import Union
from BayesNet import BayesNet


class BNReasoner:
    def __init__(self, net: Union[str, BayesNet]):
        """
        :param net: either file path of the bayesian network in BIFXML format or BayesNet object
        """
        if type(net) == str:
            # constructs a BN object
            self.bn = BayesNet()
            # Loads the BN from an BIFXML file
            self.bn.load_from_bifxml(net)
        else:
            self.bn = net

    # TODO: This is where your methods should go

bn_graph = BNReasoner("testing/dog_problem.BIFXML")     # Comment this and uncomment the next
# bn_graph = BNReasoner("testing/lecture_example.BIFXML")   # Comment this and uncomment the next
# bn_graph = BNReasoner("testing/lecture_example2.BIFXML")  # Comment this and uncomment the next

""" Code which creates files containing true/false to d-separateness of combination of nodes from each BIFXML file.

var_set = (("bowel-problem", "family-out", "light-on", "dog-out", "hear-bark"),
           ("Winter?", "Sprinkler?", "Rain?", "Wet Grass?", "Slippery Road?"),
           ("I", "J", "Y", "X", "O"))

i = 0   # change values here (0, 1 or 2) to shift to the next BIFXML file.
with open(f'd-seps_in_bn_graph[{i}].txt', 'w') as f:
    for var1 in var_set[i]:
        for var2 in var_set[i]:
            if var2 is not var1:
                for var3 in var_set[i]:
                    if var3 is not var2 or var1:
                        print(f"Is {var1} d-separated from {var2} given {var3}? ", nx.d_separated(bn_graph.bn.structure, {var1}, {var2}, {var3}), file=f)
"""

# print (bn_graph.bn.draw_structure())

def dsep(bn_graph):
    # module for d-separation.
    # needs x, y, and z nodes as input.
    # check if x is d-separated from y given z. 

    return None