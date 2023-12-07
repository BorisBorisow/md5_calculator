import hashlib
import os


def calculate_md5(file_path):
    """
    Calculate the MD5 sum of a file.
    """
    md5_hash = hashlib.md5()
    with open(file_path, "rb") as f:
        # Read the file in chunks of 4096 bytes
        for chunk in iter(lambda: f.read(4096), b""):
            md5_hash.update(chunk)
    return md5_hash.hexdigest()


def calculate_md5_for_directory(directory_path):
    """
    Calculate MD5 sums for all files in a directory.
    """
    md5_sums = {}
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            md5_sum = calculate_md5(file_path)
            md5_sums[file_path] = md5_sum
    return md5_sums


if __name__ == "__main__":
    """
        Give the file directory.
    """
    media_directory = r"directory_path/media"
    md5_sums = calculate_md5_for_directory(media_directory)

    # Specify the path to the output file
    output_file_path = "md5_sums.txt"

    # Write only the file name and MD5 sum to the output file using 'utf-8' encoding
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        for file_path, md5_sum in md5_sums.items():
            file_name = os.path.basename(file_path)
            output_file.write(f"{file_name}:\n {md5_sum}\n \n")

    print(f"MD5 sums written to {output_file_path}")
