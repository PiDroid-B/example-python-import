from pathlib import Path


def f():
    print(f"""
### {Path(__file__).relative_to(Path.cwd().parent)}
  app.py : 
    import example_python_import.f_mymodule as my_module
    my_module.f()""")
