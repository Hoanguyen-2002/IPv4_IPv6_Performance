import subprocess

# Set the target host
HOST = input('HOST: ')

# Test the performance of IPv4
print("Testing IPv4...")
result = subprocess.run(["ping", "-c", "10", "-4", HOST], stdout=subprocess.PIPE)
output = result.stdout.decode("utf-8")
print(output)

# Test the performance of IPv6
print("Testing IPv6...")
result = subprocess.run(["ping", "-c", "10", "-I", "::1", HOST], stdout=subprocess.PIPE)
output = result.stdout.decode("utf-8")
print(output)