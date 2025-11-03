#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# SPDX-License-Identifier: MIT

"""External pytest checks by pytest on greeter.py."""


import os
import subprocess

import pytest

PRG = "src/app/greeter.py"


@pytest.mark.blackbox
def test_script_exists() -> None:
    """Check for the script's presence."""
    assert os.path.isfile(PRG), f"script {PRG} was not found"


@pytest.mark.parametrize(
    "cli_in, cli_out",
    [
        (["python", PRG], "Hello Orgmode!"),
        (["python", PRG, "-n", "Markdown"], "Hello Markdown!"),
        (["python", PRG, "-g"], "Good bye Orgmode!"),
        (["python", PRG, "-g", "-n", "Markdown"], "Good bye Markdown!"),
    ],
)
def test_greet_and_bye(capfd, cli_in: list, cli_out: str) -> None:
    """Probe the script by a few black-box checks."""
    subprocess.run(cli_in, check=True)
    out, err = capfd.readouterr()
    out = str(out).strip()
    assert out == cli_out
