#!/usr/bin/python

import os
import sys
import os.path as path
sys.path.append(path.join(path.dirname(path.abspath(sys.argv[0])), "..", "repos", "mesa_ci"))
import build_support as bs


bs.build(bs.PerfBuilder("gfxbench5.car_chase_o", iterations=5, windowed=True))

