import subprocess
result = subprocess.run(['python3', 'to-compile.py'], stdout=subprocess.PIPE)
print(result.stdout.decode('utf-8'))
