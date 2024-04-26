import subprocess

from srai_core.command_handler_base import CommandHandlerBase


def check_git_installed():
    try:
        subprocess.check_output(["git", "--version"])
        return True
    except FileNotFoundError:
        return False


def check_pending_changes():
    try:
        output = subprocess.check_output(["git", "status", "--porcelain"])
        return len(output) > 0
    except subprocess.CalledProcessError:
        return False
