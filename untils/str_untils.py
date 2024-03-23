import base64

def convert_str_base64(str):
    """
    将字符串转为base64格式的字符串
    """
    if not str:
        return None
    bytes_str = str.encode('utf-8')
    base64_bytes = base64.b64encode(bytes_str)
    base64_str = base64_bytes.decode('utf-8')
    return base64_str