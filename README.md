# example-python-import

just run app.py

OUTPUT :
```
### example_python_import/f_mymodule.py
  app.py : 
    import example_python_import.f_mymodule as my_module
    my_module.f()

### example_python_import/modules/f_module_import.py
  app.py : 
    import example_python_import.modules.f_module_import as f_module_import
    f_module_import.f()

### example_python_import/modules/f_module_from.py
  app.py : 
    from example_python_import.modules.f_module_from import f as f_module_from_fonc
    f_module_from_fonc()

### example_python_import/pkg_import/f_pkg_import.py
  app.py : 
    import example_python_import.pkg_import as pkg_import
    pkg_import.f_pkg_import.f()
    # example_python_import.pkg_import.const not available
  pkg_import/__init__.py
    import example_python_import.pkg_import.f_pkg_import

### example_python_import/pkg_importall/f_pkg_importall.py
  app.py : 
    from example_python_import.pkg_importall.f_pkg_importall import *
    pkg_importall_f()
    pkg_importall_f2()
    # example_python_import.pkg_importall.const not available
  pkg_import/__init__.py
    import example_python_import.pkg_importall.f_pkg_importall

### example_python_import/pkg_import_init_all/f_pkg_import_init_all.py
  app.py : 
    import example_python_import.pkg_import_init_all as pkg_init_all
    pkg_init_all.f1()
    pkg_init_all.f2()
    # example_python_import.pkg_import_init_all.const not available
  pkg_import/__init__.py
    from example_python_import.pkg_import_init_all.f_pkg_import_init_all import f1, f2
```