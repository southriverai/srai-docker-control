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


def release_for_repository_tag(command_handler: CommandHandlerBase, repository_url: str, version: str):
    # check if the repository exists with that tag
    path_dir_repository = "test"  # command_handler.get_current_dir()
    # remove current version
    command_handler.execute("rm -rf *")
    # clone the repository
    command_handler.execute(f"git clone {repository_url}")
