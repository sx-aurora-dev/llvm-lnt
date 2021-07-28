import plistlib


def _matches_format(path_or_file):
    try:
        plistlib.readPlist(path_or_file)
        return True
    except Exception:
        return False

def readPlist(file_name):
  # TODO plistlib.readPlist,
  pass

def writePlist(root_dist, file_path):
  # TODO plistlib.writePlist,
  pass

format = {
    'name': 'plist',
    'predicate': _matches_format,
    'read': readPlist,
    'write': writePlist,
}
