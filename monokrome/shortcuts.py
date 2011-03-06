def project_path(dirname):
    """ Gets a path relative to the project's root directory. """

    import os

    if 'VIRTUAL_ENV' in os.environ:
        project_directory = os.path.abspath(os.environ['VIRTUAL_ENV'])
    else:
        project_directory = os.path.expanduser('~')

    return os.sep.join([project_directory, dirname])

def asset_path(dirname, assets_directory='assets'):
    """ Gets a path under the project's assets directory. """

    import os

    return project_path(os.sep.join([assets_directory, dirname]))
