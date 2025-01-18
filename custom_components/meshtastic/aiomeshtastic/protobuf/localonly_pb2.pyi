"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.message
from . import config_pb2
from . import module_config_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class LocalConfig(google.protobuf.message.Message):
    """
    Protobuf structures common to apponly.proto and deviceonly.proto
    This is never sent over the wire, only for local use
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DEVICE_FIELD_NUMBER: builtins.int
    POSITION_FIELD_NUMBER: builtins.int
    POWER_FIELD_NUMBER: builtins.int
    NETWORK_FIELD_NUMBER: builtins.int
    DISPLAY_FIELD_NUMBER: builtins.int
    LORA_FIELD_NUMBER: builtins.int
    BLUETOOTH_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    SECURITY_FIELD_NUMBER: builtins.int
    version: builtins.int
    """
    A version integer used to invalidate old save files when we make
    incompatible changes This integer is set at build time and is private to
    NodeDB.cpp in the device code.
    """
    @property
    def device(self) -> config_pb2.Config.DeviceConfig:
        """
        The part of the config that is specific to the Device
        """

    @property
    def position(self) -> config_pb2.Config.PositionConfig:
        """
        The part of the config that is specific to the GPS Position
        """

    @property
    def power(self) -> config_pb2.Config.PowerConfig:
        """
        The part of the config that is specific to the Power settings
        """

    @property
    def network(self) -> config_pb2.Config.NetworkConfig:
        """
        The part of the config that is specific to the Wifi Settings
        """

    @property
    def display(self) -> config_pb2.Config.DisplayConfig:
        """
        The part of the config that is specific to the Display
        """

    @property
    def lora(self) -> config_pb2.Config.LoRaConfig:
        """
        The part of the config that is specific to the Lora Radio
        """

    @property
    def bluetooth(self) -> config_pb2.Config.BluetoothConfig:
        """
        The part of the config that is specific to the Bluetooth settings
        """

    @property
    def security(self) -> config_pb2.Config.SecurityConfig:
        """
        The part of the config that is specific to Security settings
        """

    def __init__(
        self,
        *,
        device: config_pb2.Config.DeviceConfig | None = ...,
        position: config_pb2.Config.PositionConfig | None = ...,
        power: config_pb2.Config.PowerConfig | None = ...,
        network: config_pb2.Config.NetworkConfig | None = ...,
        display: config_pb2.Config.DisplayConfig | None = ...,
        lora: config_pb2.Config.LoRaConfig | None = ...,
        bluetooth: config_pb2.Config.BluetoothConfig | None = ...,
        version: builtins.int = ...,
        security: config_pb2.Config.SecurityConfig | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["bluetooth", b"bluetooth", "device", b"device", "display", b"display", "lora", b"lora", "network", b"network", "position", b"position", "power", b"power", "security", b"security"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["bluetooth", b"bluetooth", "device", b"device", "display", b"display", "lora", b"lora", "network", b"network", "position", b"position", "power", b"power", "security", b"security", "version", b"version"]) -> None: ...

global___LocalConfig = LocalConfig

@typing.final
class LocalModuleConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MQTT_FIELD_NUMBER: builtins.int
    SERIAL_FIELD_NUMBER: builtins.int
    EXTERNAL_NOTIFICATION_FIELD_NUMBER: builtins.int
    STORE_FORWARD_FIELD_NUMBER: builtins.int
    RANGE_TEST_FIELD_NUMBER: builtins.int
    TELEMETRY_FIELD_NUMBER: builtins.int
    CANNED_MESSAGE_FIELD_NUMBER: builtins.int
    AUDIO_FIELD_NUMBER: builtins.int
    REMOTE_HARDWARE_FIELD_NUMBER: builtins.int
    NEIGHBOR_INFO_FIELD_NUMBER: builtins.int
    AMBIENT_LIGHTING_FIELD_NUMBER: builtins.int
    DETECTION_SENSOR_FIELD_NUMBER: builtins.int
    PAXCOUNTER_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    version: builtins.int
    """
    A version integer used to invalidate old save files when we make
    incompatible changes This integer is set at build time and is private to
    NodeDB.cpp in the device code.
    """
    @property
    def mqtt(self) -> module_config_pb2.ModuleConfig.MQTTConfig:
        """
        The part of the config that is specific to the MQTT module
        """

    @property
    def serial(self) -> module_config_pb2.ModuleConfig.SerialConfig:
        """
        The part of the config that is specific to the Serial module
        """

    @property
    def external_notification(self) -> module_config_pb2.ModuleConfig.ExternalNotificationConfig:
        """
        The part of the config that is specific to the ExternalNotification module
        """

    @property
    def store_forward(self) -> module_config_pb2.ModuleConfig.StoreForwardConfig:
        """
        The part of the config that is specific to the Store & Forward module
        """

    @property
    def range_test(self) -> module_config_pb2.ModuleConfig.RangeTestConfig:
        """
        The part of the config that is specific to the RangeTest module
        """

    @property
    def telemetry(self) -> module_config_pb2.ModuleConfig.TelemetryConfig:
        """
        The part of the config that is specific to the Telemetry module
        """

    @property
    def canned_message(self) -> module_config_pb2.ModuleConfig.CannedMessageConfig:
        """
        The part of the config that is specific to the Canned Message module
        """

    @property
    def audio(self) -> module_config_pb2.ModuleConfig.AudioConfig:
        """
        The part of the config that is specific to the Audio module
        """

    @property
    def remote_hardware(self) -> module_config_pb2.ModuleConfig.RemoteHardwareConfig:
        """
        The part of the config that is specific to the Remote Hardware module
        """

    @property
    def neighbor_info(self) -> module_config_pb2.ModuleConfig.NeighborInfoConfig:
        """
        The part of the config that is specific to the Neighbor Info module
        """

    @property
    def ambient_lighting(self) -> module_config_pb2.ModuleConfig.AmbientLightingConfig:
        """
        The part of the config that is specific to the Ambient Lighting module
        """

    @property
    def detection_sensor(self) -> module_config_pb2.ModuleConfig.DetectionSensorConfig:
        """
        The part of the config that is specific to the Detection Sensor module
        """

    @property
    def paxcounter(self) -> module_config_pb2.ModuleConfig.PaxcounterConfig:
        """
        Paxcounter Config
        """

    def __init__(
        self,
        *,
        mqtt: module_config_pb2.ModuleConfig.MQTTConfig | None = ...,
        serial: module_config_pb2.ModuleConfig.SerialConfig | None = ...,
        external_notification: module_config_pb2.ModuleConfig.ExternalNotificationConfig | None = ...,
        store_forward: module_config_pb2.ModuleConfig.StoreForwardConfig | None = ...,
        range_test: module_config_pb2.ModuleConfig.RangeTestConfig | None = ...,
        telemetry: module_config_pb2.ModuleConfig.TelemetryConfig | None = ...,
        canned_message: module_config_pb2.ModuleConfig.CannedMessageConfig | None = ...,
        audio: module_config_pb2.ModuleConfig.AudioConfig | None = ...,
        remote_hardware: module_config_pb2.ModuleConfig.RemoteHardwareConfig | None = ...,
        neighbor_info: module_config_pb2.ModuleConfig.NeighborInfoConfig | None = ...,
        ambient_lighting: module_config_pb2.ModuleConfig.AmbientLightingConfig | None = ...,
        detection_sensor: module_config_pb2.ModuleConfig.DetectionSensorConfig | None = ...,
        paxcounter: module_config_pb2.ModuleConfig.PaxcounterConfig | None = ...,
        version: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["ambient_lighting", b"ambient_lighting", "audio", b"audio", "canned_message", b"canned_message", "detection_sensor", b"detection_sensor", "external_notification", b"external_notification", "mqtt", b"mqtt", "neighbor_info", b"neighbor_info", "paxcounter", b"paxcounter", "range_test", b"range_test", "remote_hardware", b"remote_hardware", "serial", b"serial", "store_forward", b"store_forward", "telemetry", b"telemetry"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["ambient_lighting", b"ambient_lighting", "audio", b"audio", "canned_message", b"canned_message", "detection_sensor", b"detection_sensor", "external_notification", b"external_notification", "mqtt", b"mqtt", "neighbor_info", b"neighbor_info", "paxcounter", b"paxcounter", "range_test", b"range_test", "remote_hardware", b"remote_hardware", "serial", b"serial", "store_forward", b"store_forward", "telemetry", b"telemetry", "version", b"version"]) -> None: ...

global___LocalModuleConfig = LocalModuleConfig
