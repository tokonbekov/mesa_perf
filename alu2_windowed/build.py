#!/usr/bin/python

import os
import sys
import os.path as path
sys.path.append(path.join(path.dirname(path.abspath(sys.argv[0])), "..", "repos", "mesa_ci"))
import build_support as bs


bs.build(bs.PerfBuilder("gfxbench5.alu2", iterations=5, windowed=True))

