# Value Mapper

A Python script to map values in a CSV column using a reference dictionary.

## Features
- Maps values based on substring matches
- Handles default cases for unmatched entries
- Supports case-sensitive/insensitive matching
- Accepts JSON reference dictionaries

## Usage

1. Prepare a JSON reference dictionary:
   ```json
   {
       "Key1": ["substring1", "substring2"],
       "Key2": ["substring3"]
   }
Run the script:

bash
python value_mapper.py
Provide inputs when prompted:

Path to JSON reference dictionary

Source column name

Target key column name

Target substring column name

Default substring/value (optional)

Results are saved to output.csv

Example
For hospital-region mapping:

Reference JSON: hospital_ref.json

Source column: Page path and screen class

Key target: Region

Substring target: Hospital

Default: corporate


## Note
origianal ideat for the code is uploaded ,was specific for already dicts saved in clients system
