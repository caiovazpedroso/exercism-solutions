"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """
    return record[1]

def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """
    return tuple(coordinate)

def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """
    azara_coordinate = ()
    rui_coordinate = ()
    if isinstance(get_coordinate(azara_record), str):
        azara_coordinate = convert_coordinate(get_coordinate(azara_record))
    else:
        azara_coordinate = get_coordinate(azara_record)
    if isinstance(get_coordinate(rui_record), str):
        rui_coordinate = convert_coordinate(get_coordinate(rui_record))
    else:
        rui_coordinate = get_coordinate(rui_record)
    return bool(azara_coordinate == rui_coordinate)

def create_record(azara_record, rui_record):
    """Combine the two record types (if possible)
    and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible),
    or the string "not a match" (if incompatible).
    """
    if compare_records(azara_record, rui_record):
        return azara_record + rui_record
    return "not a match"

def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records.

    :param combined_record_group: tuple - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.

    The return statement should be a multi-lined string with items separated by newlines.

    (see HINTS.md for an example).
    """
    cleansed = []
    cleansed_string = ""
    index = 0
    while index < len(combined_record_group):
        cleansed.append(combined_record_group[index][0:1] + combined_record_group[index][2:])
        cleansed_string += str(cleansed[index]) + "\n"
        index += 1
    return cleansed_string
