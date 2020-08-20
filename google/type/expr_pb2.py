# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/type/expr.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/type/expr.proto",
    package="google.type",
    syntax="proto3",
    serialized_options=b"\n\017com.google.typeB\tExprProtoP\001Z4google.golang.org/genproto/googleapis/type/expr;expr\242\002\003GTP",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x16google/type/expr.proto\x12\x0bgoogle.type"P\n\x04\x45xpr\x12\x12\n\nexpression\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x10\n\x08location\x18\x04 \x01(\tBZ\n\x0f\x63om.google.typeB\tExprProtoP\x01Z4google.golang.org/genproto/googleapis/type/expr;expr\xa2\x02\x03GTPb\x06proto3',
)


_EXPR = _descriptor.Descriptor(
    name="Expr",
    full_name="google.type.Expr",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="expression",
            full_name="google.type.Expr.expression",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="title",
            full_name="google.type.Expr.title",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="description",
            full_name="google.type.Expr.description",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="location",
            full_name="google.type.Expr.location",
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=39,
    serialized_end=119,
)

DESCRIPTOR.message_types_by_name["Expr"] = _EXPR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Expr = _reflection.GeneratedProtocolMessageType(
    "Expr",
    (_message.Message,),
    {
        "DESCRIPTOR": _EXPR,
        "__module__": "google.type.expr_pb2"
        # @@protoc_insertion_point(class_scope:google.type.Expr)
    },
)
_sym_db.RegisterMessage(Expr)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
