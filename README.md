
# python_task_helper

A Python helper library for use by Puppet Tasks. Using it requires the Shareable Task Code feature, implemented in Bolt 1.1 and Puppet Enterprise 2019.0.

#### Table of Contents

1. [Description](#description)
1. [Requirements](#requirements)
1. [Usage - Configuration options and additional functionality](#usage)
1. [Development - Guide for contributing to the module](#development)

## Description

This library handles parsing JSON input, serializing the result as JSON output, and producing a formatted error message for errors.

## Requirements

This library works with Python 2.7 and later.

## Usage

To use this library in a task, import it in your `Puppetfile`
```
mod 'puppetlabs-python_task_helper'
```
add it to your metadata
```
{
  "files": ["python_task_helper/lib/task_helper.py"]
}
```
and write your task to extend the `TaskHelper` class.
```
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'python_task_helper', 'lib'))
from task_helper import TaskHelper

class MyTask(TaskHelper):
    def task(self, args):
        return {'result': args['hello']}

if __name__ == '__main__':
    MyTask().run()
```

You can additionally provide detailed errors by raising a `TaskError`, such as
```
class MyTask(TaskHelper):
    def task(self, args):
        raise TaskError('my task errored', 'mytask/error_kind', {'location': 'task entry'})
```

## Development

To test this library,
```
pip install pytest
pytest
```
