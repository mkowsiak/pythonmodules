[![Price](https://img.shields.io/badge/price-FREE-0098f7.svg)](https://github.com/mkowsiak/pythonmodules/blob/master/LICENSE.md)
[![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/mkowsiak/pythonmodules/blob/master/LICENSE.md)
# Sample code demonstrating Python modules

Very simple Python code that demonstrates how to use Python modules.

# Project structure

    .
    |-- LICENSE                               - MIT license file
    |-- README.md                             - This README.md file
    |-- module                                - Python sub-module
    |   |-- __init__.py                       - marker for making directory a module
    |   `-- module_sub.py                     - contains fun_sub and fun_sub_2
    |-- module_root.py                        - module with fun_root
    |-- simple_explicit_import.py             - will fail to execute fun_sub_2
    |                                           as we don't import it explicitly
    |-- simple_import_all.py                  - import all symbols from module_sub
    |                                           and module_root; we don't have to prefix
    |                                           symbols with module names
    `-- simple_import_module.py               - import modules only; we have to prefix
                                                imported symbols with name of the module
                                                eg.: module_root.fun_root()
# Clonning

    > git clone https://github.com/mkowsiak/pythonmodules

# Running

    > cd pythonmodules
    > python pythonmodules/simple_explicit_import.py
    > python pythonmodules/simple_import_all.py
    > python pythonmodules/simple_import_module.py
   
    # you can run all the samples using find
    > find . -name "simple_*" -exec python {} \;

# Known limitations

Samples are realy basic, and illustrate how to import modules inside your code

