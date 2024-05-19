Filetree sample data is a batch application.

It will take a JSON file with a collection of object keys as input and
create an output file consisting of metadata for each object key.

The application requires at least two _CLI_ arguments below from the user to start the application successfully.

- **input_file_path**: The absolute path for the input file, which extends with .json
- **output_file_path**: The absolute path for the output file which extends with .json

**How to run the batch application:**

- `(.venv) -> python3 Application.py <input_file_path> <output_file_path>
  `

The batch application will exit with the system exit code upon successful or failed completion, as shown below.

- _0_: The batch application successfully processed an input file and created metadata in an output file in a desired
  location
- _1_: The batch application failed to process an input file and was not able to create any metadata
- _2_: The batch application could not be started as it expects at least two CLI arguments from the user
- _3_: The batch application successfully processed an input file; however, the metadata created in the output file is
  partial.
- _4_: The batch application received a no-content input file




