from pathlib import Path


def f():
    print(f"""
### {Path(__file__).relative_to(Path.cwd().parent)}
  app.py : 
    import example_python_import.modules.f_module_import as f_module_import
    f_module_import.f()""")
