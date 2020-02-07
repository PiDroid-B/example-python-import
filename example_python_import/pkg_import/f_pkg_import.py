from . import f_const


from pathlib import Path


def f():
    print(f"""
### {Path(__file__).relative_to(Path.cwd().parent)}
  app.py : 
    import example_python_import.pkg_import as pkg_import
    pkg_import.f_pkg_import.f()
    {f_const.no_available}
  pkg_import/__init__.py
    import example_python_import.pkg_import.f_pkg_import""")
