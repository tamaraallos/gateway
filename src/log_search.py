import json

# search for specific string from log files and return line number (searches enter email)
def search_log(log_file_path, search_string):
    try:
        search_string = search_string.lower()
        line_count = 1 # initalise the line count
        found = False # if search_string exists within the file
        with open(log_file_path, 'r') as log_file: # file opened in read mode
            # initalise variables used for the for loop
            inside_obj = False
            current_obj = ""

            for line in log_file:
                if search_string in line.lower():
                    found = True

                if '{' in line and not inside_obj:
                    inside_obj = True
                    current_obj = line  # gets the { line

                elif inside_obj:
                    current_obj += line # gets everything between the { } object (so the email)

                    if '}' in line:
                        inside_obj = False 
                        if search_string in current_obj.lower():
                            print(current_obj.strip())

                line_count += 1

            if not found:
                print(f"The '{search_string}' was not found within the email log file.")

    except Exception as e: # throw error 
        print(f"An error has occured: {e}")


# searches an email based on a specific header (from, to, subject, date etc), and passed in value
def search_by_field(log_file_path, search_action, search_value):
    try:
        search_value = search_value.lower()
        with open(log_file_path, 'r') as log_file:
            inside_obj = False # if search_string exists within the obj
            current_obj = ""

            for line in log_file:
                if '{' in line and not inside_obj:
                    inside_obj = True
                    current_obj = line  # start to get the JSON object ({)
                elif inside_obj:
                    current_obj += line  # gets the rest of the JSON object
                    
                    if '}' in line:
                        inside_obj = False
                        # parse the collected JSON object
                        try:
                            email_obj = json.loads(current_obj)
                            field_value = email_obj.get(search_action, "").lower() # retrievers passed in header (search_action)
                            
                            if search_value in field_value:
                                print(json.dumps(email_obj, indent=4))
                                print()
                        except json.JSONDecodeError:
                            print(f"The '{search_value}' was not found within the email log file searching by {search_action}.")
                        
                        current_obj = ""  # reset current_obj for the next JSON object
                
    except Exception as e:
        print(f"An error has occurred: {e}")