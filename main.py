import requests

def get_tokens_data(filepath="tokens.txt"):
    tokens_data = []
    with open(filepath,"r") as f:
        data = f.read().split("\n")
        for string in data:
            splited_string = string.split(" ")
            tokens_data.append((splited_string[0],splited_string[1]))
    return tokens_data

def check_proxie(proxies:dict):
    response = requests.get("http://jsonip.com",proxies=proxies)
    ip = response.json()["ip"]
    return ip

def parse_proxie(proxie:str,null="None",check=False):
    if proxie == null:
        return None

    splited_proxie = proxie.split(":")

    ip = splited_proxie[0]
    port = splited_proxie[1]
    login = splited_proxie[2]
    pswd = splited_proxie[3]

    proxies = {
        "http":f"http://{login}:{pswd}@{ip}:{port}",
        "https":f"http://{login}:{pswd}@{ip}:{port}"
    }

    if check:
        check_response = check_proxie(proxies)
        if check_response != ip:
            return None

    return proxies
 
def join(token, server_invite, proxies):
    header = {"authorization": token}
    if proxies == None:
        r = requests.post("https://discord.com/api/v8/invites/{}".format(server_invite), headers=header)
    else:
        r = requests.post("https://discord.com/api/v8/invites/{}".format(server_invite), headers=header,proxies=proxies)

    if r.status_code == 200:
        return True
    else:
        return False


if __name__ == "__main__":
    tokens_data = get_tokens_data()
    user_input = input("Input invite link / invite code: ")

    if "https://discord.gg" in user_input:
        server_invite = user_input.split("https://discord.gg/")[1]
    else:
        server_invite = user_input

    for token_data in tokens_data:
        token = token_data[0]
        proxies = parse_proxie(token_data[1])
        #print(check_proxie(proxies))
        response = join(token,server_invite,proxies)
        print(f"{token}|{proxies}- {response}")
