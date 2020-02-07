from pathlib import Path


def f():
    print(f"""
### {Path(__file__).relative_to(Path.cwd().parent)}
  app.py : 
    from example_python_import.modules.f_module_from import f as f_module_from_fonc
    f_module_from_fonc()""")
