import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from repository import all, retrieve, create, update


class HandleRequests(BaseHTTPRequestHandler):
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """

    def parse_url(self, path):
        '''Just like splitting a string in JavaScript. If the path is "/animals/1", the resulting list will have "" at index 0, "animals" at index 1, and "1" at index 2.'''

        path_params = path.split("/")
        resource = path_params[1]
        id = None

        # Try to get item at index 2
        try:
            id = int(path_params[2])
        except IndexError:
            pass
        except ValueError:
            pass

        return (resource, id)

    def do_GET(self):
        """Handles GET requests to the server """
        response = {}
        (resource, id) = self.parse_url(self.path)

        if id is not None:
            response = retrieve(resource, id)
        else:
            response = all(resource)

        if response is not None:
            self._set_headers(200)
        else:
            self._set_headers(404)
            response = {
                "message": "this is not the file you're looking for"}

        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        """Handles POST requests to the server """

        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        (resource, id) = self.parse_url(self.path)

        new_order = None

        if resource == "orders":
            if "metalId" in post_body and "sizeId" in post_body and "settingId" in post_body and "styleId" in post_body:
                self._set_headers(201)
                new_order = create(post_body)
            else:
                self._set_headers(400)
                new_order = {"message": f'{"please enter a metal" if "metalId" not in post_body else ""}{"please enter a size" if "sizeId" not in post_body else ""}{"please enter a style" if "styleId" not in post_body else ""}{"please enter a setting" if "settingId" not in post_body else ""}'}

            self.wfile.write(json.dumps(new_order).encode())

    def do_PUT(self):
        """Handles PUT requests to the server """

        self._set_headers(204)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        (resource, id) = self.parse_url(self.path)

        if resource == "metals":
            update(id, post_body)

            # self.wfile.write(json.dumps(response).encode())
            # update_order(id, post_body)

        self.wfile.write("".encode())

    def _set_headers(self, status):
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                         'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                         'X-Requested-With, Content-Type, Accept')
        self.end_headers()


# point of this application.
def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
