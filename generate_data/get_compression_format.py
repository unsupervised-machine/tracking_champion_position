import magic


def get_compression_format(file_path):
    _, file_extension = os.path.splitext(file_path)
    return file_extension.lower()


def get_compression_format_magic(file_path):
    # Create a magic.Magic object
    mime = magic.Magic()

    # Use the object to get the file type
    return mime.from_file(file_path)

file_path = 'getting_website_data/model_files/Aatrox/Aatrox/Aatrox.glb.gz'

compression_format = get_compression_format(file_path)
print(f"The compression format of the file is: {compression_format}")


compression_format_m = get_compression_format_magic(file_path)
print(f"The compression format of the file is: {compression_format_m}")