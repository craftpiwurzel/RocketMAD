# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/notification_category.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/enums/notification_category.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_pb=_b('\n,pogoprotos/enums/notification_category.proto\x12\x10pogoprotos.enums*\xfb\n\n\x14NotificationCategory\x12\x1f\n\x1bUNSET_NOTIFICATION_CATEGORY\x10\x00\x12\x0f\n\x0bGYM_REMOVAL\x10\x01\x12\x12\n\x0ePOKEMON_HUNGRY\x10\x02\x12\x0f\n\x0bPOKEMON_WON\x10\x03\x12\x19\n\x15\x45XCLUSIVE_RAID_INVITE\x10\x04\x12\x1f\n\x1b\x45XCLUSIVE_RAID_CANCELLATION\x10\x05\x12\x14\n\x10GIFTBOX_INCOMING\x10\x06\x12\x15\n\x11GIFTBOX_DELIVERED\x10\x07\x12\x1f\n\x1b\x46RIENDSHIP_MILESTONE_REWARD\x10\x08\x12#\n\x1fGYM_BATTLE_FRIENDSHIP_INCREMENT\x10\t\x12 \n\x1cSHARED_EXCLUSIVE_RAID_INVITE\x10\n\x12\x14\n\x10\x42GMODE_EGG_HATCH\x10\x0b\x12\x16\n\x12\x42GMODE_BUDDY_CANDY\x10\x0c\x12 \n\x1c\x42GMODE_WEEKLY_FITNESS_REPORT\x10\r\x12\x1b\n\x17\x43OMBAT_CHALLENGE_OPENED\x10\x0e\x12\x1f\n\x1b\x42GMODE_OFF_SESSION_DISTANCE\x10\x0f\x12\x18\n\x14\x42GMODE_POI_PROXIMITY\x10\x10\x12\x10\n\x0cLUCKY_FRIEND\x10\x11\x12\x1c\n\x18\x42GMODE_NAMED_BUDDY_CANDY\x10\x12\x12\x12\n\x0e\x41PP_BADGE_ONLY\x10\x13\x12\x1c\n\x18\x43OMBAT_VS_SEEKER_CHARGED\x10\x14\x12!\n\x1d\x43OMBAT_COMPETITIVE_SEASON_END\x10\x15\x12\x10\n\x0c\x42UDDY_HUNGRY\x10\x16\x12\x14\n\x10\x42UDDY_FOUND_GIFT\x10\x18\x12#\n\x1f\x42UDDY_AFFECTION_LEVEL_MILESTONE\x10\x19\x12\x1b\n\x17\x42UDDY_AFFECTION_WALKING\x10\x1a\x12\x18\n\x14\x42UDDY_AFFECTION_CARE\x10\x1b\x12\x1a\n\x16\x42UDDY_AFFECTION_BATTLE\x10\x1c\x12\x19\n\x15\x42UDDY_AFFECTION_PHOTO\x10\x1d\x12\x17\n\x13\x42UDDY_AFFECTION_POI\x10\x1e\x12\x1b\n\x17\x42GMODE_BUDDY_FOUND_GIFT\x10\x1f\x12\x18\n\x14\x42UDDY_ATTRACTIVE_POI\x10 \x12\x1f\n\x1b\x42GMODE_BUDDY_ATTRACTIVE_POI\x10!\x12\"\n\x1e\x42UDDY_AFFECTION_ATTRACTIVE_POI\x10$\x12\x19\n\x15POI_PASSCODE_REDEEMED\x10%\x12\x16\n\x12NO_EGGS_INCUBATING\x10&\x12\x1c\n\x18RETENTION_UNOPENED_GIFTS\x10\'\x12\x17\n\x13RETENTION_STARPIECE\x10(\x12\x15\n\x11RETENTION_INCENSE\x10)\x12\x17\n\x13RETENTION_LUCKY_EGG\x10*\x12\x1d\n\x19RETENTION_ADVSYNC_REWARDS\x10+\x12!\n\x1dRETENTION_EGGS_NOT_INCUBATING\x10,\x12\x18\n\x14RETENTION_POWER_WALK\x10-\x12\x1e\n\x1aRETENTION_FUN_WITH_FRIENDS\x10.\x12\x15\n\x11\x42UDDY_REMOTE_GIFT\x10/\x12\x1c\n\x18\x42GMODE_BUDDY_REMOTE_GIFT\x10\x30\x12\x1a\n\x16REMOTE_RAID_INVITATION\x10\x31\x12\x10\n\x0cITEM_REWARDS\x10\x32\x12!\n\x1dTIMED_GROUP_CHALLENGE_STARTED\x10\x33\x12\"\n\x1eTIMED_GROUP_CHALLENGE_GOAL_MET\x10\x34\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_NOTIFICATIONCATEGORY = _descriptor.EnumDescriptor(
  name='NotificationCategory',
  full_name='pogoprotos.enums.NotificationCategory',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET_NOTIFICATION_CATEGORY', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GYM_REMOVAL', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKEMON_HUNGRY', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKEMON_WON', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXCLUSIVE_RAID_INVITE', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXCLUSIVE_RAID_CANCELLATION', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GIFTBOX_INCOMING', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GIFTBOX_DELIVERED', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FRIENDSHIP_MILESTONE_REWARD', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GYM_BATTLE_FRIENDSHIP_INCREMENT', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHARED_EXCLUSIVE_RAID_INVITE', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BGMODE_EGG_HATCH', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BGMODE_BUDDY_CANDY', index=12, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BGMODE_WEEKLY_FITNESS_REPORT', index=13, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMBAT_CHALLENGE_OPENED', index=14, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BGMODE_OFF_SESSION_DISTANCE', index=15, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BGMODE_POI_PROXIMITY', index=16, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LUCKY_FRIEND', index=17, number=17,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BGMODE_NAMED_BUDDY_CANDY', index=18, number=18,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='APP_BADGE_ONLY', index=19, number=19,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMBAT_VS_SEEKER_CHARGED', index=20, number=20,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMBAT_COMPETITIVE_SEASON_END', index=21, number=21,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUDDY_HUNGRY', index=22, number=22,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUDDY_FOUND_GIFT', index=23, number=24,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUDDY_AFFECTION_LEVEL_MILESTONE', index=24, number=25,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUDDY_AFFECTION_WALKING', index=25, number=26,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUDDY_AFFECTION_CARE', index=26, number=27,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUDDY_AFFECTION_BATTLE', index=27, number=28,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUDDY_AFFECTION_PHOTO', index=28, number=29,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUDDY_AFFECTION_POI', index=29, number=30,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BGMODE_BUDDY_FOUND_GIFT', index=30, number=31,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUDDY_ATTRACTIVE_POI', index=31, number=32,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BGMODE_BUDDY_ATTRACTIVE_POI', index=32, number=33,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUDDY_AFFECTION_ATTRACTIVE_POI', index=33, number=36,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POI_PASSCODE_REDEEMED', index=34, number=37,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_EGGS_INCUBATING', index=35, number=38,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RETENTION_UNOPENED_GIFTS', index=36, number=39,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RETENTION_STARPIECE', index=37, number=40,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RETENTION_INCENSE', index=38, number=41,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RETENTION_LUCKY_EGG', index=39, number=42,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RETENTION_ADVSYNC_REWARDS', index=40, number=43,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RETENTION_EGGS_NOT_INCUBATING', index=41, number=44,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RETENTION_POWER_WALK', index=42, number=45,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RETENTION_FUN_WITH_FRIENDS', index=43, number=46,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUDDY_REMOTE_GIFT', index=44, number=47,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BGMODE_BUDDY_REMOTE_GIFT', index=45, number=48,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REMOTE_RAID_INVITATION', index=46, number=49,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_REWARDS', index=47, number=50,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TIMED_GROUP_CHALLENGE_STARTED', index=48, number=51,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TIMED_GROUP_CHALLENGE_GOAL_MET', index=49, number=52,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=67,
  serialized_end=1470,
)
_sym_db.RegisterEnumDescriptor(_NOTIFICATIONCATEGORY)

NotificationCategory = enum_type_wrapper.EnumTypeWrapper(_NOTIFICATIONCATEGORY)
UNSET_NOTIFICATION_CATEGORY = 0
GYM_REMOVAL = 1
POKEMON_HUNGRY = 2
POKEMON_WON = 3
EXCLUSIVE_RAID_INVITE = 4
EXCLUSIVE_RAID_CANCELLATION = 5
GIFTBOX_INCOMING = 6
GIFTBOX_DELIVERED = 7
FRIENDSHIP_MILESTONE_REWARD = 8
GYM_BATTLE_FRIENDSHIP_INCREMENT = 9
SHARED_EXCLUSIVE_RAID_INVITE = 10
BGMODE_EGG_HATCH = 11
BGMODE_BUDDY_CANDY = 12
BGMODE_WEEKLY_FITNESS_REPORT = 13
COMBAT_CHALLENGE_OPENED = 14
BGMODE_OFF_SESSION_DISTANCE = 15
BGMODE_POI_PROXIMITY = 16
LUCKY_FRIEND = 17
BGMODE_NAMED_BUDDY_CANDY = 18
APP_BADGE_ONLY = 19
COMBAT_VS_SEEKER_CHARGED = 20
COMBAT_COMPETITIVE_SEASON_END = 21
BUDDY_HUNGRY = 22
BUDDY_FOUND_GIFT = 24
BUDDY_AFFECTION_LEVEL_MILESTONE = 25
BUDDY_AFFECTION_WALKING = 26
BUDDY_AFFECTION_CARE = 27
BUDDY_AFFECTION_BATTLE = 28
BUDDY_AFFECTION_PHOTO = 29
BUDDY_AFFECTION_POI = 30
BGMODE_BUDDY_FOUND_GIFT = 31
BUDDY_ATTRACTIVE_POI = 32
BGMODE_BUDDY_ATTRACTIVE_POI = 33
BUDDY_AFFECTION_ATTRACTIVE_POI = 36
POI_PASSCODE_REDEEMED = 37
NO_EGGS_INCUBATING = 38
RETENTION_UNOPENED_GIFTS = 39
RETENTION_STARPIECE = 40
RETENTION_INCENSE = 41
RETENTION_LUCKY_EGG = 42
RETENTION_ADVSYNC_REWARDS = 43
RETENTION_EGGS_NOT_INCUBATING = 44
RETENTION_POWER_WALK = 45
RETENTION_FUN_WITH_FRIENDS = 46
BUDDY_REMOTE_GIFT = 47
BGMODE_BUDDY_REMOTE_GIFT = 48
REMOTE_RAID_INVITATION = 49
ITEM_REWARDS = 50
TIMED_GROUP_CHALLENGE_STARTED = 51
TIMED_GROUP_CHALLENGE_GOAL_MET = 52


DESCRIPTOR.enum_types_by_name['NotificationCategory'] = _NOTIFICATIONCATEGORY


# @@protoc_insertion_point(module_scope)
