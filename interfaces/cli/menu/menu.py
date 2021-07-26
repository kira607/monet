from abc import abstractmethod
from budget.budget import Budget
from budget.transaction import Transaction

class Option:
    command: str
    description: str
    budget: Budget = None

    def __init__(self, command, description):
        self.command = command
        self.description = description

    def __call__(self, budget_ref):
        self.budget = budget_ref
        self._process()

    @property
    def exit(self):
        return True

    @abstractmethod
    def _process(self):
        pass


class AddTransaction(Option):
    def _process(self):
        print('add transaction')
        t = self.__input_transaction()
        self.budget.add_transaction(*t)

    def __input_transaction(self):
        from_ = input('From:')
        to = input('To: ')
        value = float(input('Value: '))
        return (from_, to, value)

class ShowAssets(Option):
    def _process(self):
        print('show assets')


class ShowTransactions(Option):
    def _process(self):
        print('transactions')


class ExitApp(Option):
    def _process(self):
        print('exit')

    @property
    def exit(self):
        return False


class Options:

    def __init__(self, option):
        self.options = {
            't': AddTransaction('t', 'add transaction'),
            'a': ShowAssets('a', 'show assets'),
            's': ShowTransactions('s', 'show transactions'),
            'e': ExitApp('exit', 'exit'),
            'h': self.__help(self)
        }
        self.option = option

    def __call__(self, budget_ref):
        if (process := self.options.get(self.option)) is None:
            process = self.__default()
        process(budget_ref)
        return process.exit

    def __default(self):
        class Default(Option):
            def _process(self):
                print('Unknown command. type "h" for help.')
        return Default('', '')

    def __help(self, opts_ref):
        class Help(Option):
            def __init__(self, command, description, opts_ref):
                self.opts_ref = opts_ref
                super().__init__(command, description)
            def _process(self):
                opts = self.opts_ref.options
                for cmd, obj in opts.items():
                    print(f'{cmd} - {obj.description}')
        return Help('help', 'show help', opts_ref)


def menu(budget_ref, prompt='> ') -> bool:
    option = str(input(prompt))
    option = Options(option)
    return option(budget_ref)