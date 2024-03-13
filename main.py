from form import (FormBuilder, InvalidFilePathError,InvalidFileFormatError,SupportedFileTypeYAML,SupportedFileTypeJSON,SupportedFileTypeYML)

def main():
    form_builder = FormBuilder()
    #Prompt user for file path and check if file path exists
    path: str
    try:
        path = form_builder.get_file_path()
    except InvalidFilePathError as e:
        print(e)
        return
    
    try:
        file_type = form_builder.get_file_type(path)
    except InvalidFileFormatError as e:
        print(e)
        return
    
    if file_type == SupportedFileTypeJSON:
        data = form_builder.read_json(path=path)
        #Read json
    elif file_type == SupportedFileTypeYAML or file_type == SupportedFileTypeYML:
        data = form_builder.read_yaml_file(path=path)
    
    #Validate input from questions uploaded

    questions_validation_error = form_builder.validate(data=data)

    if len(questions_validation_error) != 0:
        print(questions_validation_error)
        return
    
    #If there is no error then let's build the form
    answers = form_builder.build_form(data=data)

    #Print Results
    form_builder.print_questions_and_answers(data,answers)


if __name__ == "__main__":
    main()