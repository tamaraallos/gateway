# search for specific string from log files and return line number 
def search_log(log_file_path, search_string):
    try:
        line_count = 1 # initalise the line count
        with open(log_file_path, 'r') as log_file: # file opened in read mode
            for line in log_file:
                if search_string in line:
                    print(f"Found '{search_string}' on line {line_count}: {line.strip()}")
                line_count += 1 # increment line count
    except Exception as e: # throw error 
        print(f"An error has occured: {e}")

## will be making improvements to above