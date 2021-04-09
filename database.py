import json
import csv
from collections import defaultdict, OrderedDict

"""A database encapsulating collections of near-Earth objects and their close approaches.

A `NEODatabase` holds an interconnected data set of NEOs and close approaches.
It provides methods to fetch an NEO by primary designation or by name, as well
as a method to query the set of close approaches that match a collection of
user-specified criteria.

Under normal circumstances, the main module creates one NEODatabase from the
data on NEOs and close approaches extracted by `extract.load_neos` and
`extract.load_approaches`.

You'll edit this file in Tasks 2 and 3.
"""


class NEODatabase:
    """A database of near-Earth objects and their close approaches.

    A `NEODatabase` contains a collection of NEOs and a collection of close
    approaches. It additionally maintains a few auxiliary data structures to
    help fetch NEOs by primary designation or by name and to help speed up
    querying for close approaches that match criteria.
    """

    def __init__(self, neos, approaches):
        """Create a new `NEODatabase`.

        As a precondition, this constructor assumes that the collections of NEOs
        and close approaches haven't yet been linked - that is, the
        `.approaches` attribute of each `NearEarthObject` resolves to an empty
        collection, and the `.neo` attribute of each `CloseApproach` is None.

        However, each `CloseApproach` has an attribute (`._designation`) that
        matches the `.designation` attribute of the corresponding NEO. This
        constructor modifies the supplied NEOs and close approaches to link them
        together - after it's done, the `.approaches` attribute of each NEO has
        a collection of that NEO's close approaches, and the `.neo` attribute of
        each close approach references the appropriate NEO.

        :param neos: A collection of `NearEarthObject`s.
        :param approaches: A collection of `CloseApproach`es.
        """
        self._neos = neos
        self._approaches = approaches

        # Writes a CSV file containing self._neo data
        with open('data/test.csv', 'w', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=self._neos[0].keys())
            writer.writeheader()
            for row in self._neos:
                writer.writerow(row)

        # Creates dict containing NEO with pdes as key
        des_dict = {rows['pdes']: rows for rows in self._neos}
        # print(json.dumps(des_dict, indent=4))

        # Writes a CSV file containing NEO pdes data
        with open('data/neo_pdes_dict.csv', 'w', newline='') as outfile:
            writer = csv.writer(outfile)
            for des in des_dict:
                for vals in des_dict[des]:
                    writer.writerow([des, vals, des_dict[des][vals]])

        # Creates a dict containing CAD data with fields as keys
        header = []  # Takes items in "fields" and places them into a list to later implement as keys to data items
        cad_dict = {}
        cad_list = []
        count = 0  # Counts through each CAD item
        for row in self._approaches.keys():
            if row == 'fields':
                for fields in self._approaches[row]:
                    header.append(fields)
            if row == 'data':
                for data in self._approaches[row]:
                    if count == len(header):
                        count = 0
                    for key in header:
                        # print(key, ": ", data[count])
                        # cad_dict = {cad_dict[key]: data[count] for cad_dict[key] in header}
                        cad_dict[key] = data[count]
                        count += 1
                    cad_list.append(json.dumps(cad_dict))
        #for dictline in cad_list:
        #    print(dictline)

        #cad_dict = {header[rows]: rows for rows in self._approaches}
        #print(json.dumps(cad_dict, indent=4))

        # dict containing NEO with name as key
        name_dict = {rows['name']: rows for rows in self._neos}
        # print(json.dumps(name_dict, indent=4))

        # Writes a CSV file containing name_dict data
        with open('data/name_dict.csv', 'w', newline='') as outfile:
            writer = csv.writer(outfile)
            for name in name_dict:
                for vals in name_dict[name]:
                    writer.writerows([name, vals, name_dict[name][vals]])


        # TODO: Link together the NEOs and their close approaches.

        # Link NEOs and their close approach using designation
        dd = {}
        count = 0
        print(cad_list[0]['des'])



        '''
        # Write dd dict to file
        # For testing purposes
        with open("data/dd_dict.csv", "w") as outfile:
            w = csv.writer(outfile)
            for key, val in dd.items():
                w.writerow([key, val])
        '''

        '''
        # Print's the designation for each CAD
        for cad_row in self._approaches:
            print(cad_row[0])

        for row in neo_link:
            for cad_row in self._approaches:
                for neo_row in self._neos:
                    if cad_row[0] in neo_row[3]:
                        neo_link[row] = {cad_row[0]: self._neos[3]}
        print(neo_link)
        '''

        # Print's the first 5 new NEO's with their matching CAD's
        '''
        for neo_row in neo[:5]:
            for cad_row in self._approaches:
                while True:
                    if neo_row[3] == cad_row[0]:
                        neo += cad_row
        print(neo[:5], "\n")
        '''

    def get_neo_by_designation(self, designation):
        """Find and return an NEO by its primary designation.

        If no match is found, return `None` instead.

        Each NEO in the data set has a unique primary designation, as a string.

        The matching is exact - check for spelling and capitalization if no
        match is found.

        :param designation: The primary designation of the NEO to search for.
        :return: The `NearEarthObject` with the desired primary designation, or `None`.
        """
        # TODO: Fetch an NEO by its primary designation.
        return None

    def get_neo_by_name(self, name):
        """Find and return an NEO by its name.

        If no match is found, return `None` instead.

        Not every NEO in the data set has a name. No NEOs are associated with
        the empty string nor with the `None` singleton.

        The matching is exact - check for spelling and capitalization if no
        match is found.

        :param name: The name, as a string, of the NEO to search for.
        :return: The `NearEarthObject` with the desired name, or `None`.
        """
        # TODO: Fetch an NEO by its name.
        return None

    def query(self, filters=()):
        """Query close approaches to generate those that match a collection of filters.

        This generates a stream of `CloseApproach` objects that match all of the
        provided filters.

        If no arguments are provided, generate all known close approaches.

        The `CloseApproach` objects are generated in internal order, which isn't
        guaranteed to be sorted meaninfully, although is often sorted by time.

        :param filters: A collection of filters capturing user-specified criteria.
        :return: A stream of matching `CloseApproach` objects.
        """
        # TODO: Generate `CloseApproach` objects that match all of the filters.
        for approach in self._approaches:
            yield approach
