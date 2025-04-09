# plp-python-file-read-write-assignment
# File Read & Write Program

## Overview
This Python program demonstrates file operations with comprehensive error handling. It reads content from an input file, modifies it, and writes the modified content to a new output file.

## Features
- **File Reading**: Reads content from a user-specified file
- **Content Modification**: Converts text to uppercase (can be customized)
- **File Writing**: Writes modified content to a new file
- **Robust Error Handling**: Gracefully handles file not found, permission errors, and other exceptions

## Requirements
- Python 3.x

## Usage
1. Run the program:
   ```
   python file_processor.py
   ```

2. Follow the prompts:
   - Enter the name of the file to read
   - Enter the name of the file to write to

3. The program will:
   - Read the content from the input file
   - Convert the content to uppercase
   - Write the modified content to the output file

## Error Handling
The program handles the following errors:
- **FileNotFoundError**: When the specified input file doesn't exist
- **PermissionError**: When you don't have permission to read the file
- **IOError**: For general input/output errors
- **Other Exceptions**: Generic handling for unexpected issues

## Example

```
File Read & Write Program with Error Handling
--------------------------------------------
Enter the name of the file to read: sample.txt
Successfully read 156 characters from sample.txt
Enter the name of the file to write to: output.txt
Successfully wrote modified content to output.txt
```

## Customization
You can easily modify the program to perform different transformations on the text. Change the line:
```python
modified_content = content.upper()
```
to apply any other transformation you need.

## License
Open source - feel free to modify and use as needed.
