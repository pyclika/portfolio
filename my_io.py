"""
Submodule my_io; utlizes submodule config for printing filehandling errors
"""

import os
from assignment5 import config


def get_fh(file=None, mode=None):
    """
    filehandle : get_fh(file, "r")
    Takes : 2 arguments; file name and mode
    @param file: The file to open for the mode
    @parm mode: They way to open the file, ex. "r" "w"
    @return: filehandle
    """
    try:
        fobj = open(file, mode)
        return fobj
    except FileNotFoundError as err:
        config.get_error_string_4_FileNotFoundError(file)
        raise err
    except IOError as err:
        config.get_error_string_4_IOError(file, mode)
        raise err
    except ValueError as err:
        config.get_error_string_4_ValueError()
        raise err
    except TypeError as err:
        config.get_error_string_4_TypeError()
        raise err


def is_valid_gene_file_name(file_path):
    """
    This function checks if the file path with the input host and gene name to search exists.
    @param file_path : joined file path with modified host name and gene name
    @return : if file name exists returns True and if not, reutrns False
    """
    return os.path.lexists(file_path)
