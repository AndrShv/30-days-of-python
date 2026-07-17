import pathlib
import runpy

import pytest

SCRIPTS_DIR = pathlib.Path(__file__).resolve().parent.parent / "1-3days"


def run_script(name):
    """Execute a script in ``1-3days`` and return its stdout lines.

    The scripts are plain top-level programs (some with hyphenated names that
    cannot be imported), so they are run in-process with ``runpy`` which keeps
    them under coverage measurement.
    """
    return runpy.run_path(str(SCRIPTS_DIR / name), run_name="__main__")


@pytest.fixture
def script_output(capsys):
    def _run(name):
        run_script(name)
        return capsys.readouterr().out.splitlines()

    return _run
