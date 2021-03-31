def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    user_info['first_name'] = first
    user_info['last_nmae'] = last
    return user_info

user_profile = build_profile('zhang', 'fuhong', location='shanghai', 
                            field='computer', age=26)

print(user_profile)