# ft_package

This package provides my version of the tqdm function.

To build the package : 
```
pip install --upgrade setuptools wheel
pip install --upgrade build
python -m build 
pip install ./dist/ft_package-0.0.1-py3-none-any.whl

```

Check that it is installed:
```
pip list
pip show -v ft_package
```

Usage is :

```
from time import sleep
from ft_package import ft_tqdm

for elem in ft_tqdm(range(10)):
    sleep(0.005)

print()

```