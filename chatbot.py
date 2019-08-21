import json
import requests

def main():
    webhook_url = "개인hook url"
    content = "가즈아ㅏㅏ"
    payload = {"text": content}
    requests.post(
        webhook_url, data=json.dumps(payload),
        headers={'Content-Type': 'application/json'}
    )


if __name__ == '__main__':
    main()

