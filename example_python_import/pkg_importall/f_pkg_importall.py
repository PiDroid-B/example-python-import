from . import f_const


from pathlib import Path


def pkg_importall_f():
    print(f"""
### {Path(__file__).relative_to(Path.cwd().parent)}
  app.py : 
    from example_python_import.pkg_importall.f_pkg_importall import *
    pkg_importall_f()
    pkg_importall_f2()
    {f_const.no_available}
  pkg_import/__init__.py
    import example_python_import.pkg_importall.f_pkg_importall""")


def pkg_importall_f2():
    pass
