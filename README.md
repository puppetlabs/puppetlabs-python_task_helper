
# python_task_helper

A Python helper library for use by [Puppet Tasks](https://puppet.com/docs/bolt/1.x/writing_tasks.html). It provides a class that handles error generation, simplifies JSON input and output, and makes testing your task easier. It requires Bolt >= 1.1 and Puppet Enterprise >= 2019.0.

#### Table of Contents

1. [Description](#description)
1. [Requirements](#requirements)
1. [Setup](#setup)
1. [Usage](#usage)
1. [Debugging](#debugging)

## Description

This library handles parsing JSON input, serializing the result as JSON output, and producing a formatted error message for errors.

## Requirements

This library works with Python 2.7 and later.

## Setup

To use this library, include this module in a `Puppetfile`
```ruby
mod 'puppetlabs-python_task_helper'
```

Add it to your [task metadata](https://puppet.com/docs/bolt/1.x/writing_tasks.html#concept-677) (note that the helper expects to read arguments on stdin)
```json
{
  "files": ["python_task_helper/files/task_helper.py"],
  "input_method": "stdin"
}
```

## Usage

When writing your task include the library in your script, extend the `TaskHelper` module, and write the `task()` function. The `task()` function **must** take a hash of parameters as input (even if it's an empty hash), and **must** return a hash. The following is an example of a task that uses the library

```python
#!/usr/bin/env python

import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'python_task_helper', 'files'))
from task_helper import TaskHelper

class MyTask(TaskHelper):
    def task(self, args):
        return {'result': 'Hi, my name is '+args['name']}

if __name__ == '__main__':
    MyTask().run()
```

You can then run the task like any other Bolt task
```shell
bolt task run mymodule::task -n target.example.com name='Robert'
```

You can find this example in [examples](examples), as well as an example test in [tests](tests). For a real task, `examples` would be renamed to `tasks`.

You can additionally provide detailed errors by raising a `TaskError`, such as
```python
class MyTask(TaskHelper):
    def task(self, args):
        raise TaskError('my task errored', 'mytask/error_kind', {'location': 'task entry'})
```

## Debugging

When writing your task, it can be helpful to write debugging statements to locate
the source of any errors. The library includes a `debug` method that accepts arbitrary
values and logs it as a debugging statement. If the task errors, the list of
debugging statements will be included in the resulting error message.

The list of debugging statements can also be accessed from the task itself by accessing
the `debug_statements` attribute. This can be used to include the debugging statements in
a `TaskError` that you explicitly raise.

Adding a debugging statement:
```python
self.debug('Result of method call: {}'.format(result))
```
Adding the list of debugging statements to a `TaskError`:
```python
raise TaskError('my task error message',
                'mytask/error-kind',
                { 'debug': self.debug_statements })
```
