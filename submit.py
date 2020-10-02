from subprocess import run

print("Submitting Files")
run(["git", "add", "."])
run(["git", "commit", "-m", "Working"])
run(["git", "push", "orgin"])