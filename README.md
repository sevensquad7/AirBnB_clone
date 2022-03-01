# 0x00. AirBnB clone - The console

 ![HNBN](https://github.com/zye7ert/AirBnB_clone/blob/master/picture/HBNB-HolbertonAirbnb.png)

### Descripción
***
__Airbnb__ is an online platform that connects people who have a home to offer, with people who need a place to stay temporarily.

This is the first phase of an eight phase project, where we create The AirBnB Clone and create a shell to manage the AirBnB objects.

This Phase of the project focuses on everything about Python:
`Import`,` Exceptions`, `Class`, `Private attribute`, `Getter / Setter`, `Class method`, `Static method`, `Inheritance`, `Unittest`, `Read / Write file`, `args `and` kwargs`, `Serialization` / `Deserialization` and `JSON`.

Phases of the AirBnB clone project:
1. **The console**

### Requirements
***
#### Python Scripts

* Allowed editors: `vi`, `vim`, `emacs`.
* Files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5).
* Files must be executable.
* The length of your files will be tested using `wc`.

#### Python Unit Tests

* All your test files should be inside a folder `tests`.
* You have to use the unittest module.
* All your test files should be python files (extension: `.py`).
* All your test files and folders should start by `test_`.
* All your tests should be executed by using this command: `python3 -m unittest discover tests`.

### Style
***
* Code should use the PEP 8 style (version 2.7.*).

### Repository Projects
***
#### Tasks:
| Files | Description |
| --- | --- |
| [`models/base_model.py`]() | Defines all common attributes/methods for other classes. |
| [`models/engine/file_storage.py`]() | Serializes instances to a JSON file and deserializes JSON file to instances. |
| [`console.py`]() | Contains the entry point of the command interpreter. |
| [`models/user.py`]() | Defines subclass User. |
| [`models/state.py`]() | Defines subclass State. |
| [`models/city.py`]() | Defines subclass City. |
| [`models/amenity.py`]() | Defines subclass Amenity |
| [`models/place.py`]() | Place file that contains detailed information about the place to be rented. |
| [`models/review.py`]() | Defines subclass Review. |
| [`tests/test_console.py`]() | unittests for console. |
| [`tests/test_models/test_base_model.py`]() | unittests for base_model. |
| [`tests/test_models/test_user.py`]() | Unittests for user. |
| [`tests/test_models/test_state.py`]() | Unittests for state. |
| [`tests/test_models/test_city.py`]() | Unittests for city. |
| [`tests/test_models/test_amenity.py`]() | Unittests for amenity. |
| [`tests/test_models/test_place.py`]() | Unittests for place. |
| [`tests/test_models/test_review.py`]() | Unittests for review. |
| [`tests/test_models/test_engine/test_file_storage.py`]() | Unittests for file_storage. |