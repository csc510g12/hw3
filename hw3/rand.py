import secrets

def random_array(arr):
    shuffled_num = None
    for i in range(len(arr)):
        # Use random to pass bandit security checks
        # shuffled_num = subprocess.run(["shuf", "-i1-20", "-n1"], capture_output=True)
        # arr[i] = int(shuffled_num.stdout)
        arr[i] = secrets.randbelow(20) + 1
    return arr
