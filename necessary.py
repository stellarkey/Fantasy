import os
import sys
import traceback
import chardet
import random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx

def main():
    EH = EnvironmentalHelper()
    EH.install_requirements()

class EnvironmentalHelper():
    def install_requirements(self):
        import os
        os.system('pip3 install chardet')
        os.system('pip3 install numpy')
        os.system('pip3 install pandas')
        os.system('pip3 install matplotlib')
        os.system('pip3 install seaborn')
        os.system('pip3 install PyQt5')
        os.system('pip3 install networkx')

if __name__ == '__main__':
    main()
    