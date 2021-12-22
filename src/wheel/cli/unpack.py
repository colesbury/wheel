import os.path

from ..wheelfile import WheelFile


def unpack(path, dest='.'):
    """Unpack a wheel.

    Wheel content will be unpacked to {dest}/{name}-{ver}, where {name}
    is the package name and {ver} its version.

    :param path: The path to the wheel.
    :param dest: Destination directory (default to current directory).
    """
    with WheelFile(path) as wf:
        namever = wf.parsed_filename.group('namever')
        destination = os.path.join(dest, namever)
        print(f"Unpacking to: {destination}...", end='', flush=True)
        wf.extractall(destination)

    print('OK')
