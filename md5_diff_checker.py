import hashlib
import os

def calculate_md5(file_path):
    md5_hash = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            md5_hash.update(chunk)
    return md5_hash.hexdigest()

def find_different_md5_sums(original_directory, new_directory):
    original_md5_sums = {calculate_md5(file): file for root, _, files in os.walk(original_directory) for file in [os.path.join(root, f) for f in files]}
    new_md5_sums = {calculate_md5(file): file for root, _, files in os.walk(new_directory) for file in [os.path.join(root, f) for f in files]}

    different_md5_sums = set(new_md5_sums.keys()) - set(original_md5_sums.keys())

    result = {}
    for md5_sum in different_md5_sums:
        result[new_md5_sums[md5_sum]] = md5_sum

    return result

if __name__ == "__main__":
    """
        Give a directory paths
    """
    original_directory = r"first_path_directory"
    new_directory = r"second_path_directory"

    different_md5_sums = find_different_md5_sums(original_directory, new_directory)

    output_file_path = "different_md5_sums.txt"

    with open(output_file_path, "w", encoding="utf-8") as output_file:
        for file_path, md5_sum in different_md5_sums.items():
            file_name = os.path.basename(file_path)
            output_file.write(f"{file_name}: {md5_sum}\n")

    print(f"Different MD5 sums written to {output_file_path}")
