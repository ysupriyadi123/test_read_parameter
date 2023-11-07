from retry_request import RetryRequest

request = RetryRequest()

try:
    response = request.get()

    if response.status_code >= 400:
        raise Exception(response.text)

    print("SUCCESS ")
except Exception as e:
    print(e)


print()
print(">>> End of the script")