# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/start_incident_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import enum_wrapper_pb2 as pogoprotos_dot_enums_dot_enum__wrapper__pb2
from pogoprotos.map.fort import fort_data_pb2 as pogoprotos_dot_map_dot_fort_dot_fort__data__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/start_incident_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_pb=_b('\n=pogoprotos/networking/responses/start_incident_response.proto\x12\x1fpogoprotos.networking.responses\x1a#pogoprotos/enums/enum_wrapper.proto\x1a#pogoprotos/map/fort/fort_data.proto\"\xc0\r\n\x15StartIncidentResponse\x12M\n\x06status\x18\x01 \x01(\x0e\x32=.pogoprotos.networking.responses.StartIncidentResponse.Status\x12W\n\x08incident\x18\x02 \x01(\x0b\x32\x45.pogoprotos.networking.responses.StartIncidentResponse.ClientIncident\x1a\xda\n\n\x0e\x43lientIncident\x12\x13\n\x0bincident_id\x18\x01 \x01(\t\x12\x0f\n\x07\x66ort_id\x18\x02 \x01(\t\x12\x11\n\tfort_name\x18\x03 \x01(\t\x12\x1a\n\x12pokestop_image_uri\x18\x04 \x01(\t\x12\x14\n\x0c\x63urrent_step\x18\x05 \x01(\x05\x12\x66\n\x04step\x18\x06 \x03(\x0b\x32X.pogoprotos.networking.responses.StartIncidentResponse.ClientIncident.ClientIncidentStep\x12Q\n\x12\x63ompletion_display\x18\x07 \x01(\x0b\x32\x35.pogoprotos.map.fort.FortData.PokestopIncidentDisplay\x12>\n\x07\x63ontext\x18\x08 \x01(\x0e\x32-.pogoprotos.enums.EnumWrapper.InvasionContext\x1a\xe1\x07\n\x12\x43lientIncidentStep\x12\x8c\x01\n\x0finvasion_battle\x18\x01 \x01(\x0b\x32q.pogoprotos.networking.responses.StartIncidentResponse.ClientIncident.ClientIncidentStep.ClientInvasionBattleStepH\x00\x12\x92\x01\n\x12invasion_encounter\x18\x02 \x01(\x0b\x32t.pogoprotos.networking.responses.StartIncidentResponse.ClientIncident.ClientIncidentStep.ClientInvasionEncounterStepH\x00\x12\x93\x01\n\x11pokestop_dialogue\x18\x03 \x01(\x0b\x32v.pogoprotos.networking.responses.StartIncidentResponse.ClientIncident.ClientIncidentStep.ClientPokestopNpcDialogueStepH\x00\x1a^\n\x18\x43lientInvasionBattleStep\x12\x42\n\tcharacter\x18\x01 \x01(\x0e\x32/.pogoprotos.enums.EnumWrapper.InvasionCharacter\x1a\x1d\n\x1b\x43lientInvasionEncounterStep\x1a\xfb\x02\n\x1d\x43lientPokestopNpcDialogueStep\x12\xa1\x01\n\rdialogue_line\x18\x01 \x03(\x0b\x32\x89\x01.pogoprotos.networking.responses.StartIncidentResponse.ClientIncident.ClientIncidentStep.ClientPokestopNpcDialogueStep.ClientDialogueLine\x1a\xb5\x01\n\x12\x43lientDialogueLine\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x42\n\tcharacter\x18\x02 \x01(\x0e\x32/.pogoprotos.enums.EnumWrapper.InvasionCharacter\x12M\n\nexpression\x18\x03 \x01(\x0e\x32\x39.pogoprotos.enums.EnumWrapper.InvasionCharacterExpressionB\x14\n\x12\x43lientIncidentStep\"\xa1\x01\n\x06Status\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x16\n\x12\x45RROR_NOT_IN_RANGE\x10\x02\x12\x1c\n\x18\x45RROR_INCIDENT_COMPLETED\x10\x03\x12\x1c\n\x18\x45RROR_INCIDENT_NOT_FOUND\x10\x04\x12 \n\x1c\x45RROR_PLAYER_BELOW_MIN_LEVEL\x10\x05\x12\t\n\x05\x45RROR\x10\x06\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_enum__wrapper__pb2.DESCRIPTOR,pogoprotos_dot_map_dot_fort_dot_fort__data__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_STARTINCIDENTRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='pogoprotos.networking.responses.StartIncidentResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_NOT_IN_RANGE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_INCIDENT_COMPLETED', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_INCIDENT_NOT_FOUND', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_PLAYER_BELOW_MIN_LEVEL', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=6, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1740,
  serialized_end=1901,
)
_sym_db.RegisterEnumDescriptor(_STARTINCIDENTRESPONSE_STATUS)


_STARTINCIDENTRESPONSE_CLIENTINCIDENT_CLIENTINCIDENTSTEP_CLIENTINVASIONBATTLESTEP = _descriptor.Descriptor(
  name='ClientInvasionBattleStep',
  full_name='pogoprotos.networking.responses.StartIncidentResponse.ClientIncident.ClientIncidentStep.ClientInvasionBattleStep',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='character', full_name='pogoprotos.networking.responses.StartIncidentResponse.ClientIncident.ClientIncidentStep.ClientInvasionBattleStep.character', index=0,
      number=1, type=14, cpp_type=8, label=1,
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
  serialized_start=1208,
  serialized_end=1302,
)

_STARTINCIDENTRESPONSE_CLIENTINCIDENT_CLIENTINCIDENTSTEP_CLIENTINVASIONENCOUNTERSTEP = _descriptor.Descriptor(
  name='ClientInvasionEncounterStep',
  full_name='pogoprotos.networking.responses.StartIncidentResponse.ClientIncident.ClientIncidentStep.ClientInvasionEncounterStep',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=1304,
  serialized_end=1333,
)

_STARTINCIDENTRESPONSE_CLIENTINCIDENT_CLIENTINCIDENTSTEP_CLIENTPOKESTOPNPCDIALOGUESTEP_CLIENTDIALOGUELINE = _descriptor.Descriptor(
  name='ClientDialogueLine',
  full_name='pogoprotos.networking.responses.StartIncidentResponse.ClientIncident.ClientIncidentStep.ClientPokestopNpcDialogueStep.ClientDialogueLine',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='pogoprotos.networking.responses.StartIncidentResponse.ClientIncident.ClientIncidentStep.ClientPokestopNpcDialogueStep.ClientDialogueLine.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='character', full_name='pogoprotos.networking.responses.StartIncidentResponse.ClientIncident.ClientIncidentStep.ClientPokestopNpcDialogueStep.ClientDialogueLine.character', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='expression', full_name='pogoprotos.networking.responses.StartIncidentResponse.ClientIncident.ClientIncidentStep.ClientPokestopNpcDialogueStep.ClientDialogueLine.expression', index=2,
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
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1534,
  serialized_end=1715,
)

_STARTINCIDENTRESPONSE_CLIENTINCIDENT_CLIENTINCIDENTSTEP_CLIENTPOKESTOPNPCDIALOGUESTEP = _descriptor.Descriptor(
  name='ClientPokestopNpcDialogueStep',
  full_name='pogoprotos.networking.responses.StartIncidentResponse.ClientIncident.ClientIncidentStep.ClientPokestopNpcDialogueStep',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dialogue_line', full_name='pogoprotos.networking.responses.StartIncidentResponse.ClientIncident.ClientIncidentStep.ClientPokestopNpcDialogueStep.dialogue_line', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_STARTINCIDENTRESPONSE_CLIENTINCIDENT_CLIENTINCIDENTSTEP_CLIENTPOKESTOPNPCDIALOGUESTEP_CLIENTDIALOGUELINE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1336,
  serialized_end=1715,
)

_STARTINCIDENTRESPONSE_CLIENTINCIDENT_CLIENTINCIDENTSTEP = _descriptor.Descriptor(
  name='ClientIncidentStep',
  full_name='pogoprotos.networking.responses.StartIncidentResponse.ClientIncident.ClientIncidentStep',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='invasion_battle', full_name='pogoprotos.networking.responses.StartIncidentResponse.ClientIncident.ClientIncidentStep.invasion_battle', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='invasion_encounter', full_name='pogoprotos.networking.responses.StartIncidentResponse.ClientIncident.ClientIncidentStep.invasion_encounter', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokestop_dialogue', full_name='pogoprotos.networking.responses.StartIncidentResponse.ClientIncident.ClientIncidentStep.pokestop_dialogue', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_STARTINCIDENTRESPONSE_CLIENTINCIDENT_CLIENTINCIDENTSTEP_CLIENTINVASIONBATTLESTEP, _STARTINCIDENTRESPONSE_CLIENTINCIDENT_CLIENTINCIDENTSTEP_CLIENTINVASIONENCOUNTERSTEP, _STARTINCIDENTRESPONSE_CLIENTINCIDENT_CLIENTINCIDENTSTEP_CLIENTPOKESTOPNPCDIALOGUESTEP, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='ClientIncidentStep', full_name='pogoprotos.networking.responses.StartIncidentResponse.ClientIncident.ClientIncidentStep.ClientIncidentStep',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=744,
  serialized_end=1737,
)

_STARTINCIDENTRESPONSE_CLIENTINCIDENT = _descriptor.Descriptor(
  name='ClientIncident',
  full_name='pogoprotos.networking.responses.StartIncidentResponse.ClientIncident',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='incident_id', full_name='pogoprotos.networking.responses.StartIncidentResponse.ClientIncident.incident_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fort_id', full_name='pogoprotos.networking.responses.StartIncidentResponse.ClientIncident.fort_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fort_name', full_name='pogoprotos.networking.responses.StartIncidentResponse.ClientIncident.fort_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokestop_image_uri', full_name='pogoprotos.networking.responses.StartIncidentResponse.ClientIncident.pokestop_image_uri', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='current_step', full_name='pogoprotos.networking.responses.StartIncidentResponse.ClientIncident.current_step', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='step', full_name='pogoprotos.networking.responses.StartIncidentResponse.ClientIncident.step', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='completion_display', full_name='pogoprotos.networking.responses.StartIncidentResponse.ClientIncident.completion_display', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='context', full_name='pogoprotos.networking.responses.StartIncidentResponse.ClientIncident.context', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_STARTINCIDENTRESPONSE_CLIENTINCIDENT_CLIENTINCIDENTSTEP, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=367,
  serialized_end=1737,
)

_STARTINCIDENTRESPONSE = _descriptor.Descriptor(
  name='StartIncidentResponse',
  full_name='pogoprotos.networking.responses.StartIncidentResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='pogoprotos.networking.responses.StartIncidentResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='incident', full_name='pogoprotos.networking.responses.StartIncidentResponse.incident', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_STARTINCIDENTRESPONSE_CLIENTINCIDENT, ],
  enum_types=[
    _STARTINCIDENTRESPONSE_STATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=173,
  serialized_end=1901,
)

_STARTINCIDENTRESPONSE_CLIENTINCIDENT_CLIENTINCIDENTSTEP_CLIENTINVASIONBATTLESTEP.fields_by_name['character'].enum_type = pogoprotos_dot_enums_dot_enum__wrapper__pb2._ENUMWRAPPER_INVASIONCHARACTER
_STARTINCIDENTRESPONSE_CLIENTINCIDENT_CLIENTINCIDENTSTEP_CLIENTINVASIONBATTLESTEP.containing_type = _STARTINCIDENTRESPONSE_CLIENTINCIDENT_CLIENTINCIDENTSTEP
_STARTINCIDENTRESPONSE_CLIENTINCIDENT_CLIENTINCIDENTSTEP_CLIENTINVASIONENCOUNTERSTEP.containing_type = _STARTINCIDENTRESPONSE_CLIENTINCIDENT_CLIENTINCIDENTSTEP
_STARTINCIDENTRESPONSE_CLIENTINCIDENT_CLIENTINCIDENTSTEP_CLIENTPOKESTOPNPCDIALOGUESTEP_CLIENTDIALOGUELINE.fields_by_name['character'].enum_type = pogoprotos_dot_enums_dot_enum__wrapper__pb2._ENUMWRAPPER_INVASIONCHARACTER
_STARTINCIDENTRESPONSE_CLIENTINCIDENT_CLIENTINCIDENTSTEP_CLIENTPOKESTOPNPCDIALOGUESTEP_CLIENTDIALOGUELINE.fields_by_name['expression'].enum_type = pogoprotos_dot_enums_dot_enum__wrapper__pb2._ENUMWRAPPER_INVASIONCHARACTEREXPRESSION
_STARTINCIDENTRESPONSE_CLIENTINCIDENT_CLIENTINCIDENTSTEP_CLIENTPOKESTOPNPCDIALOGUESTEP_CLIENTDIALOGUELINE.containing_type = _STARTINCIDENTRESPONSE_CLIENTINCIDENT_CLIENTINCIDENTSTEP_CLIENTPOKESTOPNPCDIALOGUESTEP
_STARTINCIDENTRESPONSE_CLIENTINCIDENT_CLIENTINCIDENTSTEP_CLIENTPOKESTOPNPCDIALOGUESTEP.fields_by_name['dialogue_line'].message_type = _STARTINCIDENTRESPONSE_CLIENTINCIDENT_CLIENTINCIDENTSTEP_CLIENTPOKESTOPNPCDIALOGUESTEP_CLIENTDIALOGUELINE
_STARTINCIDENTRESPONSE_CLIENTINCIDENT_CLIENTINCIDENTSTEP_CLIENTPOKESTOPNPCDIALOGUESTEP.containing_type = _STARTINCIDENTRESPONSE_CLIENTINCIDENT_CLIENTINCIDENTSTEP
_STARTINCIDENTRESPONSE_CLIENTINCIDENT_CLIENTINCIDENTSTEP.fields_by_name['invasion_battle'].message_type = _STARTINCIDENTRESPONSE_CLIENTINCIDENT_CLIENTINCIDENTSTEP_CLIENTINVASIONBATTLESTEP
_STARTINCIDENTRESPONSE_CLIENTINCIDENT_CLIENTINCIDENTSTEP.fields_by_name['invasion_encounter'].message_type = _STARTINCIDENTRESPONSE_CLIENTINCIDENT_CLIENTINCIDENTSTEP_CLIENTINVASIONENCOUNTERSTEP
_STARTINCIDENTRESPONSE_CLIENTINCIDENT_CLIENTINCIDENTSTEP.fields_by_name['pokestop_dialogue'].message_type = _STARTINCIDENTRESPONSE_CLIENTINCIDENT_CLIENTINCIDENTSTEP_CLIENTPOKESTOPNPCDIALOGUESTEP
_STARTINCIDENTRESPONSE_CLIENTINCIDENT_CLIENTINCIDENTSTEP.containing_type = _STARTINCIDENTRESPONSE_CLIENTINCIDENT
_STARTINCIDENTRESPONSE_CLIENTINCIDENT_CLIENTINCIDENTSTEP.oneofs_by_name['ClientIncidentStep'].fields.append(
  _STARTINCIDENTRESPONSE_CLIENTINCIDENT_CLIENTINCIDENTSTEP.fields_by_name['invasion_battle'])
_STARTINCIDENTRESPONSE_CLIENTINCIDENT_CLIENTINCIDENTSTEP.fields_by_name['invasion_battle'].containing_oneof = _STARTINCIDENTRESPONSE_CLIENTINCIDENT_CLIENTINCIDENTSTEP.oneofs_by_name['ClientIncidentStep']
_STARTINCIDENTRESPONSE_CLIENTINCIDENT_CLIENTINCIDENTSTEP.oneofs_by_name['ClientIncidentStep'].fields.append(
  _STARTINCIDENTRESPONSE_CLIENTINCIDENT_CLIENTINCIDENTSTEP.fields_by_name['invasion_encounter'])
_STARTINCIDENTRESPONSE_CLIENTINCIDENT_CLIENTINCIDENTSTEP.fields_by_name['invasion_encounter'].containing_oneof = _STARTINCIDENTRESPONSE_CLIENTINCIDENT_CLIENTINCIDENTSTEP.oneofs_by_name['ClientIncidentStep']
_STARTINCIDENTRESPONSE_CLIENTINCIDENT_CLIENTINCIDENTSTEP.oneofs_by_name['ClientIncidentStep'].fields.append(
  _STARTINCIDENTRESPONSE_CLIENTINCIDENT_CLIENTINCIDENTSTEP.fields_by_name['pokestop_dialogue'])
_STARTINCIDENTRESPONSE_CLIENTINCIDENT_CLIENTINCIDENTSTEP.fields_by_name['pokestop_dialogue'].containing_oneof = _STARTINCIDENTRESPONSE_CLIENTINCIDENT_CLIENTINCIDENTSTEP.oneofs_by_name['ClientIncidentStep']
_STARTINCIDENTRESPONSE_CLIENTINCIDENT.fields_by_name['step'].message_type = _STARTINCIDENTRESPONSE_CLIENTINCIDENT_CLIENTINCIDENTSTEP
_STARTINCIDENTRESPONSE_CLIENTINCIDENT.fields_by_name['completion_display'].message_type = pogoprotos_dot_map_dot_fort_dot_fort__data__pb2._FORTDATA_POKESTOPINCIDENTDISPLAY
_STARTINCIDENTRESPONSE_CLIENTINCIDENT.fields_by_name['context'].enum_type = pogoprotos_dot_enums_dot_enum__wrapper__pb2._ENUMWRAPPER_INVASIONCONTEXT
_STARTINCIDENTRESPONSE_CLIENTINCIDENT.containing_type = _STARTINCIDENTRESPONSE
_STARTINCIDENTRESPONSE.fields_by_name['status'].enum_type = _STARTINCIDENTRESPONSE_STATUS
_STARTINCIDENTRESPONSE.fields_by_name['incident'].message_type = _STARTINCIDENTRESPONSE_CLIENTINCIDENT
_STARTINCIDENTRESPONSE_STATUS.containing_type = _STARTINCIDENTRESPONSE
DESCRIPTOR.message_types_by_name['StartIncidentResponse'] = _STARTINCIDENTRESPONSE

StartIncidentResponse = _reflection.GeneratedProtocolMessageType('StartIncidentResponse', (_message.Message,), dict(

  ClientIncident = _reflection.GeneratedProtocolMessageType('ClientIncident', (_message.Message,), dict(

    ClientIncidentStep = _reflection.GeneratedProtocolMessageType('ClientIncidentStep', (_message.Message,), dict(

      ClientInvasionBattleStep = _reflection.GeneratedProtocolMessageType('ClientInvasionBattleStep', (_message.Message,), dict(
        DESCRIPTOR = _STARTINCIDENTRESPONSE_CLIENTINCIDENT_CLIENTINCIDENTSTEP_CLIENTINVASIONBATTLESTEP,
        __module__ = 'pogoprotos.networking.responses.start_incident_response_pb2'
        # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.StartIncidentResponse.ClientIncident.ClientIncidentStep.ClientInvasionBattleStep)
        ))
      ,

      ClientInvasionEncounterStep = _reflection.GeneratedProtocolMessageType('ClientInvasionEncounterStep', (_message.Message,), dict(
        DESCRIPTOR = _STARTINCIDENTRESPONSE_CLIENTINCIDENT_CLIENTINCIDENTSTEP_CLIENTINVASIONENCOUNTERSTEP,
        __module__ = 'pogoprotos.networking.responses.start_incident_response_pb2'
        # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.StartIncidentResponse.ClientIncident.ClientIncidentStep.ClientInvasionEncounterStep)
        ))
      ,

      ClientPokestopNpcDialogueStep = _reflection.GeneratedProtocolMessageType('ClientPokestopNpcDialogueStep', (_message.Message,), dict(

        ClientDialogueLine = _reflection.GeneratedProtocolMessageType('ClientDialogueLine', (_message.Message,), dict(
          DESCRIPTOR = _STARTINCIDENTRESPONSE_CLIENTINCIDENT_CLIENTINCIDENTSTEP_CLIENTPOKESTOPNPCDIALOGUESTEP_CLIENTDIALOGUELINE,
          __module__ = 'pogoprotos.networking.responses.start_incident_response_pb2'
          # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.StartIncidentResponse.ClientIncident.ClientIncidentStep.ClientPokestopNpcDialogueStep.ClientDialogueLine)
          ))
        ,
        DESCRIPTOR = _STARTINCIDENTRESPONSE_CLIENTINCIDENT_CLIENTINCIDENTSTEP_CLIENTPOKESTOPNPCDIALOGUESTEP,
        __module__ = 'pogoprotos.networking.responses.start_incident_response_pb2'
        # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.StartIncidentResponse.ClientIncident.ClientIncidentStep.ClientPokestopNpcDialogueStep)
        ))
      ,
      DESCRIPTOR = _STARTINCIDENTRESPONSE_CLIENTINCIDENT_CLIENTINCIDENTSTEP,
      __module__ = 'pogoprotos.networking.responses.start_incident_response_pb2'
      # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.StartIncidentResponse.ClientIncident.ClientIncidentStep)
      ))
    ,
    DESCRIPTOR = _STARTINCIDENTRESPONSE_CLIENTINCIDENT,
    __module__ = 'pogoprotos.networking.responses.start_incident_response_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.StartIncidentResponse.ClientIncident)
    ))
  ,
  DESCRIPTOR = _STARTINCIDENTRESPONSE,
  __module__ = 'pogoprotos.networking.responses.start_incident_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.StartIncidentResponse)
  ))
_sym_db.RegisterMessage(StartIncidentResponse)
_sym_db.RegisterMessage(StartIncidentResponse.ClientIncident)
_sym_db.RegisterMessage(StartIncidentResponse.ClientIncident.ClientIncidentStep)
_sym_db.RegisterMessage(StartIncidentResponse.ClientIncident.ClientIncidentStep.ClientInvasionBattleStep)
_sym_db.RegisterMessage(StartIncidentResponse.ClientIncident.ClientIncidentStep.ClientInvasionEncounterStep)
_sym_db.RegisterMessage(StartIncidentResponse.ClientIncident.ClientIncidentStep.ClientPokestopNpcDialogueStep)
_sym_db.RegisterMessage(StartIncidentResponse.ClientIncident.ClientIncidentStep.ClientPokestopNpcDialogueStep.ClientDialogueLine)


# @@protoc_insertion_point(module_scope)
