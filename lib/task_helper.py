import json, sys

class TaskError(Exception):
    def __init__(self, msg, kind, details = None, issue_code = None):
        super(Exception, self).__init__(msg)
        self.kind = kind
        if details:
            self.details = details
        else:
            self.details = {}
        self.issue_code = issue_code

    def to_hash(self):
        result = { 'kind': self.kind, 'msg': self.__str__(), 'details': self.details }
        if self.issue_code:
            result['issue_code'] = self.issue_code
        return result

class TaskHelper:
    def task(self, args):
        raise TaskError(
            'TaskHelper.task is not implemented',
            'python.task.helper/exception',
            {},
            'EXCEPTION')

    def run(self):
        try:
            args = json.load(sys.stdin)
            output = self.task(args)
            print(json.dumps(output))
        except TaskError as err:
            print(json.dumps(err.to_hash()))
        except Exception as err:
            print(json.dumps({
                'kind': 'python.task.helper/exception',
                'issue_code': 'EXCEPTION',
                'msg': err.__str__(),
                'details': { 'class': err.__class__.__name__ }
            }))
