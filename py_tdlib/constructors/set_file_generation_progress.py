from ..factory import Method


class setFileGenerationProgress(Method):
	generation_id = None  # type: "int64"
	expected_size = None  # type: "int32"
	local_prefix_size = None  # type: "int32"
