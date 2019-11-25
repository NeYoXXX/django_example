# import sys
# from django_redis import get_redis_connection
# from django.db.models.fields.related_descriptors import \
#     ForwardManyToOneDescriptor, ForwardOneToOneDescriptor, ReverseManyToOneDescriptor, ManyToManyDescriptor
#
# _final_list = (ForwardManyToOneDescriptor, ForwardOneToOneDescriptor, ReverseManyToOneDescriptor, ManyToManyDescriptor)
#
# class CacheBySerializers():
#     """
#     使用序列化类缓存数据
#     """
#     def __init__(self):
#         self.data_dict = dict()  # 存储的key类型为元祖，{model,{key,data}}
#         self.redis = get_redis_connection()
#
#     def get_data(self, serializer, key):
#         """
#         获取数据，若数据不存在则保存到缓存并返回序列化后数据
#         :param serializer:
#         :param key:
#         :return:
#         """
#         mod_key = serializer.Meta.model.__name__
#         mid_dic = self.data_dict.get(mod_key)
#         if mid_dic:
#             value = mid_dic.get(key)
#             if value:
#                 if value == "redis":
#                     key = serializer.Meta.model.__name__ + "@" + key
#                     value = self.redis.get(key)
#                 return value
#             else:
#                 data = serializer.data
#                 if sys.getsizeof(data) > 10000:
#                     mid_dic[key] = 'redis'
#                     # 存入redis
#                     self.data_dict[mod_key] = mid_dic
#                     key = serializer.Meta.model.__name__ + "@" + key
#                     is_ = self.redis.set(key, data, ex=7200 * 12)
#                 else:
#                     mid_dic[key] = data
#                     self.data_dict[mod_key] = mid_dic
#                 return data
#         else:
#             data = serializer.data
#             if sys.getsizeof(data) > 10000:
#                 self.data_dict[mod_key] = {key: "redis"}
#                 key = serializer.Meta.model.__name__ + "@" + key
#                 is_ = self.redis.set(key, data, ex=7200 * 12)
#             else:
#                 self.data_dict[mod_key] = {key: data}
#             return data
#
#     def del_data(self, serializer):
#         """
#         删除关联表的缓存数据
#         :param key:
#         :return:
#         """
#         model_list = self.__get_model_rela_att_tools(serializer.Meta.model)
#         for key in model_list:
#             is_ = self.data_dict.get(key)
#             if is_:
#                 try:
#                     redis_pip = self.redis.pipeline()
#                     for mid_key, value in is_.items():
#                         if value != "redis":
#                             re_key = key+"@"+mid_key
#                             redis_pip.delete(re_key)
#                     redis_pip.exceptions()
#                     self.data_dict.pop(key)
#                 except:
#                     print("删除出错")
#                     return False
#             else:
#                 # 若不存在返回true
#                 return True
#
#     def clear_all_cache(self):
#         """
#         清空所有数据表
#         :return:
#         """
#         for key in self.data_dict.keys():
#             is_ = self.data_dict.get(key)
#             if is_:
#                 try:
#                     redis_pip = self.redis.pipeline()
#                     for mid_key, value in is_.items():
#                         if value != "redis":
#                             re_key = key+"@"+mid_key
#                             redis_pip.delete(re_key)
#                     redis_pip.exceptions()
#                     self.data_dict.pop(key)
#                 except:
#                     print("删除出错")
#                     return False
#             else:
#                 # 若不存在返回true
#                 return True
#         # 删除本地数据
#         self.data_dict.clear()
#
#     def __get_model_rela_att_tools(self, model):
#         """
#         获取类有外键关联的属性
#         :param model:
#         :return:
#         """
#         data_list = list()
#         for att_name,att_value in vars(model):
#             if att_value in _final_list:
#                 data_list.append(att_value.field.name.capitalize())
#         return data_list
#
# serializers_cache = CacheBySerializers()










