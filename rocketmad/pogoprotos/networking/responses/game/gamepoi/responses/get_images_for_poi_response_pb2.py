# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/game/gamepoi/responses/get_images_for_poi_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/game/gamepoi/responses/get_images_for_poi_response.proto',
  package='pogoprotos.networking.responses.game.gamepoi.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nXpogoprotos/networking/responses/game/gamepoi/responses/get_images_for_poi_response.proto\x12\x36pogoprotos.networking.responses.game.gamepoi.responses\"\xa8\x04\n\x17GetImagesForPoiResponse\x12\x66\n\x06status\x18\x01 \x01(\x0e\x32V.pogoprotos.networking.responses.game.gamepoi.responses.GetImagesForPoiResponse.Status\x12\x90\x01\n\x18photo_gallery_poi_images\x18\x02 \x03(\x0b\x32n.pogoprotos.networking.responses.game.gamepoi.responses.GetImagesForPoiResponse.GameClientPhotoGalleryPoiImage\x1a\xc7\x01\n\x1eGameClientPhotoGalleryPoiImage\x12\x10\n\x08image_id\x18\x01 \x01(\t\x12\x0e\n\x06poi_id\x18\x02 \x01(\t\x12\x1a\n\x12submitter_codename\x18\x03 \x01(\t\x12\x11\n\timage_url\x18\x04 \x01(\t\x12\x1d\n\x15\x63reation_timestamp_ms\x18\x05 \x01(\x03\x12\x18\n\x10has_player_voted\x18\x06 \x01(\x08\x12\x1b\n\x13num_votes_from_game\x18\x07 \x01(\x05\"H\n\x06Status\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x11\n\rPOI_NOT_FOUND\x10\x02\x12\x13\n\x0fINVALID_REQUEST\x10\x03\x62\x06proto3')
)



_GETIMAGESFORPOIRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='pogoprotos.networking.responses.game.gamepoi.responses.GetImagesForPoiResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POI_NOT_FOUND', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_REQUEST', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=629,
  serialized_end=701,
)
_sym_db.RegisterEnumDescriptor(_GETIMAGESFORPOIRESPONSE_STATUS)


_GETIMAGESFORPOIRESPONSE_GAMECLIENTPHOTOGALLERYPOIIMAGE = _descriptor.Descriptor(
  name='GameClientPhotoGalleryPoiImage',
  full_name='pogoprotos.networking.responses.game.gamepoi.responses.GetImagesForPoiResponse.GameClientPhotoGalleryPoiImage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='image_id', full_name='pogoprotos.networking.responses.game.gamepoi.responses.GetImagesForPoiResponse.GameClientPhotoGalleryPoiImage.image_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='poi_id', full_name='pogoprotos.networking.responses.game.gamepoi.responses.GetImagesForPoiResponse.GameClientPhotoGalleryPoiImage.poi_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='submitter_codename', full_name='pogoprotos.networking.responses.game.gamepoi.responses.GetImagesForPoiResponse.GameClientPhotoGalleryPoiImage.submitter_codename', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='image_url', full_name='pogoprotos.networking.responses.game.gamepoi.responses.GetImagesForPoiResponse.GameClientPhotoGalleryPoiImage.image_url', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creation_timestamp_ms', full_name='pogoprotos.networking.responses.game.gamepoi.responses.GetImagesForPoiResponse.GameClientPhotoGalleryPoiImage.creation_timestamp_ms', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='has_player_voted', full_name='pogoprotos.networking.responses.game.gamepoi.responses.GetImagesForPoiResponse.GameClientPhotoGalleryPoiImage.has_player_voted', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_votes_from_game', full_name='pogoprotos.networking.responses.game.gamepoi.responses.GetImagesForPoiResponse.GameClientPhotoGalleryPoiImage.num_votes_from_game', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=428,
  serialized_end=627,
)

_GETIMAGESFORPOIRESPONSE = _descriptor.Descriptor(
  name='GetImagesForPoiResponse',
  full_name='pogoprotos.networking.responses.game.gamepoi.responses.GetImagesForPoiResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='pogoprotos.networking.responses.game.gamepoi.responses.GetImagesForPoiResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='photo_gallery_poi_images', full_name='pogoprotos.networking.responses.game.gamepoi.responses.GetImagesForPoiResponse.photo_gallery_poi_images', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GETIMAGESFORPOIRESPONSE_GAMECLIENTPHOTOGALLERYPOIIMAGE, ],
  enum_types=[
    _GETIMAGESFORPOIRESPONSE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=149,
  serialized_end=701,
)

_GETIMAGESFORPOIRESPONSE_GAMECLIENTPHOTOGALLERYPOIIMAGE.containing_type = _GETIMAGESFORPOIRESPONSE
_GETIMAGESFORPOIRESPONSE.fields_by_name['status'].enum_type = _GETIMAGESFORPOIRESPONSE_STATUS
_GETIMAGESFORPOIRESPONSE.fields_by_name['photo_gallery_poi_images'].message_type = _GETIMAGESFORPOIRESPONSE_GAMECLIENTPHOTOGALLERYPOIIMAGE
_GETIMAGESFORPOIRESPONSE_STATUS.containing_type = _GETIMAGESFORPOIRESPONSE
DESCRIPTOR.message_types_by_name['GetImagesForPoiResponse'] = _GETIMAGESFORPOIRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetImagesForPoiResponse = _reflection.GeneratedProtocolMessageType('GetImagesForPoiResponse', (_message.Message,), dict(

  GameClientPhotoGalleryPoiImage = _reflection.GeneratedProtocolMessageType('GameClientPhotoGalleryPoiImage', (_message.Message,), dict(
    DESCRIPTOR = _GETIMAGESFORPOIRESPONSE_GAMECLIENTPHOTOGALLERYPOIIMAGE,
    __module__ = 'pogoprotos.networking.responses.game.gamepoi.responses.get_images_for_poi_response_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.game.gamepoi.responses.GetImagesForPoiResponse.GameClientPhotoGalleryPoiImage)
    ))
  ,
  DESCRIPTOR = _GETIMAGESFORPOIRESPONSE,
  __module__ = 'pogoprotos.networking.responses.game.gamepoi.responses.get_images_for_poi_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.game.gamepoi.responses.GetImagesForPoiResponse)
  ))
_sym_db.RegisterMessage(GetImagesForPoiResponse)
_sym_db.RegisterMessage(GetImagesForPoiResponse.GameClientPhotoGalleryPoiImage)


# @@protoc_insertion_point(module_scope)