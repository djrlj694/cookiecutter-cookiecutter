# Cookiecutter-Cookiecutter

[Cookiecutter](https://github.com/audreyr/cookiecutter) is a cross-platform software tool that generates [**boilerplate**](https://en.wikipedia.org/wiki/Boilerplate_code) for [**software projects**](https://en.wikipedia.org/wiki/Software_project_management) from templates.  These templates, called **cookiecutters**, can be used to define a project's directory tree structure, the names of its directories and files, and the boilerplate content of its files.  They can also facilitate, both manually and automatically, the run-time customization of the generated names and boilerplate.

The cookiecutter presented here, Cookiecutter-Cookiecutter, defines a basic directory structure and template files for generating boilerplate for cookiecutters.  These cookiecutters are rudimentary, containing only a starter set of files.

## Usage

Boilerplate from Cookiecutter-Cookiecutter can be generated by running shell or Python scripts.  Furthermore, during boilerplate generation, Cookiecutter-Cookiecutter itself can be sourced remotely via a direct download or locally via a cached copy from a prior download.  The subsections that follow show the syntactic differences for each aforementioned approach.

### Shell

The command `cookiecutter` generates boilerplate from a shell's command-line interface (CLI).  The argument following `cookiecutter` specifies both the cookiecutter (which, in this case, is `cookiecutter-repo`) and whether its source is remote or local.

* Remote source:

    ```sh
    # The following syntax options are semantically equivalent.
    
    # Option 1: URL
    $ cookiecutter https://github.com/djrlj694/cookiecutter-repo.git
    
    # Option 2: 'gh" prefix
    $ cookiecutter gh:djrlj694/cookiecutter-repo
    
    # Option 3: 'git+ssh' prefix
    $ cookiecutter git+ssh://git@github.com/djrlj694/cookiecutter-repo.git
    ```

* Local source:

    ```sh
    $ cookiecutter cookiecutter-repo/
    ```

### Python

The Python library `cookiecutter.main` provides an application programming interface (API) for calling Cookiecutter functions to generate boilerplate.

* Remote source:

    ```python
    from cookiecutter.main import cookiecutter
       
    cookiecutter('https://github.com/djrlj694/cookiecutter-repo.git')
    ```
    
* Local source:

    ```python
    from cookiecutter.main import cookiecutter
       
    cookiecutter('cookiecutter-repo/')
    ```
    
## Options

The `cookiecutter.json` file, located in the root directory of a cookiecutter repository (i.e., in the same directory as the cookiecutter itself), specifies run-time customization options for generating a new repository.  These options are encoded as JSON key/value pairs.  Each key denotes a template variable (e.g., `{{cookiecutter.`*`JSON_KEY`*`}}`), whereas each value denotes either a default value or an array of legal values for its respective key.  Together with [Jinja2](http://jinja.pocoo.org/docs/2.10/) as a template language, `cookiecutter.json` can be used to customize the names of directories and files as well as the content within files.

Customization options defined in Cookiecutter-Cookiecutter's `cookiecutter.json` are as follows:

| Key | Description | Value(s) | Default Value |
| --- | ----------- | ------ | ------------- |
| `repo_docs_name` | Names the repository as it would appear in documents (i.e., permits spaces and mixed-case) | N/A | `REPO_DOCS_NAME` |
| `repo_dir_name` | Names a root directory for the repository that conforms to GitHub's naming conventions | N/A | A lower-case, hyphenated version of the value of `repo_formal_name` |
| `repo_license` | Specifies an open-source software licence or not | `Not open source`, `Apache Software License 2.0`, `BSD-3`, `GNU GPL v3.0`, `MIT`  | `Not open source` |
| `add_github` | Adds a `.github` directory tree with Markdown files documenting rules on how to contribute | `True`, `False` | `True` |
| `add_make` | Adds a `.make` directory tree with makefile files specifying build automation rules for software projects | `True`, `False` | `True` |

By default, the user is prompted to assign a value for each key.  This cookiecutter feature may also be silenced.  The subsections that follow show how.

### Shell

```sh
$ cookiecutter --no-input ...
```

### Python

```python
cookiecutter(..., no_input=True)
```

## System Requirements

Cookiecutter-Cookiecutter supports the 3 major operating systems:

* Linux
* macOS
* Windows

To use Cookiecutter-Cookiecutter, the following software must first be installed on your system:

* [Python](https://www.python.org/downloads/) 2.7, 3.4, 3.5, 3.3, or PyPy
* [Cookiecutter](https://github.com/audreyr/cookiecutter) Python package 1.6.0 or higher

## Installation

For info on installing any of the prerequisite software, refer to the [official](https://cookiecutter.readthedocs.io/en/latest/installation.html) installation document.

## Known Issues

Currently, there are no known issues.  If you discover any, please kindly submit a [pull request](.github/CONTRIBUTING.md).

## Contributing

Code and codeless (e.g., documentation) contributions toward improving Cookiecutter-Cookiecutter are welcome. See [CONTRIBUTING.md](.github/CONTRIBUTING.md) for more information on how to become a contributor.

## License

Cookiecutter-Cookiecutter is released under the [MIT License](LICENSE.md).
