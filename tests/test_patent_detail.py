# _*_ codign:utf8 _*_
"""====================================
@Author:Sadam·Sadik
@Email：1903249375@qq.com
@Date：2024/3/2
@Software: PyCharm
@disc:
======================================="""
import math
import sys

from saer import Saer


def test_search_query_dsl_gkggr_range(range=None, pagesize: int = 300):
    """
    结论已经得出: 这个range的两边都包含关系
    :param range: the two side of the range is same, the server will return 500,服务器繁忙
    :param pagesize:
    :return:
    """
    if range is None:
        range = ["1999-04-06", "1999-04-07"]
    query_dsl = {
        "must": [
            # {"children__patent__zflh": {"any": ["H01F1/42", "H01F1/49"]}}
            {"children__patent__gkggr": {"range": range}}
        ]
    }
    sort_dsl = {"gkggr": {"order": "desc"}}
    page = 1
    totalPages = math.inf
    while page <= totalPages:
        resp = api.patent_search(
            dsl_query=query_dsl,
            sort=sort_dsl,
            v_show=False,
            page_index=str(page),
            page_size=str(pagesize)
        )
        result = resp.json()["result"]
        dataList = result["datalist"]
        total = result["total"]
        if page == 1:
            totalPages = math.ceil(total / pagesize)
            print(total, totalPages)
        print("=" * 50, "page{}({})".format(page, len(dataList)), "=" * 50)
        for item in dataList:
            print(item['gkggr'], item)
        page += 1
        # if page == 1 and totalPages != 0:
        #     page += 1
        # else:
        #     break


if __name__ == '__main__':
    client_id = sys.argv[1]
    client_key = sys.argv[2]
    print(client_id, "|", client_key)
    api = Saer(client_id, client_key)
    test_search_query_dsl_gkggr_range([None, "1999-04-07"], 5)
    # print(len("00000071ba45f2bfb7f3488ae1ed8fa1"))
    # api.patent_detail("7c93aaf306ae966dcb2baa13e27d9b6e")
    # api.patent_detail("d3f524ac244a8368ba30af5e3404df1a")
    # api.patent_detail("00000071ba45f2bfb7f3488ae1ed8fa1")
#
