#
# Autogenerated by Thrift Compiler (0.9.2)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from enthrift.Thrift import TType, TMessageType, TException, TApplicationException
import evernote.edam.type.ttypes


from enthrift.transport import TTransport
from enthrift.protocol import TBinaryProtocol, TProtocol
try:
  from enthrift.protocol import fastbinary
except:
  fastbinary = None


class EDAMErrorCode:
  UNKNOWN = 1
  BAD_DATA_FORMAT = 2
  PERMISSION_DENIED = 3
  INTERNAL_ERROR = 4
  DATA_REQUIRED = 5
  LIMIT_REACHED = 6
  QUOTA_REACHED = 7
  INVALID_AUTH = 8
  AUTH_EXPIRED = 9
  DATA_CONFLICT = 10
  ENML_VALIDATION = 11
  SHARD_UNAVAILABLE = 12
  LEN_TOO_SHORT = 13
  LEN_TOO_LONG = 14
  TOO_FEW = 15
  TOO_MANY = 16
  UNSUPPORTED_OPERATION = 17
  TAKEN_DOWN = 18
  RATE_LIMIT_REACHED = 19
  BUSINESS_SECURITY_LOGIN_REQUIRED = 20

  _VALUES_TO_NAMES = {
    1: "UNKNOWN",
    2: "BAD_DATA_FORMAT",
    3: "PERMISSION_DENIED",
    4: "INTERNAL_ERROR",
    5: "DATA_REQUIRED",
    6: "LIMIT_REACHED",
    7: "QUOTA_REACHED",
    8: "INVALID_AUTH",
    9: "AUTH_EXPIRED",
    10: "DATA_CONFLICT",
    11: "ENML_VALIDATION",
    12: "SHARD_UNAVAILABLE",
    13: "LEN_TOO_SHORT",
    14: "LEN_TOO_LONG",
    15: "TOO_FEW",
    16: "TOO_MANY",
    17: "UNSUPPORTED_OPERATION",
    18: "TAKEN_DOWN",
    19: "RATE_LIMIT_REACHED",
    20: "BUSINESS_SECURITY_LOGIN_REQUIRED",
  }

  _NAMES_TO_VALUES = {
    "UNKNOWN": 1,
    "BAD_DATA_FORMAT": 2,
    "PERMISSION_DENIED": 3,
    "INTERNAL_ERROR": 4,
    "DATA_REQUIRED": 5,
    "LIMIT_REACHED": 6,
    "QUOTA_REACHED": 7,
    "INVALID_AUTH": 8,
    "AUTH_EXPIRED": 9,
    "DATA_CONFLICT": 10,
    "ENML_VALIDATION": 11,
    "SHARD_UNAVAILABLE": 12,
    "LEN_TOO_SHORT": 13,
    "LEN_TOO_LONG": 14,
    "TOO_FEW": 15,
    "TOO_MANY": 16,
    "UNSUPPORTED_OPERATION": 17,
    "TAKEN_DOWN": 18,
    "RATE_LIMIT_REACHED": 19,
    "BUSINESS_SECURITY_LOGIN_REQUIRED": 20,
  }

class EDAMInvalidContactReason:
  BAD_ADDRESS = 0
  DUPLICATE_CONTACT = 1
  NO_CONNECTION = 2

  _VALUES_TO_NAMES = {
    0: "BAD_ADDRESS",
    1: "DUPLICATE_CONTACT",
    2: "NO_CONNECTION",
  }

  _NAMES_TO_VALUES = {
    "BAD_ADDRESS": 0,
    "DUPLICATE_CONTACT": 1,
    "NO_CONNECTION": 2,
  }


class EDAMUserException(TException):
  """
  Attributes:
   - errorCode
   - parameter
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'errorCode', None, None, ), # 1
    (2, TType.STRING, 'parameter', None, None, ), # 2
  )

  def __init__(self, errorCode=None, parameter=None,):
    self.errorCode = errorCode
    self.parameter = parameter

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.errorCode = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.parameter = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('EDAMUserException')
    if self.errorCode is not None:
      oprot.writeFieldBegin('errorCode', TType.I32, 1)
      oprot.writeI32(self.errorCode)
      oprot.writeFieldEnd()
    if self.parameter is not None:
      oprot.writeFieldBegin('parameter', TType.STRING, 2)
      oprot.writeString(self.parameter)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.errorCode is None:
      raise TProtocol.TProtocolException(message='Required field errorCode is unset!')
    return


  def __str__(self):
    return repr(self)

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.errorCode)
    value = (value * 31) ^ hash(self.parameter)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class EDAMSystemException(TException):
  """
  Attributes:
   - errorCode
   - message
   - rateLimitDuration
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'errorCode', None, None, ), # 1
    (2, TType.STRING, 'message', None, None, ), # 2
    (3, TType.I32, 'rateLimitDuration', None, None, ), # 3
  )

  def __init__(self, errorCode=None, message=None, rateLimitDuration=None,):
    self.errorCode = errorCode
    self.message = message
    self.rateLimitDuration = rateLimitDuration

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.errorCode = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.message = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.rateLimitDuration = iprot.readI32();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('EDAMSystemException')
    if self.errorCode is not None:
      oprot.writeFieldBegin('errorCode', TType.I32, 1)
      oprot.writeI32(self.errorCode)
      oprot.writeFieldEnd()
    if self.message is not None:
      oprot.writeFieldBegin('message', TType.STRING, 2)
      oprot.writeString(self.message)
      oprot.writeFieldEnd()
    if self.rateLimitDuration is not None:
      oprot.writeFieldBegin('rateLimitDuration', TType.I32, 3)
      oprot.writeI32(self.rateLimitDuration)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.errorCode is None:
      raise TProtocol.TProtocolException(message='Required field errorCode is unset!')
    return


  def __str__(self):
    return repr(self)

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.errorCode)
    value = (value * 31) ^ hash(self.message)
    value = (value * 31) ^ hash(self.rateLimitDuration)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class EDAMNotFoundException(TException):
  """
  Attributes:
   - identifier
   - key
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'identifier', None, None, ), # 1
    (2, TType.STRING, 'key', None, None, ), # 2
  )

  def __init__(self, identifier=None, key=None,):
    self.identifier = identifier
    self.key = key

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.identifier = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.key = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('EDAMNotFoundException')
    if self.identifier is not None:
      oprot.writeFieldBegin('identifier', TType.STRING, 1)
      oprot.writeString(self.identifier)
      oprot.writeFieldEnd()
    if self.key is not None:
      oprot.writeFieldBegin('key', TType.STRING, 2)
      oprot.writeString(self.key)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __str__(self):
    return repr(self)

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.identifier)
    value = (value * 31) ^ hash(self.key)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class EDAMInvalidContactsException(TException):
  """
  Attributes:
   - contacts
   - parameter
   - reasons
  """

  thrift_spec = (
    None, # 0
    (1, TType.LIST, 'contacts', (TType.STRUCT,(evernote.edam.type.ttypes.Contact, evernote.edam.type.ttypes.Contact.thrift_spec)), None, ), # 1
    (2, TType.STRING, 'parameter', None, None, ), # 2
    (3, TType.LIST, 'reasons', (TType.I32,None), None, ), # 3
  )

  def __init__(self, contacts=None, parameter=None, reasons=None,):
    self.contacts = contacts
    self.parameter = parameter
    self.reasons = reasons

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.LIST:
          self.contacts = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = evernote.edam.type.ttypes.Contact()
            _elem5.read(iprot)
            self.contacts.append(_elem5)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.parameter = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.LIST:
          self.reasons = []
          (_etype9, _size6) = iprot.readListBegin()
          for _i10 in xrange(_size6):
            _elem11 = iprot.readI32();
            self.reasons.append(_elem11)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('EDAMInvalidContactsException')
    if self.contacts is not None:
      oprot.writeFieldBegin('contacts', TType.LIST, 1)
      oprot.writeListBegin(TType.STRUCT, len(self.contacts))
      for iter12 in self.contacts:
        iter12.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.parameter is not None:
      oprot.writeFieldBegin('parameter', TType.STRING, 2)
      oprot.writeString(self.parameter)
      oprot.writeFieldEnd()
    if self.reasons is not None:
      oprot.writeFieldBegin('reasons', TType.LIST, 3)
      oprot.writeListBegin(TType.I32, len(self.reasons))
      for iter13 in self.reasons:
        oprot.writeI32(iter13)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.contacts is None:
      raise TProtocol.TProtocolException(message='Required field contacts is unset!')
    return


  def __str__(self):
    return repr(self)

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.contacts)
    value = (value * 31) ^ hash(self.parameter)
    value = (value * 31) ^ hash(self.reasons)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
