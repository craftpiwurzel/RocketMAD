# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/battle/battle.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.battle import battle_participant_pb2 as pogoprotos_dot_data_dot_battle_dot_battle__participant__pb2
from pogoprotos.data.battle import battle_log_pb2 as pogoprotos_dot_data_dot_battle_dot_battle__log__pb2
from pogoprotos.enums import weather_condition_pb2 as pogoprotos_dot_enums_dot_weather__condition__pb2
from pogoprotos.enums import friendship_level_milestone_pb2 as pogoprotos_dot_enums_dot_friendship__level__milestone__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/battle/battle.proto',
  package='pogoprotos.data.battle',
  syntax='proto3',
  serialized_pb=_b('\n#pogoprotos/data/battle/battle.proto\x12\x16pogoprotos.data.battle\x1a/pogoprotos/data/battle/battle_participant.proto\x1a\'pogoprotos/data/battle/battle_log.proto\x1a(pogoprotos/enums/weather_condition.proto\x1a\x31pogoprotos/enums/friendship_level_milestone.proto\"\x8d\x03\n\x06\x42\x61ttle\x12\x17\n\x0f\x62\x61ttle_start_ms\x18\x01 \x01(\x03\x12\x15\n\rbattle_end_ms\x18\x02 \x01(\x03\x12\x11\n\tbattle_id\x18\x03 \x01(\t\x12;\n\x08\x64\x65\x66\x65nder\x18\x04 \x01(\x0b\x32).pogoprotos.data.battle.BattleParticipant\x12\x35\n\nbattle_log\x18\x05 \x01(\x0b\x32!.pogoprotos.data.battle.BattleLog\x12;\n\x08\x61ttacker\x18\x06 \x01(\x0b\x32).pogoprotos.data.battle.BattleParticipant\x12=\n\x11weather_condition\x18\x07 \x01(\x0e\x32\".pogoprotos.enums.WeatherCondition\x12P\n\x1chighest_friendship_milestone\x18\x08 \x01(\x0e\x32*.pogoprotos.enums.FriendshipLevelMilestoneb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_battle_dot_battle__participant__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_battle_dot_battle__log__pb2.DESCRIPTOR,pogoprotos_dot_enums_dot_weather__condition__pb2.DESCRIPTOR,pogoprotos_dot_enums_dot_friendship__level__milestone__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_BATTLE = _descriptor.Descriptor(
  name='Battle',
  full_name='pogoprotos.data.battle.Battle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='battle_start_ms', full_name='pogoprotos.data.battle.Battle.battle_start_ms', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battle_end_ms', full_name='pogoprotos.data.battle.Battle.battle_end_ms', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battle_id', full_name='pogoprotos.data.battle.Battle.battle_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='defender', full_name='pogoprotos.data.battle.Battle.defender', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battle_log', full_name='pogoprotos.data.battle.Battle.battle_log', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attacker', full_name='pogoprotos.data.battle.Battle.attacker', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='weather_condition', full_name='pogoprotos.data.battle.Battle.weather_condition', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='highest_friendship_milestone', full_name='pogoprotos.data.battle.Battle.highest_friendship_milestone', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=247,
  serialized_end=644,
)

_BATTLE.fields_by_name['defender'].message_type = pogoprotos_dot_data_dot_battle_dot_battle__participant__pb2._BATTLEPARTICIPANT
_BATTLE.fields_by_name['battle_log'].message_type = pogoprotos_dot_data_dot_battle_dot_battle__log__pb2._BATTLELOG
_BATTLE.fields_by_name['attacker'].message_type = pogoprotos_dot_data_dot_battle_dot_battle__participant__pb2._BATTLEPARTICIPANT
_BATTLE.fields_by_name['weather_condition'].enum_type = pogoprotos_dot_enums_dot_weather__condition__pb2._WEATHERCONDITION
_BATTLE.fields_by_name['highest_friendship_milestone'].enum_type = pogoprotos_dot_enums_dot_friendship__level__milestone__pb2._FRIENDSHIPLEVELMILESTONE
DESCRIPTOR.message_types_by_name['Battle'] = _BATTLE

Battle = _reflection.GeneratedProtocolMessageType('Battle', (_message.Message,), dict(
  DESCRIPTOR = _BATTLE,
  __module__ = 'pogoprotos.data.battle.battle_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.battle.Battle)
  ))
_sym_db.RegisterMessage(Battle)


# @@protoc_insertion_point(module_scope)
