#!/user/bin/env python
# coding=utf-8
'''
# 创 建 人: 李先生
# 文 件 名: error_code.py
# 说   明: 
# 创建时间: 2019/7/10 21:43
'''


class ErrorCode:
    """
    处理接口请求返回中的异常情况
    """
    interface_error = '系统异常，检查接口参数是否正确！'

    index_error = 'list索引错误，提取参数设置长度超出！'

    validators_error = '接口未设置检查点！'

    case_not_exit_error = '执行用例不存在！'

    env_not_exit_error = '测试环境不存在！'

    interface_not_exit_error = '执行接口不存在！'

    user_not_logged_in_error = '用户未登录！！！'

    requests_error = '接口请求异常，检查请求接口代码是否正确！'

    mock_fail = '模拟接口返回值进行断言，实际未请求！'

    empty_error = '字段不能为空！'

    fields_too_long_error = '输入字段过长！'

    not_enough_error = '输入字段长度不够！'

    different_error = '两次输入的密码不一致！'

    format_error = 'email格式错误！'

    already_exists_error = '注册用户已经存在！'

    AES_key_length_error = 'app_key长度必须是16、24或者32位！'

    random_params_error = '参数化设置错误，不符合关键字设置规则！'
