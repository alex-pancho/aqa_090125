import urllib.request
import urllib.parse

def get_method(url:str = "https://www.example.com"):
    """ Getting data... """
    response = urllib.request.urlopen(url)
    data = response.read()
    return data


def post_method(url:str = "https://www.example.com", data:dict = {}):
    """ Getting data... """
    encode_data = urllib.parse.urlencode(data).encode('utf-8')
    response = urllib.request.urlopen(url, data=encode_data)
    result = response.read()
    return result


def put_method(url:str = "https://www.example.com", data:dict = {}):
    """ Getting data... """
    encode_data = urllib.parse.urlencode(data).encode('utf-8')
    request = urllib.request.Request(
        url, 
        method='PUT',
        data=encode_data, 
        headers={'Content-Type': 'application/json'}
    )
    with urllib.request.urlopen(request) as f:
        result = f.read()
        return result


def pastebin():
    url = "https://pastebin.com/api/api_post.php"
    post_data = dict(
        api_dev_key = "ulMHuv-FlPEloav7EYTG3u4jRLqizgxJ",
        api_paste_code = "Ми вивчаємо запити у пітон",
        api_option = "paste",
    )
    return post_method(url, post_data)


if __name__ =="__main__":
    print(get_method())
    print(pastebin()) # HTTP Error 403: Forbidden
    # print(put_method()) # HTTP Error 501: Not Implemented