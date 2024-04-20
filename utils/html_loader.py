def read_html_file(file_path):
    with open(file_path, 'r') as file:
        html_code = file.read()
    return html_code
