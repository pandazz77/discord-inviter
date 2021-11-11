import requests

def get_tokens(filepath="tokens.txt"):
    with open(filepath,"r") as f:
        return f.read().split("\n")
 
def join(token, server_invite):
    header = {"authorization": token}
    r = requests.post("https://discord.com/api/v8/invites/{}".format(server_invite), headers=header)
    if r.status_code == 200:
        return True
    else:
        return False

if __name__ == "__main__":
    tokens = get_tokens()
    user_input = input("Input invite link / invite code: ")

    if "https://discord.gg" in user_input:
        server_invite = user_input.split("https://discord.gg/")[1]
    else:
        server_invite = user_input

    for token in tokens:
        response = join(token,server_invite)
        print(f"{token} - {response}")
