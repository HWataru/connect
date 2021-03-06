# -*- coding: utf-8 -*-

from OperatorInterface import OperatorInterface
from BaseOperator import BaseOperator
from JobInterface import JobInterface
from BaseJob import BaseJob
from ThreeOps import *


class UserJob(JobInterface, BaseJob):

    def define_dataflow(self):

        op1 = Operator1('1')
        op2 = Operator2('2')
        op3 = Operator3('3')

        self.df.add_node(op1)
        self.df.add_node(op2)
        self.df.add_node(op3)

        self.df.add_edge(op1, 0, op3, 0)
        self.df.add_edge(op2, 0, op3, 1)

        th1 = self.create_thread_local_group(op1)
        th2 = self.create_thread_local_group(op2)
        th3 = self.create_thread_local_group(op3)

        self.create_device_local_group('sv0', 'CPU', th1, th2, th3)
