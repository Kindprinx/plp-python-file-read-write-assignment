"""
File Read & Write Challenge with Error Handling
- Reads content from an input file
- Modifies the content
- Writes modified content to a new file
- Implements error handling for file operations
"""

def process_file():
    # Ask user for input filename
    input_filename = input("Enter the name of the file to read: ")
    
    try:
        # Try to open and read the input file
        with open(input_filename, 'r') as input_file:
            content = input_file.read()
            print(f"Successfully read {len(content)} characters from {input_filename}")
            
            # Ask for output filename
            output_filename = input("Enter the name of the file to write to: ")
            
            # Modify the content (example: convert to uppercase)
            modified_content = content.upper()
            
            try:
                # Try to write to the output file
                with open(output_filename, 'w') as output_file:
                    output_file.write(modified_content)
                    print(f"Successfully wrote modified content to {output_filename}")
            
            except IOError as e:
                print(f"Error writing to file {output_filename}: {e}")
                
            except Exception as e:
                print(f"Unexpected error while writing: {e}")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
        
    except PermissionError:
        print(f"Error: You don't have permission to read '{input_filename}'.")
        
    except IOError as e:
        print(f"IO Error reading file {input_filename}: {e}")
        
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    print("File Read & Write Program with Error Handling")
    print("--------------------------------------------")
    process_file()
