from .gmailapp import GmailApp


class GmailRobot(GmailApp):

    def list_labels(self):
        results = self.service.users().labels().list(userId='me').execute()
        labels = results.get('labels', [])

        if not labels:
            print('No labels found.')
            return
        print('Labels:')
        for label in labels:
            print(label['name'])
