from yaml import load, dump
from yaml import Loader, Dumper
from sys import argv, exit
from os.path import isfile, dirname, join
from enum import Enum
from contextlib import contextmanager

TEMPLATE_PATH = join(dirname(__file__), "template.yaml")

def detect_app_type(root: str):
    def check_file(filename):
        return isfile(join(root, filename))

    if check_file("Makefile"):
        return "c"
    if check_file("app/pom.xml"):
        return "java"
    if check_file("package.json"):
        return "javascript"
    if check_file("requirements.txt"):
        return "python"
    if check_file("app/main.bf"):
        return "befunge"
    raise ValueError("Unsupported language, please read the documentation for more information.")

def detect_dockerfile(root: str) -> bool:
    return isfile(join(root, "Dockerfile"))


@contextmanager
def open_with_error(file: str, mode="r", *args, **kwargs):
    try:
        f = open(file, mode, *args, **kwargs)
        yield f
    except IOError as e:
        raise RuntimeError(f"Failed to open file {file}:\n{e}") from e
    finally:
        f.close()

def add_to_template(file: str, output_file: str, image: str) -> None:
    with open_with_error(TEMPLATE_PATH, "r") as f:
        template = load(f, Loader=Loader)
    with open_with_error(file, "r") as f:
        user_yaml = load(f, Loader=Loader)
    if "resources" in user_yaml["deployment"]:
        template["spec"]["containers"][0]["resources"] = user_yaml["deployment"]["resources"]

    if "replicas" in user_yaml["deployment"]:
        template["spec"]["replicas"] = user_yaml["deployment"]["replicas"]
    else:
        template["spec"]["replicas"] = 1
    template["spec"]["containers"][0]["image"] = image

    with open_with_error(output_file, "w") as f:
        f.write(dump(template, Dumper=Dumper))

def main():
    if len(argv) != 3:
        print(f"USAGE: {argv[0]} app_folder output_file")
        exit(84)
    _, app_folder, output_file, *_ =  argv
    if detect_dockerfile(app_folder):
        raise NotImplementedError("Don't know what to do with user docker files")

    app_type = detect_app_type(app_folder)
    docker_image = f"whanos-{app_type}-standalone"

    yaml_location = join(app_folder, "whanos.yaml")
    if isfile(yaml_location):
        add_to_template(yaml_location, output_file, docker_image)


if __name__ == '__main__':
    main()
