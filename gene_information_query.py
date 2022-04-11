#!/usr/bin/env python3
# gene_information_query.py
"""
This program takes an input of a host name and a gene name outputs a list of
expressed tissues in the selected gene.

Sample command for running the program:
python3 gene_information_query.py -host Humans -gene TGM1
"""
import re
import sys
import argparse
from assignment5 import config
from assignment5 import my_io

# diabling: line too long
#           if-else-return erroruse
#           unnecessary use of comprehension
# pylint: disable=C0301
# pylint: disable=R1705
# pylint: disable=R1721


def main():
    """"Main Business Logic"""
    args = get_cli_args()
    in_host = args.host
    in_gene = args.gene
    # modifying input strings
    host = modify_host_name(in_host)
    gene = in_gene.upper()
    # getting the file path
    file = "/".join((config.get_unigene_directory(), host, gene + "." +
                     config.get_unigene_extension()))

    # checking if inputted gene name is valid
    if my_io.is_valid_gene_file_name(file):
        print('\nFound Gene {} for {}'.format(gene, host), end='\n', file=sys.stderr)
    else:
        print("Not found")
        print(f"Gene {gene} does not exist for {host}. exiting now...", file=sys.stderr)
        sys.exit()

    # opening selected directory and file
    fh_in = my_io.get_fh(file=file, mode="r")

    # getting expressed tissues for selected gene
    gene_data = get_gene_data(fh_in)
    print_output(host, gene, gene_data)

    # closing the file
    fh_in.close()


def modify_host_name(host_name):
    """
    This function takes the user inputted host name and converts it to the scientific name
    if name is not found in the dictionary, system exits and prints list of valid host names
    @param host_name : input str
        user-entered host name at command line
    @return value : modified str
        scientific name of inputted host
    """
    host_dict = config.get_host_keywords()
    key = str.lower(host_name)
    if key in [x for x in list(host_dict.keys())]:
        value = host_dict[key]
        return value
    else:
        return _print_host_directories()


def _print_host_directories():
    """
    This is a helper function that prints all valid directories and exits the program
    @return : None, system exit
        prints to STDERR
    """
    host_dict = config.get_host_keywords()
    all_names = list(host_dict.keys())
    # printing error message
    print('\n \n{}'.format("Either the Host Name you are searching for is not in the database"),
          file=sys.stderr)
    print('\n{}'.format('or If you are trying to use the scientific name please put the name in double quotes:'),
          file=sys.stderr)
    print('\n{}'.format('"Scientific name"'))

    # printing scientific names:
    sci_names = sorted(all_names[:6])
    print('\n{}'.format('Here is a (non-case sensitive) list of available Hosts by scientific name'), end="\n\n  ",
          file=sys.stderr)
    _print_num_list(sci_names)

    # printing common names:
    print('\n \n{}'.format('Here is a (non-case sensitive) list of available Hosts by common name'), end="\n\n  ",
          file=sys.stderr)
    com_names = sorted(all_names[6:])
    _print_num_list(com_names)
    print("\n")
    sys.exit()


def _print_num_list(names):
    """
    This helper function inputs a list of names and prints a formatted, numbered
    list
    @param names : list of names to be numbered
        list of either tissue or host names
    @return : None
        prints numbered list of names
    """
    line = "{{: >{}}}. {{}}".format(len(str(len(names))))
    for i, item in enumerate(names, 1):
        print(line.format(i, item.capitalize()), end='\n  ', file=sys.stderr)


def get_gene_data(file):
    """
    This function reads the selected file line by line and extracts a list
    of expressed tissues in the host of interest for the gene selected and
    sorts the expressed tissues
    @param file : opened file for reading
        After input host name is modified and gene name is checked for validity,
        the opened full file path is inputted
    @returns gene_data : list
        sorted list of expressed tissues
    """
    tiss_line = []
    for line in file:
        if re.findall('EXPRESS', line):
            tiss_line.append(line.rstrip())

    # converting the list to str, replacing the | with a comma, and removing []  & '' characters
    tissue_str = str(tiss_line).replace("|", ",").replace('[', '').replace(']', '').replace("'", '')

    # using regex to extract only the tissues
    match = re.search("([^EXPRESS]) (.+)", tissue_str)
    if match:
        tissue_strig = match.group(1)
        tissue_strig = match.group(2)
    # splitting the string by commas
    exprs_tissues = [x.strip() for x in tissue_strig.split(',')]
    gene_data = sorted(exprs_tissues)
    return gene_data


def print_output(host, gene, gene_data):
    """
    Final function that takes the user selected host, gene name, the extracted list of tissues and prints the
    species selected, the gene selected, how many tissues are expressed and a numbered list of the tissues
    @param host : str
        command line inputted host name
    @param gene : str
        command line inputted gene name
    @param gene_data : list
        outputted list from get_gene_data with sorted tissues
    @return : None
        prints expresed tissue list
    """
    host = host.replace("_", " ")
    line = "{{: >{}}}. {{}}".format(len(str(len(gene_data))))
    print("In {}, There are {} tissues that {} is expressed in:".format(host, str(len(gene_data)), gene),
          end="\n\n  ", file=sys.stderr)
    # Loop to print all items and their respective number
    for i, item in enumerate(gene_data, 1):
        print(line.format(i, item.capitalize()), end='\n  ', file=sys.stderr)
    print("\n")


def get_cli_args():
    """
    Command line arguments -host and -gene, setting default args to
    host "Humans" and gene "TGM1"
    @return: Instance of argparse arguments
    """
    parser = argparse.ArgumentParser(description='Give the Host and Gene name')

    parser.add_argument('-host', nargs='?', type=str, help='Name of Host',
                        default='Humans')
    parser.add_argument('-gene', nargs='?', type=str, help='Name of Gene',
                        default="TGM1")
    return parser.parse_args()


if __name__ == '__main__':
    main()
