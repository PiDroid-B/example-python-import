# PEP 8 unfriendly, just for better understanding

import example_python_import.f_mymodule as my_module
my_module.f()

import example_python_import.modules.f_module_import as f_module_import
f_module_import.f()

from example_python_import.modules.f_module_from import f as f_module_from_fonc
f_module_from_fonc()

import example_python_import.pkg_import as pkg_import
pkg_import.f_pkg_import.f()

from example_python_import.pkg_importall.f_pkg_importall import *
pkg_importall_f()
pkg_importall_f2()

import example_python_import.pkg_import_init_all as pkg_init_all
pkg_init_all.f1()
pkg_init_all.f2()
