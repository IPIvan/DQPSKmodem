"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""
#pi/4 dqpsk modulator / created by Ivan Penchev Ivanov aka IP_Ivanov
import numpy as np
from gnuradio import gr
import cmath


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, example_param=1.0):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='pi/4 DiffEncoder',   # will show up in GRC
            in_sig=[np.complex64],
            out_sig=[np.complex64]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        #print("\nMembers and methods:\n{}\n".format(dir(self))) #show all member functions of this block
        #self.set_min_noutput_items(256)
        self.example_param = example_param
        self.set_output_multiple(256)
        #self.set_history(2)
        self.last_output_item = 1 # sets initial previous output item 
        #self.LUT_phase_trans = [complex(0.70711,0.70711), complex(-0.70711,0.70711), complex(0.70711,-0.70711), complex(-0.70711,-0.70711)]

    def work(self, input_items, output_items):
        inlen = len(input_items[0])
        #print(inlen)
        #print(input_items[0])
        #output_items[0][:] = input_items[0][1:len(input_items[0])] * self.example_param
        #print("input_items[0]={} self.example_param={}".format(input_items[0], self.example_param))
        
        i = 0
        output_items[0][i] = self.last_output_item*input_items[0][i]
        i=i+1
        while i < (inlen):
            #print("output_items[0][i-1]",output_items[0][i-1])
            #print("input_items[0][i]",input_items[0][i])
            output_items[0][i] = output_items[0][i-1] * input_items[0][i]
            #output_items[0][i] = complex(round(output_items[0][i].real,15),round(output_items[0][i].imag,15)) 
            #print("output_items[0][i]",output_items[0][i])
            i = i + 1
            #print("item0={} item1={}".format(item0, item1))
            self.last_output_item = output_items[0][i-1]
        #print(i)
        #print(self.last_output_item)
        return len(output_items[0])

