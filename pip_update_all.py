# MIT License

# Copyright (c) 2016 markgot

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import sys

from subprocess import call
import time
import pip

t1 = time.clock()

i = 1
distlen = len(pip.get_installed_distributions())
f = open(os.devnull, 'w')
t2 = t1

for dist in pip.get_installed_distributions():
    t_temp = time.clock()
    print('[' + '{:.2f}'.format(t_temp - t1) + ', delta: ' + '{:.2f}'.format(t_temp - (t2 + t1)) + ']: package number ' + str(i) + ' of ' + str(distlen) + ': ' + str(dist))

    t2 = t_temp
    old_std = sys.stdout
    sys.stdout = f
    call('pip install --upgrade >nul 2>&1' +
         dist.project_name, shell=True)  # add >nul 2>&1
    sys.stdout = old_std

    i += 1
