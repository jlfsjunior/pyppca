# pyppca
Probabilistic PCA which is applicable also on data with missing values.
Missing value estimation is typically better than NIPALS but also slower to compute and uses more memory. 
Built on [code by Sheridan Beckwith Green](https://github.com/shergreen/pyppca) which in turn is a port to Python of [the implementation by Jakob Verbeek](http://lear.inrialpes.fr/~verbeek/software.php).

#### Usage
```
from pyppca import ppca
C, ss, M, X, Ye = ppca(Y,d,dia)
```

#### Installation, dev and test
Installation is most easily done with `pip install git+https://github.com/el-hult/pyppca`.

Development is most easily done in a local fork of this repo.

Test suites are developed written in PyTest. You can for example run them with `pip install pytest` and
then `python -m pytest`. 

Current version has been tested on Python 3.7.3.