import os

# this file creates empty blueprints with empty files inside
def create_blueprint(blueprint_name, path):
    
    """This funtion is used for automatically create blueprints:
    bp_name/
    ├── __init__.py
    ├── routes.py
    ├── forms.py
    └── templates/
        └── bp_name/
            ├── edit.html
            ├── detail.html
            └── view.html

    Args to be passed: blueprint_name, and full path

    """

    blueprint_dir = os.path.join(path, blueprint_name)
    os.makedirs(blueprint_dir, exist_ok=True)  # Create root directory if it doesn't exist

    # Create subdirectories
    subdirs = [ "templates"]
    for subdir in subdirs:
        os.makedirs(os.path.join(blueprint_dir, subdir), exist_ok=True)

    # Create template subdirectory inside templates
    template_subsubdir = os.path.join(blueprint_dir, "templates", blueprint_name)
    os.makedirs(template_subsubdir, exist_ok=True)

    # Create empty files (optional)
    files = [
        os.path.join(blueprint_dir, "__init__.py"),
        os.path.join(blueprint_dir, "forms.py"),
        os.path.join(blueprint_dir, "routes.py"),
        os.path.join(template_subsubdir, "edit.html"),
        os.path.join(template_subsubdir, "view.html"),
        os.path.join(template_subsubdir, "detail.html"),
    ]
    for filename in files:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("")  # Empty file

    print(f"Blueprint folder structure '{blueprint_name}' created successfully!")

    


if __name__ == "__main__":
  blueprint_name = input("Enter blueprint name (lowercase_with_underscores): ")
  blueprint_path = input("Enter path to create the blueprint (e.g., blueprints): ")
  create_blueprint(blueprint_name, blueprint_path)
  
