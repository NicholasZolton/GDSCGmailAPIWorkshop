from gmailsample.boiler import get_service


# To find more cool things you can do with the Gmail API, check out the documentation:
# https://googleapis.github.io/google-api-python-client/docs/dyn/gmail_v1.users.labels.html#list
def main():
    service = get_service()
    results = service.users().messages().list(userId="me").execute()
    messages = results.get("messages", [])

    if not messages:
        print("No messages found.")
        return

    print("Messages:")
    for message in messages[:5]:
        # get the message given ID
        message = (
            service.users().messages().get(userId="me", id=message["id"]).execute()
        ).get("payload")

        # get the subject from the message
        subject = next(
            (
                header["value"]
                for header in message["headers"]
                if header["name"] == "Subject"
            ),
            None,
        )

        print(subject)


if __name__ == "__main__":
    main()
