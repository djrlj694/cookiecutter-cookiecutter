#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = '{{ cookiecutter.author }}'
__coauthor__ = 'N/A'
__copyright__ = 'Copyright {% now 'local', '%Y' %}, {{ cookiecutter.repo_docs_name }}'
__credits__ = ['{{ cookiecutter.author }}']
__license__ = '{{ cookiecutter.license }}'
__version__ = '0.0.1'
__maintainer__ = '{{ cookiecutter.author }}'
__email__ = '{{ cookiecutter.email }}'
__status__ = 'Development'
__created_date__= '{% now 'local', '%b %d, %Y' %}'
__modified_date__= '{% now 'local', '%b %d, %Y' %}'

### Libraries ###

# 3rd-party

import os
import sys

from cookiecutter.main import cookiecutter

### Variable Declarations ###

### Function Declarations ###

### Main Program ###

sys.exit(0)
