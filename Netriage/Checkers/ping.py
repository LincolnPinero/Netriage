import subprocess
def ping_device(host):
    result = subprocess.run(["ping", host])
    if result.returncode == 0:
        return True
    else:
        return False
    pass