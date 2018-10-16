import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'python_task_helper', 'lib'))
from task_helper import TaskHelper

class MyTask(TaskHelper):
    def task(self, args):
        return {'result': args['hello']}

if __name__ == '__main__':
    MyTask().run()

