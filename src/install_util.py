import os


def run_cmd(cmd):
    os.system(cmd)


def runStep(step, installation_steps):
    print(f"\nstarting {step} installation")
    installation_steps()
    print(f"{step} installation complete\n")


def link_file(src, dst):
    run_cmd(f"ln -sv {src} {dst}")
