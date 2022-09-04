import subprocess  # nosec


def run_a_bash_command(await_compilation, bash_command, verbose):
    """Runs a bash commands from Python.

    :param await_compilation:
    :param bash_command:
    :param verbose:
    """
    if await_compilation:
        if verbose:
            subprocess.call(bash_command, shell=True)  # nosec
        else:
            subprocess.call(
                bash_command,
                shell=True,  # nosec
                stderr=subprocess.DEVNULL,
                stdout=subprocess.DEVNULL,
            )
    else:
        if verbose:
            subprocess.Popen(bash_command, shell=True)  # nosec
        else:
            subprocess.Popen(
                bash_command,
                shell=True,  # nosec
                stderr=subprocess.DEVNULL,
                stdout=subprocess.DEVNULL,
            )
