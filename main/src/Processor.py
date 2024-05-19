import json
import re

import MetadataEncoder
from Lane import Lane
from Metadata import Metadata
from Validator import validate_output_file_path, validate_input_file_path, empty_input_file


def object_keys_from_input_file(input_file_path: str):
    keys, exit_code = [], 0
    try:
        with open(input_file_path) as input_file:
            keys = json.load(input_file)
            if len(keys) == 0:
                print(f"The input file [{input_file_path}] has empty object keys")
                # System exit code can be 0 if empty object keys are allowed
                exit_code = 4
    except ValueError as e:
        print(f"The input file [{input_file_path}] is corrupt: [{e}]")
        exit_code = 1
    finally:
        return keys, exit_code


def is_object_key_valid(key: str):
    key_fragment = key.split("/")
    # Regex implemented based on raw understanding but can be modified or extended based on business requirements
    if ((len(key_fragment) == 3
         and re.match("^([XY]\\d{3}-T[cnp]\\d{1,2})$", key_fragment[0])
         and key_fragment[1] == "wgs"
         and re.match(
                "^((H[A-Z7]{8})_DNA_([XY]\\d{3}-T[cnp]\\d{1,2})_([A-Z]{8})-([A-Z]{8})_L[0-9]{3}_R1_001.fastq.gz)$",
                key_fragment[2]))
            and key_fragment[2].split("_")[2] == key_fragment[0]):
        return True
    print(f"The object key [{key}] is invalid")
    return False


def extract_metadata_from_object_key(key: str, object_keys_metadata: list, skip_count: int, dupe_count: int):
    if not is_object_key_valid(key):
        skip_count += 1
        return object_keys_metadata, skip_count, dupe_count
    lane = Lane(key)
    for idx in range(len(object_keys_metadata)):
        metadata = object_keys_metadata[idx]
        if metadata.sample_id == key.split("/")[0]:
            for metadata_lane in metadata.lanes:
                if metadata_lane.path == key:
                    dupe_count += 1
                    print(f"Duplicate object key [{key}] is found")
                    return object_keys_metadata, skip_count, dupe_count
            metadata.lanes.append(lane)
            object_keys_metadata[idx] = metadata
            return object_keys_metadata, skip_count, dupe_count
    object_keys_metadata.append(Metadata(key, [lane]))
    return object_keys_metadata, skip_count, dupe_count


def determine_system_exit_status(object_key_count: int, skip_count: int, dupe_count: int):
    print(f"Total object keys found in the input file - [{object_key_count}]")
    print(f"Total invalid object keys found in the input file - [{skip_count}]")
    print(f"Total duplicate object keys found in the input file - [{dupe_count}]")
    if skip_count == 0:
        return 0
    if skip_count == object_key_count:
        return 1
    return 3


def update_output_json_attribute_key(metadata: list):
    return (json.dumps(metadata, cls=MetadataEncoder.MetadataEncoder, ensure_ascii=False, indent=2)
            .replace("sample_id", "sample-id")
            .replace("case_id", "case-id")
            .replace("sample_label", "sample-label")
            .replace("data_type", "data-type")
            .replace("marker_forward", "marker-forward")
            .replace("marker_reverse", "marker-reverse"))


def write_metadata_to_file(metadata: list, output_file_path: str, exit_code: int):
    try:
        with open(output_file_path, "w", encoding='utf-8') as output_file:
            output_file.write(update_output_json_attribute_key(metadata))
    except ValueError as e:
        print(f"System encountered an error [{e}] while writing metadata to the output file [{output_file_path}]")
        exit_code = 1
    finally:
        return exit_code


def __execute__(input_file_path: str, output_file_path: str):
    if not validate_input_file_path(input_file_path) or not validate_output_file_path(output_file_path):
        return 1
    if empty_input_file(input_file_path):
        return 4
    object_keys, exit_status_code = object_keys_from_input_file(input_file_path)
    if exit_status_code != 0:
        return exit_status_code
    metadata_coll, skip_counter, dupe_counter = [], 0, 0
    for object_key in object_keys:
        metadata_coll, skip_counter, dupe_counter = extract_metadata_from_object_key(object_key, metadata_coll,
                                                                                     skip_counter, dupe_counter)
    exit_status_code = determine_system_exit_status(len(object_keys), skip_counter, dupe_counter)
    if exit_status_code == 1:
        return exit_status_code
    write_metadata_to_file(metadata_coll, output_file_path, exit_status_code)
    return exit_status_code
