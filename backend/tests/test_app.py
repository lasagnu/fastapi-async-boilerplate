import pytest
import json
from pathlib import Path

openapi_json_path = Path(__file__).parent / "../docs/openapi.json"

class TestGenerateDocumentation:

    def test_generate_documentation(self, client):
        response = client.get("/openapi.json")

        assert response.text

        openapi_data = json.loads(response.text)

        with open(openapi_json_path, "w") as file:
            json.dump(openapi_data, file, indent=4)


class TestMainPage:
    TEST_URL = "/"

    @pytest.mark.asyncio
    async def test_returns_200(self, client):
        response = client.get(self.TEST_URL)

        assert response.status_code == 200