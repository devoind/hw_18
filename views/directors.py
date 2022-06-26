from flask_restx import Resource, Namespace
from dao.model.directors import DirectorSchema
from implemented import director_service

director_ns = Namespace('directors')


@director_ns.route('/')
class GenresView(Resource):
    schema = DirectorSchema(many=True)

    def get(self):
        """
        Вьюшка для запроса списка директоров

        :return: возвращает список директоров
        """
        return self.schema.dump(director_service.get()), 200


@director_ns.route('/<int:director_id>')
class GenreView(Resource):
    schema = DirectorSchema()

    def get(self, director_id):
        """
        Вьюшка для запроса 1-го директора

        :return: возвращает 1-го директора
        """
        return self.schema.dump(director_service.get(director_id)), 200
