
from typing import Optional


class MessageType(Enum):
    Initialize = 0
    InitializeResponse = 1
    FatalError = 2
    Error = 3
    AsyncLock = 4
    AsyncLockResponse = 5
    Data = 6
    DataEnd = 7
    DeviceClearComplete = 8
    DeviceClearAcknowledge = 9
    AsyncRemoteLocalControl = 10
    AsyncRemoteLocalResponse = 11
    Trigger = 12
    Interrupted = 13
    AsyncInterrupted = 14
    AsyncMaximumMessageSize = 15
    AsyncMaximumMessageSizeResponse = 16
    AsyncInitialize = 17
    AsyncInitializeResponse = 18
    AsyncDeviceClear = 19
    AsyncServiceRequest = 20
    AsyncStatusQuery = 21
    AsyncStatusResponse = 22
    AsyncDeviceClearAcknowledge = 23
    AsyncLockInfo = 24
    AsyncLockInfoResponse = 25
    GetDescriptors = 26
    GetDescriptorsResponse = 27
    StartTLS = 28
    AsyncStartTLS = 29
    AsyncStartTLSResponse = 30
    EndTLS = 31
    AsyncEndTLS = 32,
    AsyncEndTLSResponse = 33,
    GetSaslMechanismList = 34,
    GetSalsMechanismListResponse = 35
    AuthenticationStart = 36
    AuthenticationExchange = 37
    AuthenticationResult = 38


class Message(object):
    def __init__(self, type: MessageType, control_code: int = 0, parameter: int = 0, payload: Optional[bytes] = None) -> None:
        super().__init__()
        self.control_code = control_code
        self.parameter = parameter
        self.payload = payload

    
    





