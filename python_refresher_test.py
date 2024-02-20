import math
import datetime
import os


def test_import_example(capsys):
    exec(open("import_example.py").read())
    captured = capsys.readouterr()
    assert captured.out.strip() == str(math.pi)


def test_control_flow(capsys):
    exec(open("control_flow.py").read())
    captured = capsys.readouterr()
    assert captured.out.strip() == "10 or less"


def test_variables_data_types(capsys):
    exec(open("variables_data_types.py").read())
    captured = capsys.readouterr()
    assert "25" in captured.out and "John" in captured.out


def test_functions_methods(capsys):
    exec(open("functions_methods.py").read())
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, Alice!"


def test_lists_dictionaries(capsys):
    exec(open("lists_dictionaries.py").read())
    captured = capsys.readouterr()
    assert captured.out.strip() == "red\nAlice"


def test_modules_packages(capsys):
    exec(open("modules_packages.py").read())
    captured = capsys.readouterr()
    assert captured.out.strip() == str(datetime.date.today())


def test_classes_objects(capsys):
    exec(open("classes_objects.py").read())
    captured = capsys.readouterr()
    assert captured.out.strip() == "Beep!"


def test_file_handling(capsys):
    exec(open("file_handling.py").read())
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, World!"
    os.remove("hello.txt")  # Clean up the file after the test


def test_error_handling(capsys):
    exec(open("error_handling.py").read())
    captured = capsys.readouterr()
    assert captured.out.strip() == "File not found."


def test_string_formatting(capsys):
    exec(open("string_formatting.py").read())
    captured = capsys.readouterr()
    assert captured.out.strip() == "There are 5 apples."
