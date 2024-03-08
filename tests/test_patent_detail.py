# _*_ codign:utf8 _*_
"""====================================
@Author:Sadam·Sadik
@Email：1903249375@qq.com
@Date：2024/3/2
@Software: PyCharm
@disc:
======================================="""
import datetime
import math
import sys

from saer import Saer


def test_search_query_dsl_gkggr_range(gkggr_range=None, pagesize: int = 300, page_start: int = 1):
    """
    结论已经得出: 这个range的两边都包含关系
    :param range: the two side of the range is same, the server will return 500,服务器繁忙
    :param pagesize:
    :return:
    """
    if gkggr_range is None:
        gkggr_range = ["1999-04-06", "1999-04-07"]
    query_dsl = {
        "must": [
            {"children__patent__zflh": {"any": ["A", "B", "C", "D", "E", "F", "G", "H"]}},
            {"children__patent__gkggr": {"range": gkggr_range}}
        ]
    }
    sort_dsl = {"gkggr": {"order": "desc"}}
    page = page_start
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
        if page == page_start:
            totalPages = math.ceil(total / pagesize)
            print("total:{}, totalPages:{}".format(total, totalPages))
        print("=" * 50, "page{}({})".format(page, len(dataList)), "=" * 50)
        for item in dataList:
            print(item['gkggr'], item)
        page += 1
        # if page == 1 and totalPages != 0:
        #     page += 1
        # else:
        #     break


def test_search_query_dsl_gkggr_range_date_block():
    """
    Test the search query
    :return:
    """
    interval = datetime.timedelta(days=30)
    start = datetime.date(year=1987, month=5, day=19)
    end = datetime.date(year=1990, month=1, day=1)
    current = start
    n = 1
    while current < end:
        date_block_start = current
        date_block_end = min(current + interval, end)
        query_dsl = {
            "must": [
                # {"children__patent__zflh": {"any": ["A", "B", "C", "D", "E", "F", "G", "H"]}},
                {"children__patent__gkggr": {
                    "range": [date_block_start.strftime("%Y-%m-%d"), date_block_end.strftime("%Y-%m-%d")]}}
            ]
        }
        sort_dsl = {"gkggr": {"order": "desc"}}
        resp = api.patent_search(
            dsl_query=query_dsl,
            sort=sort_dsl,
            v_show=False,
            page_index="1"
        )
        total = resp.json()["result"]["total"]
        print(n, date_block_start, date_block_end, total)
        n += 1
        current = date_block_end


if __name__ == '__main__':
    client_id = sys.argv[1]
    client_key = sys.argv[2]
    print(client_id, "|", client_key)
    api = Saer(client_id, client_key)

    # test_search_query_dsl_gkggr_range(["1987-05-19", "1990-01-01"], 300, 60)
    test_search_query_dsl_gkggr_range_date_block()
    # print(len("00000071ba45f2bfb7f3488ae1ed8fa1"))
    # api.patent_detail("7c93aaf306ae966dcb2baa13e27d9b6e")
    # api.patent_detail("d3f524ac244a8368ba30af5e3404df1a")
    # api.patent_detail("00000071ba45f2bfb7f3488ae1ed8fa1")
#
