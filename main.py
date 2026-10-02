# import sys


# def calculate(numbers, index):
#     if index == len(numbers):
#         return 0

#     num = numbers[index]

#     if num > 0:
#         return calculate(numbers, index + 1)

#     return num ** 4 + calculate(numbers, index + 1)


# def solve_cases(remaining, results):
#     if remaining == 0:
#         return results

#     x = int(input())
#     numbers = list(map(int, input().split()))

#     if len(numbers) != x:
#         results.append(-1)
#     else:
#         results.append(calculate(numbers, 0))

#     return solve_cases(remaining - 1, results)


# def main():
#     n = int(input())
#     results = solve_cases(n, [])
#     sys.stdout.write("\n".join(map(str, results)))


# if __name__ == "__main__":
#     main()







import time
import hmac
import hashlib
import base64
import json
import urllib.request
import urllib.error


email = "makandard20@gmail.com"
gist_url = "https://gist.github.com/dawalmalik0405-spec/aee11584c6d471705ce4572ba7a64ae5"

secret = (email + "HENNGECHALLENGE004").encode()

counter = int(time.time()) // 30
message = counter.to_bytes(8, byteorder="big")

digest = hmac.new(
    secret,
    message,
    hashlib.sha512
).digest()

offset = digest[-1] & 0x0F

binary_code = int.from_bytes(
    digest[offset:offset + 4],
    byteorder="big"
) & 0x7FFFFFFF

totp = str(binary_code % 10**10).zfill(10)

payload = {
    "github_url": gist_url,
    "contact_email": email,
    "solution_language": "python"
}

data = json.dumps(payload).encode()

credentials = base64.b64encode(
    f"{email}:{totp}".encode()
).decode()

request = urllib.request.Request(
    "https://api.challenge.hennge.com/challenges/backend-recursion/004",
    data=data,
    method="POST",
    headers={
        "Content-Type": "application/json",
        "Authorization": f"Basic {credentials}"
    }
)

try:
    with urllib.request.urlopen(request) as response:
        print("Status:", response.status)
        print(response.read().decode())

except urllib.error.HTTPError as error:
    print("Status:", error.code)
    print(error.read().decode())