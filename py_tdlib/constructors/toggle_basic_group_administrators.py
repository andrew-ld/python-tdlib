from ..factory import Method


class toggleBasicGroupAdministrators(Method):
	basic_group_id = None  # type: "int32"
	everyone_is_administrator = None  # type: "Bool"
