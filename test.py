import urllib.parse


#urlparse将url分为6个部分
url ="https://i.cnblogs.com/EditPosts.aspx?opt=1"
url_change = urllib.parse.urlparse(url) # 将url拆分为6个部分
query = url_change.query #取出拆分后6个部分中的查询模块query
lst_query = urllib.parse.parse_qsl(query)  #使用parse_qsl返回列表
dict1 =dict(lst_query)  #将返回的列表转换为字典
dict_query =urllib.parse.parse_qs(query)  #使用parse_qs返回字典
print(query)
print("使用parse_qsl返回列表  ：", lst_query)
print("将返回的列表转换为字典 ：", dict1)
print("使用parse_qs返回字典   : ", dict_query)