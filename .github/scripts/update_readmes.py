import json
from datetime import datetime
import os
import util
import re


def main():

    listings = util.getListingsFromJSON()

    util.checkSchema(listings)
    util.sortListings(listings)

    util.embedTable(listings)

    util.setOutput("commit_message", "Updating README at " + datetime.now().strftime("%B %d, %Y %H:%M:%S"))


if __name__ == "__main__":
    main()
