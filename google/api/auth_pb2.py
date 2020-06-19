# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/api/auth.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/api/auth.proto",
    package="google.api",
    syntax="proto3",
    serialized_options=b"\n\016com.google.apiB\tAuthProtoP\001ZEgoogle.golang.org/genproto/googleapis/api/serviceconfig;serviceconfig\242\002\004GAPI",
    serialized_pb=b'\n\x15google/api/auth.proto\x12\ngoogle.api\x1a\x1cgoogle/api/annotations.proto"l\n\x0e\x41uthentication\x12-\n\x05rules\x18\x03 \x03(\x0b\x32\x1e.google.api.AuthenticationRule\x12+\n\tproviders\x18\x04 \x03(\x0b\x32\x18.google.api.AuthProvider"\xa9\x01\n\x12\x41uthenticationRule\x12\x10\n\x08selector\x18\x01 \x01(\t\x12,\n\x05oauth\x18\x02 \x01(\x0b\x32\x1d.google.api.OAuthRequirements\x12 \n\x18\x61llow_without_credential\x18\x05 \x01(\x08\x12\x31\n\x0crequirements\x18\x07 \x03(\x0b\x32\x1b.google.api.AuthRequirement"j\n\x0c\x41uthProvider\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06issuer\x18\x02 \x01(\t\x12\x10\n\x08jwks_uri\x18\x03 \x01(\t\x12\x11\n\taudiences\x18\x04 \x01(\t\x12\x19\n\x11\x61uthorization_url\x18\x05 \x01(\t"-\n\x11OAuthRequirements\x12\x18\n\x10\x63\x61nonical_scopes\x18\x01 \x01(\t"9\n\x0f\x41uthRequirement\x12\x13\n\x0bprovider_id\x18\x01 \x01(\t\x12\x11\n\taudiences\x18\x02 \x01(\tBk\n\x0e\x63om.google.apiB\tAuthProtoP\x01ZEgoogle.golang.org/genproto/googleapis/api/serviceconfig;serviceconfig\xa2\x02\x04GAPIb\x06proto3',
    dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR],
)


_AUTHENTICATION = _descriptor.Descriptor(
    name="Authentication",
    full_name="google.api.Authentication",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="rules",
            full_name="google.api.Authentication.rules",
            index=0,
            number=3,
            type=11,
            cpp_type=10,
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
        ),
        _descriptor.FieldDescriptor(
            name="providers",
            full_name="google.api.Authentication.providers",
            index=1,
            number=4,
            type=11,
            cpp_type=10,
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
    serialized_start=67,
    serialized_end=175,
)


_AUTHENTICATIONRULE = _descriptor.Descriptor(
    name="AuthenticationRule",
    full_name="google.api.AuthenticationRule",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="selector",
            full_name="google.api.AuthenticationRule.selector",
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
        ),
        _descriptor.FieldDescriptor(
            name="oauth",
            full_name="google.api.AuthenticationRule.oauth",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="allow_without_credential",
            full_name="google.api.AuthenticationRule.allow_without_credential",
            index=2,
            number=5,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="requirements",
            full_name="google.api.AuthenticationRule.requirements",
            index=3,
            number=7,
            type=11,
            cpp_type=10,
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
    serialized_start=178,
    serialized_end=347,
)


_AUTHPROVIDER = _descriptor.Descriptor(
    name="AuthProvider",
    full_name="google.api.AuthProvider",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="google.api.AuthProvider.id",
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
        ),
        _descriptor.FieldDescriptor(
            name="issuer",
            full_name="google.api.AuthProvider.issuer",
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
        ),
        _descriptor.FieldDescriptor(
            name="jwks_uri",
            full_name="google.api.AuthProvider.jwks_uri",
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
        ),
        _descriptor.FieldDescriptor(
            name="audiences",
            full_name="google.api.AuthProvider.audiences",
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
        ),
        _descriptor.FieldDescriptor(
            name="authorization_url",
            full_name="google.api.AuthProvider.authorization_url",
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
    serialized_start=349,
    serialized_end=455,
)


_OAUTHREQUIREMENTS = _descriptor.Descriptor(
    name="OAuthRequirements",
    full_name="google.api.OAuthRequirements",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="canonical_scopes",
            full_name="google.api.OAuthRequirements.canonical_scopes",
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
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=457,
    serialized_end=502,
)


_AUTHREQUIREMENT = _descriptor.Descriptor(
    name="AuthRequirement",
    full_name="google.api.AuthRequirement",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="provider_id",
            full_name="google.api.AuthRequirement.provider_id",
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
        ),
        _descriptor.FieldDescriptor(
            name="audiences",
            full_name="google.api.AuthRequirement.audiences",
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
    serialized_start=504,
    serialized_end=561,
)

_AUTHENTICATION.fields_by_name["rules"].message_type = _AUTHENTICATIONRULE
_AUTHENTICATION.fields_by_name["providers"].message_type = _AUTHPROVIDER
_AUTHENTICATIONRULE.fields_by_name["oauth"].message_type = _OAUTHREQUIREMENTS
_AUTHENTICATIONRULE.fields_by_name["requirements"].message_type = _AUTHREQUIREMENT
DESCRIPTOR.message_types_by_name["Authentication"] = _AUTHENTICATION
DESCRIPTOR.message_types_by_name["AuthenticationRule"] = _AUTHENTICATIONRULE
DESCRIPTOR.message_types_by_name["AuthProvider"] = _AUTHPROVIDER
DESCRIPTOR.message_types_by_name["OAuthRequirements"] = _OAUTHREQUIREMENTS
DESCRIPTOR.message_types_by_name["AuthRequirement"] = _AUTHREQUIREMENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Authentication = _reflection.GeneratedProtocolMessageType(
    "Authentication",
    (_message.Message,),
    {
        "DESCRIPTOR": _AUTHENTICATION,
        "__module__": "google.api.auth_pb2"
        # @@protoc_insertion_point(class_scope:google.api.Authentication)
    },
)
_sym_db.RegisterMessage(Authentication)

AuthenticationRule = _reflection.GeneratedProtocolMessageType(
    "AuthenticationRule",
    (_message.Message,),
    {
        "DESCRIPTOR": _AUTHENTICATIONRULE,
        "__module__": "google.api.auth_pb2"
        # @@protoc_insertion_point(class_scope:google.api.AuthenticationRule)
    },
)
_sym_db.RegisterMessage(AuthenticationRule)

AuthProvider = _reflection.GeneratedProtocolMessageType(
    "AuthProvider",
    (_message.Message,),
    {
        "DESCRIPTOR": _AUTHPROVIDER,
        "__module__": "google.api.auth_pb2"
        # @@protoc_insertion_point(class_scope:google.api.AuthProvider)
    },
)
_sym_db.RegisterMessage(AuthProvider)

OAuthRequirements = _reflection.GeneratedProtocolMessageType(
    "OAuthRequirements",
    (_message.Message,),
    {
        "DESCRIPTOR": _OAUTHREQUIREMENTS,
        "__module__": "google.api.auth_pb2"
        # @@protoc_insertion_point(class_scope:google.api.OAuthRequirements)
    },
)
_sym_db.RegisterMessage(OAuthRequirements)

AuthRequirement = _reflection.GeneratedProtocolMessageType(
    "AuthRequirement",
    (_message.Message,),
    {
        "DESCRIPTOR": _AUTHREQUIREMENT,
        "__module__": "google.api.auth_pb2"
        # @@protoc_insertion_point(class_scope:google.api.AuthRequirement)
    },
)
_sym_db.RegisterMessage(AuthRequirement)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
