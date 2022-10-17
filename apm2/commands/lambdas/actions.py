from apm2.utils.abstracts import BaseCommand


class CreateLambda(BaseCommand):
    def execute(self):
        print(f"create lambda {self._payload}")


class DeleteLambda(BaseCommand):
    def execute(self):
        print(f"Delete lambda {self._payload}")


class UpdateLambda(BaseCommand):
    def execute(self):
        print(f"Delete lambda {self._payload}")


class ListLambdas(BaseCommand):
    def execute(self):
        print(f"list lambdas {self._payload}")


class UpdateProperty(BaseCommand):
    def execute(self):
        print(f"Delete lambda {self._payload}")
