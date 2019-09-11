# 导包
import yaml


def read_yaml(filename):
    """参数化读取yaml文件并使用数据"""
    with open("../data/" + filename, "r", encoding="utf-8")as f:
        arr = []
        for i in yaml.load(f).values():
            arr.append((i.get("username"), i.get("pwd")))
        return arr


if __name__ == '__main__':
    print(read_yaml("login.yaml"))