
```
C:\Users\Turtle\Anaconda3\envs\tensorflow\pythonw.exe C:/Users/Turtle/PycharmProjects/LinearRegressionGrades/Regression.py
Traceback (most recent call last):
  File "C:/Users/Turtle/PycharmProjects/LinearRegressionGrades/Regression.py", line 3, in <module>
    import sklearn
  File "C:\Users\Turtle\Anaconda3\envs\tensorflow\lib\site-packages\sklearn\__init__.py", line 82, in <module>
    from .base import clone
  File "C:\Users\Turtle\Anaconda3\envs\tensorflow\lib\site-packages\sklearn\base.py", line 20, in <module>
    from .utils import _IS_32BIT
  File "C:\Users\Turtle\Anaconda3\envs\tensorflow\lib\site-packages\sklearn\utils\__init__.py", line 27, in <module>
    from .fixes import np_version
  File "C:\Users\Turtle\Anaconda3\envs\tensorflow\lib\site-packages\sklearn\utils\fixes.py", line 18, in <module>
    import scipy.stats
  File "C:\Users\Turtle\Anaconda3\envs\tensorflow\lib\site-packages\scipy\stats\__init__.py", line 384, in <module>
    from .stats import *
  File "C:\Users\Turtle\Anaconda3\envs\tensorflow\lib\site-packages\scipy\stats\stats.py", line 179, in <module>
    from scipy.spatial.distance import cdist
  File "C:\Users\Turtle\Anaconda3\envs\tensorflow\lib\site-packages\scipy\spatial\__init__.py", line 102, in <module>
    from ._procrustes import procrustes
  File "C:\Users\Turtle\Anaconda3\envs\tensorflow\lib\site-packages\scipy\spatial\_procrustes.py", line 11, in <module>
    from scipy.linalg import orthogonal_procrustes
  File "C:\Users\Turtle\Anaconda3\envs\tensorflow\lib\site-packages\scipy\linalg\__init__.py", line 195, in <module>
    from .misc import *
  File "C:\Users\Turtle\Anaconda3\envs\tensorflow\lib\site-packages\scipy\linalg\misc.py", line 5, in <module>
    from .blas import get_blas_funcs
  File "C:\Users\Turtle\Anaconda3\envs\tensorflow\lib\site-packages\scipy\linalg\blas.py", line 215, in <module>
    from scipy.linalg import _fblas
ImportError: DLL load failed: The file cannot be accessed by the system.

Process finished with exit code 1
```


```
from scipy.linalg import _fblas
ImportError: DLL load failed: The file cannot be accessed by the system.
```



Facts
====
	* Sklean on Windows
	* python 3.7

Assumptions:
============
	* the thing we can't load is `_fblas`


Questions for Runnned Trimmed:
===
	* python version?
	* anaconda

# Which of these imports is causing the failure
```
import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
```

```
import sklearn
```

Theories
========
	* Begin Theory 1: we are missing some library that needs to be installed
                    outside of python for one for one of these scientific things


Begin's Thoughts:
---
	- You see you see an error about DLL, or C libraries, or libsys, you are missing dependencies outside of python

Open Questions:
---
	* Which library are we importing that causes the error?
	* What is linalg?
	* What us `_fblas`
	* What does DLL mean -> (Dynamically Linked Library)








