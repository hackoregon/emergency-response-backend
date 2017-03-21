# import yaml
# from rest_framework.compat import coreapi, urlparse
# from rest_framework.schemas import SchemaGenerator
# from rest_framework_swagger import renderers
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import exceptions
# from rest_framework.permissions import AllowAny
#
#
# class CustomSchemaGenerator(SchemaGenerator):
#     def get_link(self, path, method, view):
#         """
#         __doc__ in yaml format, eg:
#         desc: the desc of this api.
#         parameters:
#         - name: mobile
#           desc: the mobile number
#           type: string
#           required: true
#           location: query
#         - name: promotion
#           desc: the activity id
#           type: int
#           required: true
#           location: form
#         """
#         fields = self.get_path_fields(path, method, view)
#         yaml_doc = None
#         func = getattr(view, view.action) if getattr(view, 'action', None) else None
#         if func and func.__doc__:
#             try:
#                 yaml_doc = yaml.load(func.__doc__)
#             except:
#                 yaml_doc = None
#         if yaml_doc and 'desc' in yaml_doc:
#             desc = yaml_doc.get('desc', '')
#             _method_desc = desc
#             params = yaml_doc.get('parameters', [])
#             for i in params:
#                 _name = i.get('name')
#                 _desc = i.get('desc')
#                 _required = i.get('required', True)
#                 _type = i.get('type', 'string')
#                 _location = i.get('location', 'query')
#                 f = coreapi.Field(
#                     name=_name,
#                     location=_location,
#                     required=_required,
#                     description=_desc,
#                     type=_type
#                 )
#                 fields.append(f)
#         else:
#             _method_desc = func.__doc__ if func and func.__doc__ else ''
#             fields += self.get_serializer_fields(path, method, view)
#         fields += self.get_pagination_fields(path, method, view)
#         fields += self.get_filter_fields(path, method, view)
#
#         if fields and any([field.location in ('form', 'body') for field in fields]):
#             encoding = self.get_encoding(path, method, view)
#         else:
#             encoding = None
#
#         if self.url and path.startswith('/'):
#             path = path[1:]
#
#         return coreapi.Link(
#             url=urlparse.urljoin(self.url, path),
#             action=method.lower(),
#             encoding=encoding,
#             fields=fields,
#             description=_method_desc
#         )
#
# def get_swagger_view(title=None, url=None, patterns=None, urlconf=None):
#     """
#     Return schema view which renders Swagger/OpenAPI.
#     """
#     class SwaggerSchemaView(APIView):
#         _ignore_model_permissions = True
#         exclude_from_schema = False
#         permission_classes = [AllowAny]
#         renderer_classes = [
#             renderers.JSONRenderer,
#             renderers.OpenAPIRenderer,
#             renderers.SwaggerUIRenderer
#         ]
#
#         def get(self, request):
#             generator = CustomSchemaGenerator(
#                 title=title,
#                 url=url,
#                 patterns=patterns,
#                 urlconf=urlconf
#             )
#             schema = generator.get_schema(request=request)
#
#             if not schema:
#                 raise exceptions.ValidationError(
#                     'The schema generator did not return a schema Document'
#                 )
#
#             return Response(schema)
#
#     return SwaggerSchemaView.as_view()
