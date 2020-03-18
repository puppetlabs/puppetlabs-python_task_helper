import json
import pytest
import sys
import unittest
from task_helper import TaskHelper, TaskError

if (sys.version_info > (3, 0)):
    from io import StringIO
else:
    from StringIO import StringIO

def stub_stdin(testcase_inst, inputs):
    stdin = sys.stdin

    def cleanup():
        sys.stdin = stdin

    testcase_inst.addCleanup(cleanup)
    sys.stdin = StringIO(inputs)

def stub_stdouts(testcase_inst):
    stderr = sys.stderr
    stdout = sys.stdout

    def cleanup():
        sys.stderr = stderr
        sys.stdout = stdout

    testcase_inst.addCleanup(cleanup)
    sys.stderr = StringIO()
    sys.stdout = StringIO()

class TestHelper(unittest.TestCase):
    def test_no_method(self):
        stub_stdin(self, '{"hello": "world"}')
        stub_stdouts(self)
        class MyTask(TaskHelper):
            pass
        with pytest.raises(SystemExit) as pytest_wrapped_e:
            MyTask().run()
            assert pytest_wrapped_e.value.code == 1
        result = json.loads(sys.stdout.getvalue())
        self.assertEqual(result, {
            '_error': {
                'kind': 'python.task.helper/exception',
                'issue_code': 'EXCEPTION',
                'msg': 'TaskHelper.task is not implemented',
                'details': {}
            }
        })

    def test_error_method(self):
        stub_stdin(self, '{"hello": "world"}')
        stub_stdouts(self)
        class MyTask(TaskHelper):
            def task(self, args):
                raise Exception('does not work')
        with pytest.raises(SystemExit) as pytest_wrapped_e:
            MyTask().run()
            assert pytest_wrapped_e.value.code == 1
        result = json.loads(sys.stdout.getvalue())
        self.assertEqual(result, {
            '_error': {
                'kind': 'python.task.helper/exception',
                'issue_code': 'EXCEPTION',
                'msg': 'does not work',
                'details': { 'class': 'Exception', 'debug': [] }
            }
        })

    def test_task_error(self):
        stub_stdin(self, '{"hello": "world"}')
        stub_stdouts(self)
        class MyTask(TaskHelper):
            def task(self, args):
                raise TaskError('a task error', 'mytask/failed', {'any': 'thing'})
        with pytest.raises(SystemExit) as pytest_wrapped_e:
            MyTask().run()
            assert pytest_wrapped_e.value.code == 1
        result = json.loads(sys.stdout.getvalue())
        self.assertEqual(result, {
            '_error': {
                'kind': 'mytask/failed',
                'msg': 'a task error',
                'details': {'any': 'thing'}
            }
        })

    def test_echo_method(self):
        stub_stdin(self, '{"hello": "world"}')
        stub_stdouts(self)
        class MyTask(TaskHelper):
            def task(self, args):
                return {'result': args['hello']}
        MyTask().run()
        result = json.loads(sys.stdout.getvalue())
        self.assertEqual(result, {'result': 'world'})

    def test_debug_method(self):
        stub_stdin(self, '{"hello": "world"}')
        stub_stdouts(self)
        class MyTask(TaskHelper):
            def task(self, args):
                self.debug('a debugging statement')
                self.debug('another debugging statement')
                raise TaskError(
                    'a task error',
                    'mytask/failed',
                    { 'debug': self.debug_statements }
                )
        with pytest.raises(SystemExit) as pytest_wrapped_e:
            MyTask().run()
            assert pytest_wrapped_e.value.code == 1
        result = json.loads(sys.stdout.getvalue())
        self.assertEqual(result, {
            '_error': {
                'kind': 'mytask/failed',
                'msg': 'a task error',
                'details': { 'debug': ['a debugging statement', 'another debugging statement'] }
            }
        })
