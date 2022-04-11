"""
This Module is used for configuration; contains the directory path, file ending, dictionary
for host names and prints errors.
"""

# disable pylint: doesn't conform to snake_case naming style
# pylint: disable=invalid-name

_UNIGENE_DIR = "/data/PROGRAMMING/assignment5"
_UNIGENE_FILE_ENDING = "unigene"


def get_unigene_directory():
    """ Returns the absolute path for directory that will be used """
    return _UNIGENE_DIR


def get_unigene_extension():
    """ Returns the file ending for the gene data """
    return _UNIGENE_FILE_ENDING


def get_host_keywords():
    """
    This function creates a dictionary to map the scientific names
    of the host species to common names.

    @return host_keywords : dict
        calling the function with no arguments returns the dictionary of mapped
        names
    """
    homo_sap = "Homo_sapiens"
    bos_tarus = "Bos_taurus"
    eq_cab = "Equus_caballus"
    mus_musc = "Mus_musculus"
    ovis_aries = "Ovis_aries"
    rat_norv = "Rattus_norvegicus"

    host_keywords = {
        "homo_sapiens": homo_sap,
        "bos_taurus": bos_tarus,
        "equus_caballus": eq_cab,
        "mus_musculus": mus_musc,
        "ovis_aries": ovis_aries,
        "rattus_norvegicus": rat_norv,
        "homo sapiens": homo_sap,
        "human": homo_sap,
        "humans": homo_sap,
        "bos taurus": bos_tarus,
        "cow": bos_tarus,
        "cows": bos_tarus,
        "equus caballus": eq_cab,
        "horse": eq_cab,
        "horses": eq_cab,
        "mus musculus": mus_musc,
        "mouse": mus_musc,
        "mice": mus_musc,
        "ovis aries": ovis_aries,
        "sheep": ovis_aries,
        "sheeps": ovis_aries,
        "rattus norvegicus": rat_norv,
        "rat": rat_norv,
        "rats": rat_norv}
    return host_keywords


def get_error_string_4_IOError(file=None, mode=None):  # error: get_fh(file, "1234")
    """ Print the invalid argument type message and exits the program """
    print(f"Could not open the file: {file} for mode '{mode}'")


def get_error_string_4_ValueError():  # error:  get_fh(file, "1234")
    """ Print the invalid argument type message and exits the program """
    print("Invalid argument Value for opening a file for reading/writing")


def get_error_string_4_TypeError():  # error: get_fh(file, "r", "w")
    """ Print the invalid argument type message and exits the program """
    print("Invalid argument Type passed in:")


def get_error_string_4_FileNotFoundError(file=None):
    """ Print the invalid argument type message and exits the program """
    print(f"Could not create the directory (invalid argument): {file}")
