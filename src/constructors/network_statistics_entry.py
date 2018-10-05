from ..factory import Type


class networkStatisticsEntryFile(Type):
    #  information about the total amount of data that was
    #  to send and receive files @file_type Type of the
    #  the data is part of @network_type Type of the
    #  the data was sent through. Call setNetworkType to maintain
    #  actual network type

    file_type = None  # type: "FileType"
    network_type = None  # type: "NetworkType"
    sent_bytes = None  # type: "int53"
    received_bytes = None  # type: "int53"


class networkStatisticsEntryCall(Type):
    #  information about the total amount of data that was
    #  for calls @network_type Type of the network the data
    #  sent through. Call setNetworkType to maintain the actual network

    network_type = None  # type: "NetworkType"
    sent_bytes = None  # type: "int53"
    received_bytes = None  # type: "int53"
    duration = None  # type: "double"
