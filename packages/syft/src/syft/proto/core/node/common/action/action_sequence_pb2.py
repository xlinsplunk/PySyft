# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/core/node/common/action/action_sequence.proto
"""Generated protocol buffer code."""
# third party
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


# syft absolute
from syft.proto.core.io import address_pb2 as proto_dot_core_dot_io_dot_address__pb2
from syft.proto.core.node.common.action import (
    save_object_pb2 as proto_dot_core_dot_node_dot_common_dot_action_dot_save__object__pb2,
)

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n3proto/core/node/common/action/action_sequence.proto\x12\x1csyft.core.node.common.action\x1a/proto/core/node/common/action/save_object.proto\x1a\x1bproto/core/io/address.proto"u\n\x0e\x41\x63tionSequence\x12;\n\x03obj\x18\x01 \x03(\x0b\x32..syft.core.node.common.action.SaveObjectAction\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Addressb\x06proto3'
)


_ACTIONSEQUENCE = DESCRIPTOR.message_types_by_name["ActionSequence"]
ActionSequence = _reflection.GeneratedProtocolMessageType(
    "ActionSequence",
    (_message.Message,),
    {
        "DESCRIPTOR": _ACTIONSEQUENCE,
        "__module__": "proto.core.node.common.action.action_sequence_pb2"
        # @@protoc_insertion_point(class_scope:syft.core.node.common.action.ActionSequence)
    },
)
_sym_db.RegisterMessage(ActionSequence)

if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _ACTIONSEQUENCE._serialized_start = 163
    _ACTIONSEQUENCE._serialized_end = 280
# @@protoc_insertion_point(module_scope)
