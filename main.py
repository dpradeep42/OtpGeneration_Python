import secrets
import string


def generateOtp(length):
    numbers = string.digits
    otp = ''.join(secrets.choice(numbers) for i in range(length))
    print(otp)


if __name__ == '__main__':
    generateOtp(int(input("Enter the length of OTP: ")))
