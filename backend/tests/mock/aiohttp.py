import dataclasses
import logging

data_to_use = []
next_status = [
    200,
]


@dataclasses.dataclass
class RequestData:
    method: str
    url: str
    data: dict
    params: dict | None = None


requests_done: list[RequestData] = []


class MockGetRequest:

    def __init__(self, *args, **kwargs):
        self.url = args[0] if args else kwargs.get('url', "")
        self.status = next_status.pop(0) if next_status else 200
        self.params = kwargs.get('params', {})
        self._return_data = data_to_use.pop(0) if data_to_use else None

        requests_done.append(
            RequestData(
                method='GET',
                url=self.url,
                data={},
                params=self.params,
            )
        )

        if self.params and any(value is None for value in self.params.values()):
            assert False, "None value in params"

        if self.params and any(isinstance(value, bool) for value in self.params.values()):
            assert False, "Boolean value in params"

    async def json(self):
        return self._return_data

    async def text(self):
        return self._return_data

    async def __aenter__(self):
        logging.debug("Making GET request to URL %s", self.url)

    async def __aexit__(self, esc_type, exc_val, exc_tb):
        pass


class MockPostRequest:

    def __init__(self, *args, **kwargs):
        self.url = args[0] if args else kwargs.get('url', "")
        self.data = kwargs.get('json', {}) or kwargs.get('data', {})
        self.status = next_status.pop(0) if next_status else 200
        self._return_data = data_to_use.pop(0) if data_to_use else None

        requests_done.append(RequestData(method='POST', url=self.url, data=self.data))

    async def json(self):
        return self._return_data

    async def text(self):
        return self._return_data

    async def __aenter__(self):
        logging.debug("Making POST request to URL %s", self.url)

    async def __aexit__(self, esc_type, exc_val, exc_tb):
        pass


class MockPutRequest:
    def __init__(self, *args, **kwargs):
        self.url = args[0] if args else kwargs.get('url', "")
        self.data = kwargs.get('json', {}) or kwargs.get('data', {})
        self.status = next_status.pop(0) if next_status else 200
        self._return_data = data_to_use.pop(0) if data_to_use else None

        requests_done.append(RequestData(method='PUT', url=self.url, data=self.data))

    async def json(self):
        return self._return_data

    async def text(self):
        return self._return_data

    async def __aenter__(self):
        logging.debug("Making PUT request to URL %s", self.url)

    async def __aexit__(self, esc_type, exc_val, exc_tb):
        pass


class MockDeleteRequest:
    def __init__(self, *args, **kwargs):
        self.url = args[0] if args else kwargs.get('url', "")
        self.data = kwargs.get('json', {}) or kwargs.get('data', {})
        self.status = next_status.pop(0) if next_status else 200
        self._return_data = data_to_use.pop(0) if data_to_use else None

        requests_done.append(RequestData(method='DELETE', url=self.url, data=self.data))

    async def text(self):
        return f'Mock returned Status Code: {self.status}'

    async def __aenter__(self):
        logging.debug("Making DELETE request to URL %s", self.url)

    async def __aexit__(self, esc_type, exc_val, exc_tb):
        pass


class MockPatchRequest:
    def __init__(self, *args, **kwargs):
        self.url = args[0] if args else kwargs.get('url', "")
        self.data = kwargs.get('json', {}) or kwargs.get('data', {})
        self.status = next_status.pop(0) if next_status else 200
        self._return_data = data_to_use.pop(0) if data_to_use else None

        requests_done.append(RequestData(method='PATCH', url=self.url, data=self.data))

    async def json(self):
        return self._return_data

    async def text(self):
        return self._return_data

    async def __aenter__(self):
        logging.debug("Making PATCH request to URL %s", self.url)

    async def __aexit__(self, esc_type, exc_val, exc_tb):
        pass


class MockSessionContext:
    pass

    def get(self, *args, **kwargs):
        return MockGetRequest(*args, **kwargs)

    def post(self, *args, **kwargs):
        return MockPostRequest(*args, **kwargs)

    def put(self, *args, **kwargs):
        return MockPutRequest(*args, **kwargs)

    def delete(self, *args, **kwargs):
        return MockDeleteRequest(*args, **kwargs)

    def patch(self, *args, **kwargs):
        return MockPatchRequest(*args, **kwargs)


class MockSession:
    async def __aenter__(self):
        return MockSessionContext()

    async def __aexit__(self, esc_type, exc_val, exc_tb):
        pass
