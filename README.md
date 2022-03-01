# 0x00. AirBnB clone - The console

 ![HNBN](https://github.com/zye7ert/AirBnB_clone/blob/master/picture/HBNB-HolbertonAirbnb.png)

### Descripción
***
__Airbnb__ is an online platform that connects people who have a home to offer, with people who need a place to stay temporarily.

This is the first phase of an eight phase project, where we create The AirBnB Clone and create a shell to manage the AirBnB objects.

This Phase of the project focuses on everything about Python`Import`,` Exceptions`, `Class`, `Private attribute`, `Getter / Setter`, `Class method`, `Static method`, `Inheritance`, `Unittest`, `Read / Write file`, `args `and` kwargs`, `Serialization` / `Deserialization` and `JSON`.

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

#### Folders:
| Folders | Description |
| --- | --- |
| [`models/`]() | Folder containing the Airbnb base structure models. |
| [`models/engine/`]() | Folder containing storage engine abstracted from the project: File storage. |
| [`tests/`]() | Folder that contains all unittests to validate all our classes and storage engine. |
| [`tests/test_models`]() | Folder containing all unit test files in the `models` folder. |
| [`tests/test_models/test_engine`]() | Folder containing all unit test files in the `engine` subfolder. |

### Console
***
#### Description of the command interpreter 

the console contains the entry point of the command interpreter.

### Installation
***
1. Clone this repository:
`https://github.com/zye7ert/AirBnB_clone.git`
2. Access AirBnb directory:
`cd AirBnB_clone`
3. Run hbnb(interactively)
```bash
root@c698ec171c6e:/home/AirBnB_clone# ./console
```
4. When this command is run the following prompt should appear:
```bash
(hbnb)
```
5. This prompt designates you are in the "HBnB" console. There are a variety of commands available within the console program.

| Command | Description |
| --- | --- |
| `create` | Creates a new instance of `BaseModel`, saves it (to the JSON file) and prints the `id`. |
| `show` | Prints the string representation of an instance based on the class name and `id`. |
| `destroy` | Deletes an instance based on the class name and `id` (save the change into the JSON file). |
| `all` | Prints all string representation of all instances based or not on the class name. |
| `update` | Updates an instance based on the class name and `id` by adding or updating attribute (save the change into the JSON file). |
| `quit` and `EOF`| To exit the program. |
| `help` | Shows the commands that can be used in the console. |