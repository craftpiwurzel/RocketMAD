# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/acknowledge_punishment_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/messages/acknowledge_punishment_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_pb=_b('\nLpogoprotos/networking/requests/messages/acknowledge_punishment_message.proto\x12\'pogoprotos.networking.requests.messages\"E\n\x1c\x41\x63knowledgePunishmentMessage\x12\x0f\n\x07is_warn\x18\x01 \x01(\x08\x12\x14\n\x0cis_suspended\x18\x02 \x01(\x08\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ACKNOWLEDGEPUNISHMENTMESSAGE = _descriptor.Descriptor(
  name='AcknowledgePunishmentMessage',
  full_name='pogoprotos.networking.requests.messages.AcknowledgePunishmentMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_warn', full_name='pogoprotos.networking.requests.messages.AcknowledgePunishmentMessage.is_warn', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_suspended', full_name='pogoprotos.networking.requests.messages.AcknowledgePunishmentMessage.is_suspended', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=121,
  serialized_end=190,
)

DESCRIPTOR.message_types_by_name['AcknowledgePunishmentMessage'] = _ACKNOWLEDGEPUNISHMENTMESSAGE

AcknowledgePunishmentMessage = _reflection.GeneratedProtocolMessageType('AcknowledgePunishmentMessage', (_message.Message,), dict(
  DESCRIPTOR = _ACKNOWLEDGEPUNISHMENTMESSAGE,
  __module__ = 'pogoprotos.networking.requests.messages.acknowledge_punishment_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.AcknowledgePunishmentMessage)
  ))
_sym_db.RegisterMessage(AcknowledgePunishmentMessage)


# @@protoc_insertion_point(module_scope)
