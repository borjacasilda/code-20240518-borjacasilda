import os

def save_output_dir(root):
    """
    Creates a 'save_output' directory within 
    the specified root directory if it does 
    not already exist. 
    

    Parameters:
    - root (str): The root directory where 
    the 'save_output' directory will be created. 
    By default in definitions.py I have specified
    the GitHub local repository as PATH.

    Returns:
    - str or None: The path to the 'save_output' directory 
    if creation is successful or it already exists, 
    otherwise None. Defined in main.py as comment.
    """
    
    # Define the full path for the 'save_output' directory
    save_output_dir = os.path.join(root, 'save_output')
    # Check if the directory already exists
    if not os.path.exists(save_output_dir):
        try:
            # Attempt to create the directory
            os.makedirs(save_output_dir)
            # Return the directory path if creation is successful
            return save_output_dir
        # Handle any errors encountered during directory creation
        except OSError as e:
            # Print an error message
            print(f'Check root: {root}')
            # Return None if directory creation fails
            return None
    else:
        # Inform that the directory already exists
        print(f'save_output_dir: {save_output_dir}')
        # Return the existing directory path
        return save_output_dir
    