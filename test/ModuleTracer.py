import unittest
import torch
import torch.nn as nn
from mirror.ModuleTracer import *
import pprint
from mirror.tree import Tracer


class MyModule(nn.Module):
    def __init__(self):
        super(MyModule, self).__init__()


        self.linear =  nn.Sequential(
                                   nn.Conv2d(32, 32, kernel_size=1),
                                   nn.BatchNorm2d(32)
                               )

        self.conv = nn.Sequential(nn.Conv2d(3, 32, kernel_size=3),
                                  nn.ReLU())

    def forward(self, x):
        x = self.conv(x)
        x = self.linear(x)
        return x

class ModuleTracerTest(unittest.TestCase):
    def test(self):
        module = MyModule()
        tracer = ModuleTracer(module)
        x = torch.ones((1,3,28,28))
        tracer(x)
        # tracer_dict = tracer.__dict__()
        pprint.pprint(tracer.to_JSON())

        tracer = Tracer(module)
        tracer(x)
        pprint.pprint(tracer.serialized)
