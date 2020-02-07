from . import f_const


from pathlib import Path


def f1():
    print(f"""
### {Path(__file__).relative_to(Path.cwd().parent)}
  app.py : 
    import example_python_import.pkg_import_init_all as pkg_init_all
    pkg_init_all.f1()
    pkg_init_all.f2()
    {f_const.no_available}
  pkg_import/__init__.py
    from example_python_import.pkg_import_init_all.f_pkg_import_init_all import f1, f2""")


def f2():
    pass
