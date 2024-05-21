import os

def save_output_dir(root):
    save_output_dir = os.path.join(root, 'save_output')
    if not os.path.exists(save_output_dir):
        try:
            os.makedirs(save_output_dir)
            return save_output_dir
        except OSError as e:
            print(f'Check root: {root}')
            return None
        else:
            print(f'save_output_dir: {save_output_dir}')
            return save_output_dir
