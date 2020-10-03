import platform
import sys
import os
from string import Template
from shutil import copyfile
import install_util

current_os = platform.platform()
dev_os_home = "~/dev-os"


def main():
    # TODO: Get a better logging solution
    print("\n- Installing dev-os onto system")

    if (current_os.__contains__("Darwin")):
        installMac()
    elif (current_os.__contains__("Windows")):
        installWindows()
    elif (current_os.__contains__("Linux")):
        installLinux()
    else:
        sys.exit("Script being run on an unknown OS that is not support!")


def installMac():
    print("Running installation for Darwin")

    def installStarShip():
        install_util.run_cmd(
            "curl -fsSL https://starship.rs/install.sh | bash")
        install_util.run_cmd(f"mkdir -pv ~/.config")
        install_util.link_file(f"{dev_os_home}/config/starship/config.toml",
                               "~/.config/starship.toml")

    def installBashProfile():
        install_util.link_file(
            f"{dev_os_home}/config/bash/.bashrc", "~/.bashrc")
        install_util.link_file(f"{dev_os_home}/config/bash/.bash_profile",
                               "~/.bash_profile")

    install_util.runStep("starship shell", installStarShip)
    install_util.runStep("bash profile", installBashProfile)


def installWindows():
    sys.exit("Installation for windows not yet implemented")

    # TODO Install scoop

    # TODO Install starship
    def installStarship():
        install_util.run_cmd("scoop install starship")
        copyfile(f"{dev_os_home}/config/powershell/.Microsoft.PowerShell_profile.ps1",
                 "~\Documents\PowerShell\Microsoft.PowerShell_profile.ps1")

    # TODO Bash profile


def installLinux():
    sys.exit("Installation for linux not yet implemented")
    # TODO Install starship
    # TODO Bash profile


# Run the main installation script
main()
