# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: powermon.proto
# Protobuf Python Version: 5.28.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    2,
    '',
    'meshtastic/aiomeshtastic/protobuf/powermon.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0meshtastic/aiomeshtastic/protobuf/powermon.proto\x12!meshtastic.aiomeshtastic.protobuf\"\xe0\x01\n\x08PowerMon\"\xd3\x01\n\x05State\x12\x08\n\x04None\x10\x00\x12\x11\n\rCPU_DeepSleep\x10\x01\x12\x12\n\x0e\x43PU_LightSleep\x10\x02\x12\x0c\n\x08Vext1_On\x10\x04\x12\r\n\tLora_RXOn\x10\x08\x12\r\n\tLora_TXOn\x10\x10\x12\x11\n\rLora_RXActive\x10 \x12\t\n\x05\x42T_On\x10@\x12\x0b\n\x06LED_On\x10\x80\x01\x12\x0e\n\tScreen_On\x10\x80\x02\x12\x13\n\x0eScreen_Drawing\x10\x80\x04\x12\x0c\n\x07Wifi_On\x10\x80\x08\x12\x0f\n\nGPS_Active\x10\x80\x10\"\x96\x03\n\x12PowerStressMessage\x12I\n\x03\x63md\x18\x01 \x01(\x0e\x32<.meshtastic.aiomeshtastic.protobuf.PowerStressMessage.Opcode\x12\x13\n\x0bnum_seconds\x18\x02 \x01(\x02\"\x9f\x02\n\x06Opcode\x12\t\n\x05UNSET\x10\x00\x12\x0e\n\nPRINT_INFO\x10\x01\x12\x0f\n\x0b\x46ORCE_QUIET\x10\x02\x12\r\n\tEND_QUIET\x10\x03\x12\r\n\tSCREEN_ON\x10\x10\x12\x0e\n\nSCREEN_OFF\x10\x11\x12\x0c\n\x08\x43PU_IDLE\x10 \x12\x11\n\rCPU_DEEPSLEEP\x10!\x12\x0e\n\nCPU_FULLON\x10\"\x12\n\n\x06LED_ON\x10\x30\x12\x0b\n\x07LED_OFF\x10\x31\x12\x0c\n\x08LORA_OFF\x10@\x12\x0b\n\x07LORA_TX\x10\x41\x12\x0b\n\x07LORA_RX\x10\x42\x12\n\n\x06\x42T_OFF\x10P\x12\t\n\x05\x42T_ON\x10Q\x12\x0c\n\x08WIFI_OFF\x10`\x12\x0b\n\x07WIFI_ON\x10\x61\x12\x0b\n\x07GPS_OFF\x10p\x12\n\n\x06GPS_ON\x10qBc\n\x13\x63om.geeksville.meshB\x0ePowerMonProtosZ\"github.com/meshtastic/go/generated\xaa\x02\x14Meshtastic.Protobufs\xba\x02\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'meshtastic.aiomeshtastic.protobuf.powermon_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\023com.geeksville.meshB\016PowerMonProtosZ\"github.com/meshtastic/go/generated\252\002\024Meshtastic.Protobufs\272\002\000'
  _globals['_POWERMON']._serialized_start=88
  _globals['_POWERMON']._serialized_end=312
  _globals['_POWERMON_STATE']._serialized_start=101
  _globals['_POWERMON_STATE']._serialized_end=312
  _globals['_POWERSTRESSMESSAGE']._serialized_start=315
  _globals['_POWERSTRESSMESSAGE']._serialized_end=721
  _globals['_POWERSTRESSMESSAGE_OPCODE']._serialized_start=434
  _globals['_POWERSTRESSMESSAGE_OPCODE']._serialized_end=721
# @@protoc_insertion_point(module_scope)
