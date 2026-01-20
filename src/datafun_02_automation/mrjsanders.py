"""mrjsanders.py - Project script.

Author: mrjsanders
Date: 2026-01

Practice key Python skills:
- docstring comments used at the start of each module and function
- pathlib for cross-platform file paths
- creating and writing files
- type hints (explicit types)
- logging (preferred over print)
- repetition patterns:
  - for year in range(...)
  - for item in list
  - list comprehension
  - while loop
- standard Python entry point pattern (if __name__ == "__main__":)

OBS:
  This is your file to practice and customize.
  Find the TODO comments, and as you complete each task, remove the TODO note.

"""


# === DECLARE IMPORTS (BRING IN FREE CODE) ===

import logging
from pathlib import Path
import time
from typing import Final

# External (must be listed in pyproject.toml)
from datafun_toolkit.logger import get_logger, log_header

# === CONFIGURE LOGGER ONCE PER MODULE (FILE) ===

LOG: logging.Logger = get_logger("P02", level="DEBUG")

# === DECLARE SOME GLOBAL VARIABLES ===

# Find the current working directory (cwd) using pathlib.
# Use UPPER_SNAKE_CASE for constant names.
# Use `type hints` with Final for constants.

ROOT_DIR: Final[Path] = Path.cwd()

REGIONS: Final[list[str]] = [
    "North America",
    "South America",
    "Europe",
    "Asia",
    "Africa",
    "Oceania",
    "Middle East",
]

# === HERE IS A HELPER FUNCTION THAT WRITES A FILE AND LOGS IT ===


def write_text_file(path: Path, content: str) -> None:
    """Write content to a text file (overwriting if it exists).

    Arguments:
        path: Full path to the file to create/write.
        content: Text content to write.

    Returns:
        None
    """
    path.write_text(content, encoding="utf-8")
    LOG.info(f"WROTE file: {path.name}")


# === DECLARE REPETITION FUNCTION 1: FOR EACH IN NUMERIC RANGE ===


def create_files_from_numeric_range() -> None:
    """Create one file per year for a given year range.

    Arguments: None
    Returns:  None
    """
    LOG.info("Start Function 1: create_files_from_numeric_range()")

    starting_year: int = 2023
    ending_year: int = 2026

    LOG.info(f"Starting year: {starting_year}")
    LOG.info(f"Ending year: {ending_year}")

    for year in range(starting_year, ending_year + 1):
        filename: str = f"case_{year}.txt"
        path: Path = ROOT_DIR / filename
        content: str = f"Here is my report for the year: {year}\n"
        write_text_file(path, content)


# === DECLARE REPETITION FUNCTION 2: FOR ITEM IN LIST ===


def create_files_from_list() -> None:
    """Create one file per region.

    Arguments: None
    Returns:  None
    """
    LOG.info("START FUNCTION 2: create_files_from_list()")
    LOG.info(f"Region list ={REGIONS}")

    for region in REGIONS:
        filename: str = f"case_{region.replace(' ', '_')}.txt"
        path: Path = ROOT_DIR / filename
        content: str = f"Here is my report for the region: {region}\n"

    write_text_file(path, content)


# === DECLARE REPETITION FUNCTION 3: USING LIST COMPREHENSION ===


def create_files_using_list_comprehension() -> None:
    """Create files by transforming names using list comprehension.

    Arguments: None

    Returns: None
    """
    # Log the start of this function
    LOG.info("START FUNCTION 3: create_files_using_list_comprehension()")
    LOG.info("WHY: Use list comprehension to TRANSFORM a list into a new list.")
    LOG.info("WHY: They are super compact list transformations.")
    LOG.info("Read it as <do this logic> FOR each <item> IN <list>.")

    region_tag: list[str] = [region.lower().replace(" ", "_") for region in REGIONS]
    LOG.info(f"Region tag list ={region_tag}")

    for tag in region_tag:
        filename: str = f"case_{tag}.txt"
        path: Path = ROOT_DIR / filename
        content: str = f"Here is my special data about the region tag: '{tag}'\n"
        write_text_file(path, content)


# === DECLARE REPETITION FUNCTION 4: WHILE LOOP (PERIODIC) ===


def create_files_periodically() -> None:
    """Create a small number of files with a delay between each creation.

    Arguments: None
    Returns:   None
    """
    # Log the start of this function
    LOG.info("START FUNCTION 4: create_files_periodically()")
    LOG.info("WHY: Use while loop for REPETITIVE tasks with a WAIT or DELAY.")

    # Define wait_seconds: Seconds to wait between file writes.
    wait_seconds: int = 1
    # Define count: How many files to create.
    count: int = 13  # 5 >= count < 25

    # Log the wait_seconds
    LOG.info(f"Waiting seconds between files: {wait_seconds}")
    # Log the count
    LOG.info(f"Number of files to create: {count}")

    # Define a counter variable
    i: int = 1

    # While the counter is less than or equal to the count
    while i <= count:
        # Define a filename that starts with my name and uses the counter
        # Use 02d formatting for leading zeros and two digits
        filename: str = f"case_{i:02d}.txt"
        # Define the path for my new file
        path: Path = ROOT_DIR / filename
        # Define some content to put in the new file

        content: str = (
            "If we accidentally make an infinite loop, this will go forever... We're on file count: {i}\n"
            "Periodic file creation {automated}\n"
            f"File number: {i}\n"
            f"Delay between files: {wait_seconds} seconds.\n"
        )

        write_text_file(path, content)

        # Log the wait time
        LOG.info(f"Waiting {wait_seconds} seconds...")

        # Call the time.sleep() function to wait for the given number of wait_seconds
        time.sleep(wait_seconds)
        # IMPORTANT: Remember to increment the counter variable to avoid an infinite loop!
        # Set the value of i to itself plus one (this is the same as i = i + 1)
        i += 1


# === DEFINE THE MAIN FUNCTION ===


def main() -> None:
    """Entry point for the script.

    Creates files as visible artifacts which will be committed to Git.

    Arguments: None
    Returns:   None
    """
    log_header(LOG, "Automation: Creating Files with Repetition Patterns")

    LOG.info("START main()")

    # Task 1. Create one file for each number in a range
    create_files_from_numeric_range()

    # Task 2. Create one file for each item in a list
    create_files_from_list()

    # Task 3. Use a list comprehension to make a list from a list - then create a file for each
    create_files_using_list_comprehension()

    # Task 4. Create files periodically
    create_files_periodically()

    # To Delete these text files while working, run this command in terminal:
    # rm *.txt

    LOG.info("END main()")


# === CONDITIONAL EXECUTION GUARD ===

if __name__ == "__main__":
    main()
