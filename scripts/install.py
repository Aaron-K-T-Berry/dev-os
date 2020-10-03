import platform
import sys
import os
from string import Template
from shutil import copyfile

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


def runStep(step, installation_steps):
    print(Template("\nstarting $step installation").substitute(step=step))
    installation_steps()
    print(Template("$step installation complete\n").substitute(step=step))


def link_file(src, dst):
    os.system(f"ln -sv {src} {dst}")


def installMac():
    print("Running installation for Darwin")

    def installStarShip():
        os.system("curl -fsSL https://starship.rs/install.sh | bash")
        os.system(f"mkdir -pv ~/.config")
        link_file(f"{dev_os_home}/config/starship/config.toml",
                  "~/.config/starship.toml")

    def installBashProfile():
        link_file(f"{dev_os_home}/config/bash/.bashrc", "~/.bashrc")
        link_file(f"{dev_os_home}/config/bash/.bash_profile",
                  "~/.bash_profile")

    runStep("starship shell", installStarShip)
    runStep("bash profile", installBashProfile)


def installWindows():
    sys.exit("Installation for windows not yet implemented")

    # TODO Install scoop

    # TODO Install starship
    def installStarship():
        os.system("scoop install starship")
        copyfile(f"{dev_os_home}/config/powershell/.Microsoft.PowerShell_profile.ps1",
                 "~\Documents\PowerShell\Microsoft.PowerShell_profile.ps1")

    # TODO Bash profile


def installLinux():
    sys.exit("Installation for linux not yet implemented")
    # TODO Install starship
    # TODO Bash profile


# Run the main installation script
main()
