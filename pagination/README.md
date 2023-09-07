# Pagination

### Resources

**Read or Watch**:

- REST API Design: Pagination
- HATEOAS

### Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

- How to paginate a dataset with simple page and page_size parameters
- How to paginate a dataset with hypermedia metadata
- How to paginate in a deletion-resilient manner

### Requirements

- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` style (version 2.5.*)
- The length of your files will be tested using `wc`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your functions should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- All your functions and coroutines must be type-annotated.

### Setup: Popular_Baby_Names.csv

Use this data file for your project.

---

### Tasks

#### 0. Simple helper function

**File**: `0-simple_helper_function.py`

Write a function named `index_range` that takes two integer arguments `page` and `page_size`.

The function should return a tuple of size two containing a start index and an end index corresponding to the range of indexes to return in a list for those particular pagination parameters. Page numbers are 1-indexed, i.e. the first page is page 1.

#### 1. Simple pagination

**File**: `1-simple_pagination.py`

Copy `index_range` from the previous task and the given class into your code.

Implement a method named `get_page` that takes two integer arguments `page` with default value 1 and `page_size` with default value 10.

#### 2. Hypermedia pagination

**File**: `2-hypermedia_pagination.py`

Replicate code from the previous task.

Implement a `get_hyper` method that takes the same arguments (and defaults) as `get_page` and returns a dictionary containing the provided key-value pairs.

#### 3. Deletion-resilient hypermedia pagination

**File**: `3-hypermedia_del_pagination.py`

The goal here is that if between two queries, certain rows are removed from the dataset, the user does not miss items from dataset when changing page.

Implement a `get_hyper_index` method with two integer arguments: `index` with a `None` default value and `page_size` with default value of 10. The method should return a dictionary with the specified key-value pairs.

---

**GitHub repository**: holbertonschool-web_back_end  
**Directory**: pagination