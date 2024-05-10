import ast
from service_methods import service_methods
import os

def extract_classes_and_methods(file_path):
    classes_and_methods = {}

    with open(file_path, "r") as file:
        tree = ast.parse(file.read())

    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            class_name = node.name
            methods = [f.name for f in node.body if isinstance(f, ast.FunctionDef)]
            classes_and_methods[class_name] = methods

    return classes_and_methods


def load_my_methods(my_methods, file_path):  
    classes_and_methods = extract_classes_and_methods(file_path) 

    for class_name, methods in classes_and_methods.items():
        
        print("Class:", class_name)
        print("Present Methods:", methods)
        print()
        missing_methods = []
        for k,v in my_methods.items():
            
            if k not in methods:
             
                missing_methods.append(v)
                
    return (class_name, missing_methods)

def add_service_content(file_path, my_methods):
    """
        Creates class for communicating with db 
    """
    
    class_and_method = load_my_methods(my_methods, file_path)
    service_name = class_and_method[0].lower()
    methods = class_and_method[1]
    content = f"""
"""
    for i in methods:
        service_name = service_name
        content += i
    
    return content


# add_service_content(file_path, my_methods)


def create_service(path, my_methods):
  
    service_content = add_service_content(path, my_methods)
    with open(path, 'a', encoding='utf-8') as f:
        f.write(service_content)

    



if __name__ == "__main__":
  service_name   = input("Enter Service name (lowercase_with_underscores): ")
  my_methods     = service_methods(service_name)
  service_path   = input("Enter full path of service file you want to update (example flaskr/services/serviceTest.py): ")
  create_service(service_path, my_methods)
  print(f"Service {service_name.title()}Service successfully updated")