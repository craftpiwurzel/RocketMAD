# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/platform/responses/replace_login_action_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.login import login_detail_pb2 as pogoprotos_dot_data_dot_login_dot_login__detail__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/platform/responses/replace_login_action_response.proto',
  package='pogoprotos.networking.responses.platform.responses',
  syntax='proto3',
  serialized_pb=_b('\nVpogoprotos/networking/responses/platform/responses/replace_login_action_response.proto\x12\x32pogoprotos.networking.responses.platform.responses\x1a(pogoprotos/data/login/login_detail.proto\"\xb9\x02\n\x1aReplaceLoginActionResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x38\n\x0clogin_detail\x18\x02 \x03(\x0b\x32\".pogoprotos.data.login.LoginDetail\x12\x65\n\x06status\x18\x03 \x01(\x0e\x32U.pogoprotos.networking.responses.platform.responses.ReplaceLoginActionResponse.Status\"i\n\x06Status\x12\t\n\x05UNSET\x10\x00\x12\x10\n\x0c\x41UTH_FAILURE\x10\x01\x12\x0f\n\x0bLOGIN_TAKEN\x10\x02\x12\x16\n\x12LOGIN_ALREADY_HAVE\x10\x03\x12\x19\n\x15LOGIN_NOT_REPLACEABLE\x10\x04\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_login_dot_login__detail__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_REPLACELOGINACTIONRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='pogoprotos.networking.responses.platform.responses.ReplaceLoginActionResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_FAILURE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOGIN_TAKEN', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOGIN_ALREADY_HAVE', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOGIN_NOT_REPLACEABLE', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=393,
  serialized_end=498,
)
_sym_db.RegisterEnumDescriptor(_REPLACELOGINACTIONRESPONSE_STATUS)


_REPLACELOGINACTIONRESPONSE = _descriptor.Descriptor(
  name='ReplaceLoginActionResponse',
  full_name='pogoprotos.networking.responses.platform.responses.ReplaceLoginActionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='pogoprotos.networking.responses.platform.responses.ReplaceLoginActionResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='login_detail', full_name='pogoprotos.networking.responses.platform.responses.ReplaceLoginActionResponse.login_detail', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='pogoprotos.networking.responses.platform.responses.ReplaceLoginActionResponse.status', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REPLACELOGINACTIONRESPONSE_STATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=185,
  serialized_end=498,
)

_REPLACELOGINACTIONRESPONSE.fields_by_name['login_detail'].message_type = pogoprotos_dot_data_dot_login_dot_login__detail__pb2._LOGINDETAIL
_REPLACELOGINACTIONRESPONSE.fields_by_name['status'].enum_type = _REPLACELOGINACTIONRESPONSE_STATUS
_REPLACELOGINACTIONRESPONSE_STATUS.containing_type = _REPLACELOGINACTIONRESPONSE
DESCRIPTOR.message_types_by_name['ReplaceLoginActionResponse'] = _REPLACELOGINACTIONRESPONSE

ReplaceLoginActionResponse = _reflection.GeneratedProtocolMessageType('ReplaceLoginActionResponse', (_message.Message,), dict(
  DESCRIPTOR = _REPLACELOGINACTIONRESPONSE,
  __module__ = 'pogoprotos.networking.responses.platform.responses.replace_login_action_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.platform.responses.ReplaceLoginActionResponse)
  ))
_sym_db.RegisterMessage(ReplaceLoginActionResponse)


# @@protoc_insertion_point(module_scope)
