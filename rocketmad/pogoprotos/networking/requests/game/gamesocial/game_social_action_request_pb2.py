# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/game/gamesocial/game_social_action_request.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.networking.requests.game.gamesocial import game_social_action_pb2 as pogoprotos_dot_networking_dot_requests_dot_game_dot_gamesocial_dot_game__social__action__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/game/gamesocial/game_social_action_request.proto',
  package='pogoprotos.networking.requests.game.gamesocial',
  syntax='proto3',
  serialized_pb=_b('\nOpogoprotos/networking/requests/game/gamesocial/game_social_action_request.proto\x12.pogoprotos.networking.requests.game.gamesocial\x1aGpogoprotos/networking/requests/game/gamesocial/game_social_action.proto\"\x8a\x01\n\x17GameSocialActionRequest\x12V\n\x0crequest_type\x18\x01 \x01(\x0e\x32@.pogoprotos.networking.requests.game.gamesocial.GameSocialAction\x12\x17\n\x0frequest_message\x18\x02 \x01(\x0c\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_networking_dot_requests_dot_game_dot_gamesocial_dot_game__social__action__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_GAMESOCIALACTIONREQUEST = _descriptor.Descriptor(
  name='GameSocialActionRequest',
  full_name='pogoprotos.networking.requests.game.gamesocial.GameSocialActionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_type', full_name='pogoprotos.networking.requests.game.gamesocial.GameSocialActionRequest.request_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='request_message', full_name='pogoprotos.networking.requests.game.gamesocial.GameSocialActionRequest.request_message', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=205,
  serialized_end=343,
)

_GAMESOCIALACTIONREQUEST.fields_by_name['request_type'].enum_type = pogoprotos_dot_networking_dot_requests_dot_game_dot_gamesocial_dot_game__social__action__pb2._GAMESOCIALACTION
DESCRIPTOR.message_types_by_name['GameSocialActionRequest'] = _GAMESOCIALACTIONREQUEST

GameSocialActionRequest = _reflection.GeneratedProtocolMessageType('GameSocialActionRequest', (_message.Message,), dict(
  DESCRIPTOR = _GAMESOCIALACTIONREQUEST,
  __module__ = 'pogoprotos.networking.requests.game.gamesocial.game_social_action_request_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.game.gamesocial.GameSocialActionRequest)
  ))
_sym_db.RegisterMessage(GameSocialActionRequest)


# @@protoc_insertion_point(module_scope)
