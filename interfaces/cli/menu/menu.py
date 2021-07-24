from abc import abstractmethod

class Option:
    command: str
    description: str
    budget_ref = None

    def __init__(self, command, description):
        self.command = command
        self.description = description

    def __call__(self, budget_ref):
        self.budget_ref = budget_ref
        self._process()

    @abstractmethod
    def _process(self):
        pass


class AddTransaction(Option):
    def _process(self):
        print('add transaction')
        from_ = input('from: ')
        to = input('to: ')
        value = float(input('value: '))
        self.budget_ref.add_transaction(from_, to, value)


class ShowAssets(Option):
    def _process(self):
        print('print assets')


class ExitApp(Option):
    def _process(self):
        print('exit')


options = {
    't': AddTransaction('t', 'add transaction'),
    'a': ShowAssets('a', 'show assets'),
    'exit': ExitApp('exit', 'exit'),
}

def menu(budget_ref, prompt='> '):
    option = str(input(prompt))
    option = options.get(option)
    if option is None:
        print('Unknown command. try "help".')
    option(budget_ref)