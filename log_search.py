import math
# search for specific string from log files and return line number 
def search_log(log_file_path, search_string):
    try:
        search_string = search_string.lower()
        line_count = 1 # initalise the line count
        found = False # if search_string exists within the file
        with open(log_file_path, 'r') as log_file: # file opened in read mode
            # initalise variables used for the for loop
            inside_obj = False
            current_obj = ""
            object_count = 0

            for line in log_file:
                if search_string in line.lower():
                    print(f"Found '{search_string}' on line {line_count}: {line.strip()}")
                    found = True

                if '{' in line and not inside_obj:
                    inside_obj = True
                    object_count = line_count
                    current_obj = line  # gets the { line

                elif inside_obj:
                    current_obj += line # gets everything between the { } object (so the email)

                    if '}' in line:
                        inside_obj = False 
                        if search_string in current_obj.lower():
                            object_count = math.ceil(((object_count - 1) / 7) + 1) # calcs what number the email object is 
                            print(f"Found email at object: {object_count}")
                            print(current_obj.strip())

                line_count += 1

            if not found:
                print(f"The '{search_string}' was not found within the email log file.")

    except Exception as e: # throw error 
        print(f"An error has occured: {e}")

