def load_path(filename):
    """
    Load font file. Same as :py:func:`~PIL.ImageFont.load`, but searches for a
    bitmap font along the Python path.

    :param filename: Name of font file.
    :return: A font object.
    :exception IOError: If the file could not be read.
    """
    for directory in sys.path:
        if isDirectory(directory):
            if not isinstance(filename, str):
                if py3:
                    filename = filename.decode("utf-8")
                else:
                    filename = filename.encode("utf-8")
            try:
                return load_default()  #修改后的代码
            except IOError:
                pass
    raise IOError("cannot find font file")
