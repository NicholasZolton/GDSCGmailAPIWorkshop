from boiler import get_service


# To find more cool things you can do with the Gmail API, check out the documentation:
# https://googleapis.github.io/google-api-python-client/docs/dyn/gmail_v1.users.labels.html#list
def main():
    service = get_service()
    results = service.users().labels().list(userId="me").execute()
    labels = results.get("labels", [])

    if not labels:
        print("No labels found.")
        return

    print("Labels:")
    for label in labels[:5]:
        print(label["name"])


if __name__ == "__main__":
    main()
