from utils.abstracts import BaseCommand


class CreatePath(BaseCommand):
    def execute(self):
        print(f"create swagger path {self._payload}")


class DeletePath(BaseCommand):
    def execute(self):
        print(f"Delete swagger path {self._payload}")


class UpdatePath(BaseCommand):
    def execute(self):
        print(f"Delete swagger path {self._payload}")


class ListPaths(BaseCommand):
    def execute(self):
        print(f"list swagger paths {self._payload}")


class UpdateProperty(BaseCommand):
    def execute(self):
        print(f"Delete swagger path {self._payload}")
