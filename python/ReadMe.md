# 1. python directory

- [1. python directory](#1-python-directory)
  - [1.1. Requirements](#11-requirements)
  - [1.2. Package files](#12-package-files)
  - [1.3. 1.1 OwlToPythonClass](#13-11-owltopythonclass)
    - [1.3.1. Command](#131-command)
  - [1.4. Tests](#14-tests)
    - [1.4.1. Command](#141-command)

This folder contains some python packages and test made with pytest
The commands should be launch from this current directory (`python`)

## 1.1. Requirements
The requirements are written in `requirements.txt`.
It is possible to install with this command.  
```
pip install -r requirements.txt
```

## 1.2. Package files
In python, you have to insert an empty `__init__.py` file so it recognize the directory as a package or a module.


## 1.3. 1.1 OwlToPythonClass

This package extract data from the ontology on `resource` and convert it into object or generate list of triples.  
You can choose to print or not the info.  

### 1.3.1. Command
```
PYTHONPATH=. python3 OwlToPythonClass/extractor.py
```

## 1.4. Tests
In the `test` folder, we insert all the test files. We used the package pytest to launch them.

### 1.4.1. Command
This command launch from the `python` directory as always launch all the tests of the folder.  This
```
pytest
```

