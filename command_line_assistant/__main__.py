import sys

NOTICE_MESSAGE: str = """\
If you have installed command-line-assistant by using pypi, uninstall it from your system, and install the command line assistant tool by using RHEL repositories.

1. Uninstall the command line assistant installed with `pypi`:
$ pip uninstall command-line-assistant

2. Install command lina assistant by using RHEL repositories
$ sudo dnf install command-line-assistant"""


def main() -> int:
    print(NOTICE_MESSAGE, file=sys.stderr)
    return 1

if __name__ == "__main__":
    sys.exit(main())