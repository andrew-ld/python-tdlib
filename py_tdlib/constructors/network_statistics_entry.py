from ..factory import Type


class networkStatisticsEntryFile(Type):
    # Contains information about the total amount of data that was
    # used to send and receive files, @file_type Type of the
    # file the data is part of, @network_type Type of the
    # network the data was sent through. Call setNetworkType to maintain
    # the actual network type

    file_type = None  # type: "FileType"
    network_type = None  # type: "NetworkType"
    sent_bytes = None  # type: "int53"
    received_bytes = None  # type: "int53"


class networkStatisticsEntryCall(Type):
    # Contains information about the total amount of data that was
    # used for calls, @network_type Type of the network the data
    # was sent through. Call setNetworkType to maintain the actual network type

    network_type = None  # type: "NetworkType"
    sent_bytes = None  # type: "int53"
    received_bytes = None  # type: "int53"
    duration = None  # type: "double"
