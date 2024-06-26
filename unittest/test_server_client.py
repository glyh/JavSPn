import requests

def main():
    url = "http://localhost:4000/jsonrpc"

    # Example echo method
    payload = {
        "method": "echo",
        "params": ["echome!"],
        "jsonrpc": "2.0",
        "id": 0,
    }
    response = requests.post(url, json=payload).json()

    assert response["result"] == "echome!"
    assert response["jsonrpc"]
    assert response["id"] == 0

if __name__ == "__main__":
    main()
