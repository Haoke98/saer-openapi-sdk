# _*_ codign:utf8 _*_
"""====================================
@Author:Sadam·Sadik
@Email：1903249375@qq.com
@Date：2024/3/2
@Software: PyCharm
@disc:
======================================="""
import sys

from saer import Saer

if __name__ == '__main__':
    client_id = sys.argv[1]
    client_key = sys.argv[2]
    print(client_id, "|", client_key)
    api = Saer(client_id, client_key)
    # api.patent_search(dsl_query={"must": [{"children__patent__zflh": {"any": ["H01F1/42", "H01F1/49"]}}]},
    #                   sort={"gkggr": {"order": "desc"}})
    print(len("00000071ba45f2bfb7f3488ae1ed8fa1"))
    api.patent_detail("7c93aaf306ae966dcb2baa13e27d9b6e")
    api.patent_detail("d3f524ac244a8368ba30af5e3404df1a")
    api.patent_detail("00000071ba45f2bfb7f3488ae1ed8fa1")
