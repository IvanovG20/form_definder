from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from tinydb import TinyDB
from .validators import get_field_type


db = TinyDB("db/forms.json")
form_submissions_db = TinyDB("db/submissions.json")


class FormMatchView(APIView):
    def post(self, request):
        form_data = request.data.get("data", {})
        templates = db.all()

        for template in templates:
            if all(
                field in form_data and get_field_type(
                    form_data[field]
                ) == template[field]
                for field in template if field != "name"
            ):
                form_submissions_db.insert(
                    {
                        "template_name": template["name"],
                        "data": form_data
                    }
                )
                return Response(
                    {"template_name": template["name"]},
                    status=status.HTTP_200_OK
                )

        field_types = {
            field: get_field_type(value) for field, value in form_data.items()
        }

        form_submissions_db.insert(
            {
                "template_name": "unknown",
                "data": form_data,
                "field_types": field_types
            }
        )

        return Response(field_types, status=status.HTTP_200_OK)
