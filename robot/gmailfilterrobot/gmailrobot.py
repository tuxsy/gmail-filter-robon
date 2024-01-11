from .gmailapp import GmailApp
from .gmailmessage import GmailMessage


def __filter_labels(labels: list, label_type: str) -> list:
    filtered_labels = []
    if labels is not None:
        for label in labels:

    return filtered_labels

class GmailRobot(GmailApp):


    def list_messages(self, query: str = "is:unread") -> list:
        results = self.service.users().messages().list(userId="me", q=query).execute()
        if results is not None:
            return results.get("messages", [])
        else:
            return None

    def get_message(self, message_id: str) -> GmailMessage:
        data = self.service.users().messages().get(userId="me", id=message_id).execute()
        return GmailMessage(data)

    def __list_labels__(self) -> list:
        results = self.service.users().labels().list(userId="me").execute()
        return results.get('labels', [])

