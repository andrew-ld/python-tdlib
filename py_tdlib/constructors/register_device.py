from ..factory import Method


class registerDevice(Method):
	device_token = None  # type: "DeviceToken"
	other_user_ids = None  # type: "vector<int32>"
