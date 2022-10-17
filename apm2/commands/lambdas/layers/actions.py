from apm2.utils.abstracts import BaseCommand


class CreateLayer(BaseCommand):
    def execute(self):
        print(f"create layer {self._payload}")


class DeleteLayer(BaseCommand):
    def execute(self):
        print(f"Delete layer {self._payload}")


class UpdateLayer(BaseCommand):
    def execute(self):
        print(f"Delete layer {self._payload}")


class ListLayers(BaseCommand):
    def execute(self):
        print(f"list layers {self._payload}")
