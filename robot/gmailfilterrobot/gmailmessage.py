class GmailMessage:
    def __init__(self, data: dict) -> None:
        self.data = data
        self.headers = self.__get_headers__()

    def get_sender(self):
        header_from = self.headers.get("from")
        return (
            header_from
            .split(" ")[-1]
            .replace("<", "")
            .replace(">", "")
        )

    def __get_headers__(self) -> dict:
        headers = dict()
        for header in self.data.get("payload", {}).get("headers", []):
            headers[str(header["name"]).lower()] = header["value"]
        return headers
