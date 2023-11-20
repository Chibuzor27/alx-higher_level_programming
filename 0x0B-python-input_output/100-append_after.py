#!/usr/bin/python3
"""Module"""


def append_after(filename="", search_string="", new_string=""):
    """Append after"""
    pg = ""
    if filename != "" or filename is not None:
        with open(filename, encoding="utf-8") as f:
            line = None
            while line != "":
                line = f.readline()
                pg = pg + line
                if search_string in line:
                    pg = pg + new_string

        with open(filename, "w", encoding="utf-8") as n:
            n.write(pg)
