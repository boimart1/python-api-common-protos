# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/type/postal_address.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/type/postal_address.proto",
    package="google.type",
    syntax="proto3",
    serialized_options=b"\n\017com.google.typeB\022PostalAddressProtoP\001ZFgoogle.golang.org/genproto/googleapis/type/postaladdress;postaladdress\370\001\001\242\002\003GTP",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n google/type/postal_address.proto\x12\x0bgoogle.type"\xfd\x01\n\rPostalAddress\x12\x10\n\x08revision\x18\x01 \x01(\x05\x12\x13\n\x0bregion_code\x18\x02 \x01(\t\x12\x15\n\rlanguage_code\x18\x03 \x01(\t\x12\x13\n\x0bpostal_code\x18\x04 \x01(\t\x12\x14\n\x0csorting_code\x18\x05 \x01(\t\x12\x1b\n\x13\x61\x64ministrative_area\x18\x06 \x01(\t\x12\x10\n\x08locality\x18\x07 \x01(\t\x12\x13\n\x0bsublocality\x18\x08 \x01(\t\x12\x15\n\raddress_lines\x18\t \x03(\t\x12\x12\n\nrecipients\x18\n \x03(\t\x12\x14\n\x0corganization\x18\x0b \x01(\tBx\n\x0f\x63om.google.typeB\x12PostalAddressProtoP\x01ZFgoogle.golang.org/genproto/googleapis/type/postaladdress;postaladdress\xf8\x01\x01\xa2\x02\x03GTPb\x06proto3',
)


_POSTALADDRESS = _descriptor.Descriptor(
    name="PostalAddress",
    full_name="google.type.PostalAddress",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="revision",
            full_name="google.type.PostalAddress.revision",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
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
            name="region_code",
            full_name="google.type.PostalAddress.region_code",
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
            name="language_code",
            full_name="google.type.PostalAddress.language_code",
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
            name="postal_code",
            full_name="google.type.PostalAddress.postal_code",
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
        _descriptor.FieldDescriptor(
            name="sorting_code",
            full_name="google.type.PostalAddress.sorting_code",
            index=4,
            number=5,
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
            name="administrative_area",
            full_name="google.type.PostalAddress.administrative_area",
            index=5,
            number=6,
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
            name="locality",
            full_name="google.type.PostalAddress.locality",
            index=6,
            number=7,
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
            name="sublocality",
            full_name="google.type.PostalAddress.sublocality",
            index=7,
            number=8,
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
            name="address_lines",
            full_name="google.type.PostalAddress.address_lines",
            index=8,
            number=9,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
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
            name="recipients",
            full_name="google.type.PostalAddress.recipients",
            index=9,
            number=10,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
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
            name="organization",
            full_name="google.type.PostalAddress.organization",
            index=10,
            number=11,
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
    serialized_start=50,
    serialized_end=303,
)

DESCRIPTOR.message_types_by_name["PostalAddress"] = _POSTALADDRESS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PostalAddress = _reflection.GeneratedProtocolMessageType(
    "PostalAddress",
    (_message.Message,),
    {
        "DESCRIPTOR": _POSTALADDRESS,
        "__module__": "google.type.postal_address_pb2"
        # @@protoc_insertion_point(class_scope:google.type.PostalAddress)
    },
)
_sym_db.RegisterMessage(PostalAddress)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
