# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: mqtt.proto
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
    'meshtastic/aiomeshtastic/protobuf/mqtt.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import config_pb2 as meshtastic_dot_aiomeshtastic_dot_protobuf_dot_config__pb2
from . import mesh_pb2 as meshtastic_dot_aiomeshtastic_dot_protobuf_dot_mesh__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,meshtastic/aiomeshtastic/protobuf/mqtt.proto\x12!meshtastic.aiomeshtastic.protobuf\x1a.meshtastic/aiomeshtastic/protobuf/config.proto\x1a,meshtastic/aiomeshtastic/protobuf/mesh.proto\"x\n\x0fServiceEnvelope\x12=\n\x06packet\x18\x01 \x01(\x0b\x32-.meshtastic.aiomeshtastic.protobuf.MeshPacket\x12\x12\n\nchannel_id\x18\x02 \x01(\t\x12\x12\n\ngateway_id\x18\x03 \x01(\t\"\x98\x04\n\tMapReport\x12\x11\n\tlong_name\x18\x01 \x01(\t\x12\x12\n\nshort_name\x18\x02 \x01(\t\x12I\n\x04role\x18\x03 \x01(\x0e\x32;.meshtastic.aiomeshtastic.protobuf.Config.DeviceConfig.Role\x12\x42\n\x08hw_model\x18\x04 \x01(\x0e\x32\x30.meshtastic.aiomeshtastic.protobuf.HardwareModel\x12\x18\n\x10\x66irmware_version\x18\x05 \x01(\t\x12O\n\x06region\x18\x06 \x01(\x0e\x32?.meshtastic.aiomeshtastic.protobuf.Config.LoRaConfig.RegionCode\x12V\n\x0cmodem_preset\x18\x07 \x01(\x0e\x32@.meshtastic.aiomeshtastic.protobuf.Config.LoRaConfig.ModemPreset\x12\x1b\n\x13has_default_channel\x18\x08 \x01(\x08\x12\x12\n\nlatitude_i\x18\t \x01(\x0f\x12\x13\n\x0blongitude_i\x18\n \x01(\x0f\x12\x10\n\x08\x61ltitude\x18\x0b \x01(\x05\x12\x1a\n\x12position_precision\x18\x0c \x01(\r\x12\x1e\n\x16num_online_local_nodes\x18\r \x01(\rB_\n\x13\x63om.geeksville.meshB\nMQTTProtosZ\"github.com/meshtastic/go/generated\xaa\x02\x14Meshtastic.Protobufs\xba\x02\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'meshtastic.aiomeshtastic.protobuf.mqtt_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\023com.geeksville.meshB\nMQTTProtosZ\"github.com/meshtastic/go/generated\252\002\024Meshtastic.Protobufs\272\002\000'
  _globals['_SERVICEENVELOPE']._serialized_start=177
  _globals['_SERVICEENVELOPE']._serialized_end=297
  _globals['_MAPREPORT']._serialized_start=300
  _globals['_MAPREPORT']._serialized_end=836
# @@protoc_insertion_point(module_scope)
