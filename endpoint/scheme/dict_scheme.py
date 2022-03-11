from marshmallow import Schema, fields


class DictScheme(Schema):
    id = fields.Int()
    name = fields.Str()


dict_scheme = DictScheme()
dict_list_scheme = DictScheme(many=True)
