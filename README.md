devconf-2014-ipython
====================

Repository with stuff for ipython lab at Developer Conference 2014.

Files
-----

### Configuration

* init.ipy
* ipython_config.py

### Sample for recursive reloading

* mod/

```python
from IPython.lib.deepreload import reload
sys.path.insert(1, THIS_REPO + "/mod/")
```

### Plotting

* plot-3d.py
* plot-imshow.py
* plot-scatter.py

```
$ ipython --pylab
```

### Embedding ipython

* run_ipy.py

### A little bit more complex sample

* simple.py

### Guide to presenter

* slides.txt


Sample usage of simple.py
-------------------------

```
$ curl http://www.jakpsatweb.cz/ 2>/dev/null | xargs -0 python simple.py
```

Reference
=========

[1]: http://www.loria.fr/~rougier/teaching/matplotlib/        "Plots"
[2]: http://ipython.org/ipython-doc/dev/                      "Official Documentation"

