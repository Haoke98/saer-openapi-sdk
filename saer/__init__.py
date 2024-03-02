# _*_ codign:utf8 _*_
"""====================================
@Author:Sadam·Sadik
@Email：1903249375@qq.com
@Date：2023/6/13
@Software: PyCharm
@disc:
======================================="""
import hashlib
import json
import time

import requests


class Saer:
    client_id = ""
    client_key = ""
    # base_url = "http://47.93.35.233/openapi"
    base_url = "http://openapi.isaerdata.com/openapi"

    def __init__(self, client_id, client_key):
        self.client_id = client_id
        self.client_key = client_key

    def gen_auth_token(self, client_id, client_key, v_show: bool = False):
        unix_timestamp = int(time.time())
        raw_string = "{}-{}-{}".format(client_id, unix_timestamp, client_key)
        md5_hash = hashlib.md5(raw_string.encode('utf-8'))
        md5_hex = md5_hash.hexdigest()
        if v_show:
            print('AUTHORIZATION,string,true,{},Md5(clientid-Timespan-clientkey)'.format(md5_hex.upper()))
            print("TIMESPAN,string,true,{},Unix时间戳".format(unix_timestamp))
            print("CLIENTID,string,true,{},Clientid(个人中心可以查看)".format(client_id))
            print("----------------------------------")
            print('AUTHORIZATION:{}'.format(md5_hex.upper()))
            print("TIMESPAN:{}".format(unix_timestamp))
            print("CLIENTID:{}".format(client_id))
        return md5_hex.upper(), unix_timestamp

    def __post__(self, url, data, v_show: bool = True):
        token, timespan = self.gen_auth_token(self.client_id, self.client_key)
        _headers = {
            "AUTHORIZATION": token,
            "TIMESPAN": str(timespan),
            "CLIENTID": self.client_id,
        }
        final_url = "{}{}".format(self.base_url, url)
        if v_show:
            print("URL:{}".format(final_url))
            print("Headers:", json.dumps(_headers, ensure_ascii=False, indent=4))
            print("Data:", json.dumps(data, ensure_ascii=False, indent=4))
        resp = requests.post(url=final_url, headers=_headers, data=data)
        if v_show:
            print("Response:", resp)
        respDict = resp.json()
        code = respDict["code"]
        if code == "200":
            if v_show:
                print("ResponseDict:", json.dumps(respDict, ensure_ascii=False, indent=4), respDict)
            pass
        else:
            print("ResponseDict:", json.dumps(respDict, ensure_ascii=False, indent=4))
        return resp

    def detail(self, key: str, key_type: str, version):
        qdata = {
            "key": key,
            "key_type": key_type,
            "version": version,
        }
        return self.__post__("/common/company_detail/", qdata)

    def get_entid(self, key, key_type):
        return self.__post__("/common/get_entid/", {
            "key": key,
            "key_type": key_type
        })

    def search(self,
               dsl={"dsl_query": {"must": [{"main__ENTNAME": {"any": ["小米科技有限责任公司", "华为技术有限公司"]}}]}}):
        qdata = {"data": json.dumps(dsl, ensure_ascii=False)}
        return self.__post__(url="/common/mohu/", data=qdata)

    def contact(self, key: str, key_type: str, ltype=None, v_show: bool = False):
        """

        :param key:搜索关键字
        :param key_type:搜索关键字类型（"0"：企业唯一标识；"1"：企业名称；"2"：统一社会信用代码；"3"：注册号），若为"0"该参数可不传
        :param ltype:("1", "手机"), ("2", "座机"), ("3", "邮箱")
        """
        qdata = {
            "key": key,
            "key_type": key_type
        }
        if ltype is not None:
            qdata.setdefault("ltype", ltype)
        resp = self.__post__("/common/company_lianxi_public/", data=qdata)
        return resp

    def all(self, company_name: str):
        self.detail(company_name, "1", "A1")
        self.detail(company_name, "1", "A2")
        self.detail(company_name, "1", "A3")
        self.detail(company_name, "1", "A4")
        self.detail(company_name, "1", "B1")
        self.detail(company_name, "1", "B2")
        self.detail(company_name, "1", "B3")
        self.detail(company_name, "1", "B4")
        self.contact(company_name, "1")

    def patent_search(self, dsl_query, sort, page_index: str = "1", page_size: str = "20", v_show=True):
        data = {
            "dsl_query": dsl_query,
            "sort": sort,
            "page_index": page_index,
            "page_size": page_size
        }
        qdata = {"data": json.dumps(data, ensure_ascii=False)}
        return self.__post__(url="/common/patent_search/", data=qdata, v_show=v_show)

    def patent_detail(self, mid: str, v_show=True):
        data = {
            "mid": mid
        }
        return self.__post__(url="/common/patent_details/", data=data, v_show=v_show)
