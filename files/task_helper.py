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
        error_hash = { 'kind': self.kind, 'msg': self.__str__(), 'details': self.details }
        if self.issue_code:
            error_hash['issue_code'] = self.issue_code
        result = { '_error': error_hash }
        return result

class TaskHelper:
    def __init__(self):
        self.debug_statements = []

    def debug(self, statement):
        self.debug_statements.append(statement)

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
            exit(1)
        except Exception as err:
            error_hash = {
                'kind': 'python.task.helper/exception',
                'issue_code': 'EXCEPTION',
                'msg': err.__str__(),
                'details': {
                    'class': err.__class__.__name__,
                    'debug': self.debug_statements
                }
            }
            print(json.dumps({ '_error': error_hash }))
            exit(1)
