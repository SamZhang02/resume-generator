import subprocess
from pathlib import Path


def format_tex(path: Path):
    """
    Format a tex file using "latexindent" given a path.
    """

    if not path.exists():
        raise FileNotFoundError(f"The file {path} does not exist.")
    if path.suffix != ".tex":
        raise ValueError(f"The file {path} is not a .tex file.")

    try:
        _ = subprocess.run(
            ["latexindent", "-w", str(path)],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        print(f"Formatted {path} successfully.")
    except subprocess.CalledProcessError as e:
        print(f"latexindent failed with error:\n{e.stderr.decode('utf-8')}")
        raise
