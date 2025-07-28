import platform

# 64 bit or 32bit
architecture = platform.architecture()[0]
print(f"The operating system is {architecture}.")
print('Python compiler:', platform.python_compiler())
# displaying system info
print('System info:', platform.system())
# displaying platform processor name
print('Platform processor:', platform.platform())

# displaying system network name
print('Systems network name:', platform.node())
