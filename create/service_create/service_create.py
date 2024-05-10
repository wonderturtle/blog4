import os
from service_methods import service_methods


def load_my_methods(service_name): 
    my_methods = service_methods(service_name)
    methods = [] 
    for k,v in my_methods.items():
        methods.append(v)

                
    return methods

def add_service_content(service_name,  path=""):
    """
        Creates class for communicating with db 
    """
    methods = load_my_methods(service_name)
    content = f"""
from flaskr.models.{service_name} import {service_name.title()}
from flaskr import db
import flaskr.tw_globals as tw_globals
from sqlalchemy.exc import SQLAlchemyError

class {service_name.title()}Service():
 
  """
    for i in methods:
        content += i
    return content

def create_service(service_name, path):
  
    service_content = add_service_content(service_name, path)
    with open(os.path.join(path, f"{service_name}Service.py"), 'w', encoding='utf-8') as f:
        f.write(service_content)

    print(f"Service {service_name} successfully created")


if __name__ == "__main__":
  service_name   = input("Enter Service name (lowercase_with_underscores): ")
  service_path   = input("Enter path of the service folder to create the new service: ")

  create_service(service_name, service_path)