import pexpect

# Start an SSH session
child = pexpect.spawn('ssh user@hostname')

# Wait for the password prompt
child.expect('Password:')

# Send the password
child.sendline('mypassword')

# Interact with the shell
child.expect('$')  # Wait for shell prompt
child.sendline('ls')  # Send a command to the shell

# Capture the output of the 'ls' command
child.expect('$')  # Wait for the command to complete
print(child.before.decode())  # Print the command output
