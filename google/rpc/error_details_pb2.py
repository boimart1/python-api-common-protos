# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/rpc/error_details.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/rpc/error_details.proto",
    package="google.rpc",
    syntax="proto3",
    serialized_options=b"\n\016com.google.rpcB\021ErrorDetailsProtoP\001Z?google.golang.org/genproto/googleapis/rpc/errdetails;errdetails\242\002\003RPC",
    serialized_pb=b'\n\x1egoogle/rpc/error_details.proto\x12\ngoogle.rpc\x1a\x1egoogle/protobuf/duration.proto";\n\tRetryInfo\x12.\n\x0bretry_delay\x18\x01 \x01(\x0b\x32\x19.google.protobuf.Duration"2\n\tDebugInfo\x12\x15\n\rstack_entries\x18\x01 \x03(\t\x12\x0e\n\x06\x64\x65tail\x18\x02 \x01(\t"y\n\x0cQuotaFailure\x12\x36\n\nviolations\x18\x01 \x03(\x0b\x32".google.rpc.QuotaFailure.Violation\x1a\x31\n\tViolation\x12\x0f\n\x07subject\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t"\x93\x01\n\tErrorInfo\x12\x0e\n\x06reason\x18\x01 \x01(\t\x12\x0e\n\x06\x64omain\x18\x02 \x01(\t\x12\x35\n\x08metadata\x18\x03 \x03(\x0b\x32#.google.rpc.ErrorInfo.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"\x95\x01\n\x13PreconditionFailure\x12=\n\nviolations\x18\x01 \x03(\x0b\x32).google.rpc.PreconditionFailure.Violation\x1a?\n\tViolation\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0f\n\x07subject\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t"\x83\x01\n\nBadRequest\x12?\n\x10\x66ield_violations\x18\x01 \x03(\x0b\x32%.google.rpc.BadRequest.FieldViolation\x1a\x34\n\x0e\x46ieldViolation\x12\r\n\x05\x66ield\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t"7\n\x0bRequestInfo\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x14\n\x0cserving_data\x18\x02 \x01(\t"`\n\x0cResourceInfo\x12\x15\n\rresource_type\x18\x01 \x01(\t\x12\x15\n\rresource_name\x18\x02 \x01(\t\x12\r\n\x05owner\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t"V\n\x04Help\x12$\n\x05links\x18\x01 \x03(\x0b\x32\x15.google.rpc.Help.Link\x1a(\n\x04Link\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t"3\n\x10LocalizedMessage\x12\x0e\n\x06locale\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\tBl\n\x0e\x63om.google.rpcB\x11\x45rrorDetailsProtoP\x01Z?google.golang.org/genproto/googleapis/rpc/errdetails;errdetails\xa2\x02\x03RPCb\x06proto3',
    dependencies=[google_dot_protobuf_dot_duration__pb2.DESCRIPTOR],
)


_RETRYINFO = _descriptor.Descriptor(
    name="RetryInfo",
    full_name="google.rpc.RetryInfo",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="retry_delay",
            full_name="google.rpc.RetryInfo.retry_delay",
            index=0,
            number=1,
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
    serialized_start=78,
    serialized_end=137,
)


_DEBUGINFO = _descriptor.Descriptor(
    name="DebugInfo",
    full_name="google.rpc.DebugInfo",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="stack_entries",
            full_name="google.rpc.DebugInfo.stack_entries",
            index=0,
            number=1,
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
        ),
        _descriptor.FieldDescriptor(
            name="detail",
            full_name="google.rpc.DebugInfo.detail",
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
    serialized_start=139,
    serialized_end=189,
)


_QUOTAFAILURE_VIOLATION = _descriptor.Descriptor(
    name="Violation",
    full_name="google.rpc.QuotaFailure.Violation",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="subject",
            full_name="google.rpc.QuotaFailure.Violation.subject",
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
            name="description",
            full_name="google.rpc.QuotaFailure.Violation.description",
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
    serialized_start=263,
    serialized_end=312,
)

_QUOTAFAILURE = _descriptor.Descriptor(
    name="QuotaFailure",
    full_name="google.rpc.QuotaFailure",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="violations",
            full_name="google.rpc.QuotaFailure.violations",
            index=0,
            number=1,
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
        )
    ],
    extensions=[],
    nested_types=[_QUOTAFAILURE_VIOLATION],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=191,
    serialized_end=312,
)


_ERRORINFO_METADATAENTRY = _descriptor.Descriptor(
    name="MetadataEntry",
    full_name="google.rpc.ErrorInfo.MetadataEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="google.rpc.ErrorInfo.MetadataEntry.key",
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
            name="value",
            full_name="google.rpc.ErrorInfo.MetadataEntry.value",
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
    serialized_options=b"8\001",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=415,
    serialized_end=462,
)

_ERRORINFO = _descriptor.Descriptor(
    name="ErrorInfo",
    full_name="google.rpc.ErrorInfo",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="reason",
            full_name="google.rpc.ErrorInfo.reason",
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
            name="domain",
            full_name="google.rpc.ErrorInfo.domain",
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
            name="metadata",
            full_name="google.rpc.ErrorInfo.metadata",
            index=2,
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
    ],
    extensions=[],
    nested_types=[_ERRORINFO_METADATAENTRY],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=315,
    serialized_end=462,
)


_PRECONDITIONFAILURE_VIOLATION = _descriptor.Descriptor(
    name="Violation",
    full_name="google.rpc.PreconditionFailure.Violation",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="type",
            full_name="google.rpc.PreconditionFailure.Violation.type",
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
            name="subject",
            full_name="google.rpc.PreconditionFailure.Violation.subject",
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
            name="description",
            full_name="google.rpc.PreconditionFailure.Violation.description",
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=551,
    serialized_end=614,
)

_PRECONDITIONFAILURE = _descriptor.Descriptor(
    name="PreconditionFailure",
    full_name="google.rpc.PreconditionFailure",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="violations",
            full_name="google.rpc.PreconditionFailure.violations",
            index=0,
            number=1,
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
        )
    ],
    extensions=[],
    nested_types=[_PRECONDITIONFAILURE_VIOLATION],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=465,
    serialized_end=614,
)


_BADREQUEST_FIELDVIOLATION = _descriptor.Descriptor(
    name="FieldViolation",
    full_name="google.rpc.BadRequest.FieldViolation",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="field",
            full_name="google.rpc.BadRequest.FieldViolation.field",
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
            name="description",
            full_name="google.rpc.BadRequest.FieldViolation.description",
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
    serialized_start=696,
    serialized_end=748,
)

_BADREQUEST = _descriptor.Descriptor(
    name="BadRequest",
    full_name="google.rpc.BadRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="field_violations",
            full_name="google.rpc.BadRequest.field_violations",
            index=0,
            number=1,
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
        )
    ],
    extensions=[],
    nested_types=[_BADREQUEST_FIELDVIOLATION],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=617,
    serialized_end=748,
)


_REQUESTINFO = _descriptor.Descriptor(
    name="RequestInfo",
    full_name="google.rpc.RequestInfo",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="request_id",
            full_name="google.rpc.RequestInfo.request_id",
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
            name="serving_data",
            full_name="google.rpc.RequestInfo.serving_data",
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
    serialized_start=750,
    serialized_end=805,
)


_RESOURCEINFO = _descriptor.Descriptor(
    name="ResourceInfo",
    full_name="google.rpc.ResourceInfo",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="resource_type",
            full_name="google.rpc.ResourceInfo.resource_type",
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
            name="resource_name",
            full_name="google.rpc.ResourceInfo.resource_name",
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
            name="owner",
            full_name="google.rpc.ResourceInfo.owner",
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
            name="description",
            full_name="google.rpc.ResourceInfo.description",
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=807,
    serialized_end=903,
)


_HELP_LINK = _descriptor.Descriptor(
    name="Link",
    full_name="google.rpc.Help.Link",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="description",
            full_name="google.rpc.Help.Link.description",
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
            name="url",
            full_name="google.rpc.Help.Link.url",
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
    serialized_start=951,
    serialized_end=991,
)

_HELP = _descriptor.Descriptor(
    name="Help",
    full_name="google.rpc.Help",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="links",
            full_name="google.rpc.Help.links",
            index=0,
            number=1,
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
        )
    ],
    extensions=[],
    nested_types=[_HELP_LINK],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=905,
    serialized_end=991,
)


_LOCALIZEDMESSAGE = _descriptor.Descriptor(
    name="LocalizedMessage",
    full_name="google.rpc.LocalizedMessage",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="locale",
            full_name="google.rpc.LocalizedMessage.locale",
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
            name="message",
            full_name="google.rpc.LocalizedMessage.message",
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
    serialized_start=993,
    serialized_end=1044,
)

_RETRYINFO.fields_by_name[
    "retry_delay"
].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_QUOTAFAILURE_VIOLATION.containing_type = _QUOTAFAILURE
_QUOTAFAILURE.fields_by_name["violations"].message_type = _QUOTAFAILURE_VIOLATION
_ERRORINFO_METADATAENTRY.containing_type = _ERRORINFO
_ERRORINFO.fields_by_name["metadata"].message_type = _ERRORINFO_METADATAENTRY
_PRECONDITIONFAILURE_VIOLATION.containing_type = _PRECONDITIONFAILURE
_PRECONDITIONFAILURE.fields_by_name[
    "violations"
].message_type = _PRECONDITIONFAILURE_VIOLATION
_BADREQUEST_FIELDVIOLATION.containing_type = _BADREQUEST
_BADREQUEST.fields_by_name["field_violations"].message_type = _BADREQUEST_FIELDVIOLATION
_HELP_LINK.containing_type = _HELP
_HELP.fields_by_name["links"].message_type = _HELP_LINK
DESCRIPTOR.message_types_by_name["RetryInfo"] = _RETRYINFO
DESCRIPTOR.message_types_by_name["DebugInfo"] = _DEBUGINFO
DESCRIPTOR.message_types_by_name["QuotaFailure"] = _QUOTAFAILURE
DESCRIPTOR.message_types_by_name["ErrorInfo"] = _ERRORINFO
DESCRIPTOR.message_types_by_name["PreconditionFailure"] = _PRECONDITIONFAILURE
DESCRIPTOR.message_types_by_name["BadRequest"] = _BADREQUEST
DESCRIPTOR.message_types_by_name["RequestInfo"] = _REQUESTINFO
DESCRIPTOR.message_types_by_name["ResourceInfo"] = _RESOURCEINFO
DESCRIPTOR.message_types_by_name["Help"] = _HELP
DESCRIPTOR.message_types_by_name["LocalizedMessage"] = _LOCALIZEDMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RetryInfo = _reflection.GeneratedProtocolMessageType(
    "RetryInfo",
    (_message.Message,),
    {
        "DESCRIPTOR": _RETRYINFO,
        "__module__": "google.rpc.error_details_pb2"
        # @@protoc_insertion_point(class_scope:google.rpc.RetryInfo)
    },
)
_sym_db.RegisterMessage(RetryInfo)

DebugInfo = _reflection.GeneratedProtocolMessageType(
    "DebugInfo",
    (_message.Message,),
    {
        "DESCRIPTOR": _DEBUGINFO,
        "__module__": "google.rpc.error_details_pb2"
        # @@protoc_insertion_point(class_scope:google.rpc.DebugInfo)
    },
)
_sym_db.RegisterMessage(DebugInfo)

QuotaFailure = _reflection.GeneratedProtocolMessageType(
    "QuotaFailure",
    (_message.Message,),
    {
        "Violation": _reflection.GeneratedProtocolMessageType(
            "Violation",
            (_message.Message,),
            {
                "DESCRIPTOR": _QUOTAFAILURE_VIOLATION,
                "__module__": "google.rpc.error_details_pb2"
                # @@protoc_insertion_point(class_scope:google.rpc.QuotaFailure.Violation)
            },
        ),
        "DESCRIPTOR": _QUOTAFAILURE,
        "__module__": "google.rpc.error_details_pb2"
        # @@protoc_insertion_point(class_scope:google.rpc.QuotaFailure)
    },
)
_sym_db.RegisterMessage(QuotaFailure)
_sym_db.RegisterMessage(QuotaFailure.Violation)

ErrorInfo = _reflection.GeneratedProtocolMessageType(
    "ErrorInfo",
    (_message.Message,),
    {
        "MetadataEntry": _reflection.GeneratedProtocolMessageType(
            "MetadataEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _ERRORINFO_METADATAENTRY,
                "__module__": "google.rpc.error_details_pb2"
                # @@protoc_insertion_point(class_scope:google.rpc.ErrorInfo.MetadataEntry)
            },
        ),
        "DESCRIPTOR": _ERRORINFO,
        "__module__": "google.rpc.error_details_pb2"
        # @@protoc_insertion_point(class_scope:google.rpc.ErrorInfo)
    },
)
_sym_db.RegisterMessage(ErrorInfo)
_sym_db.RegisterMessage(ErrorInfo.MetadataEntry)

PreconditionFailure = _reflection.GeneratedProtocolMessageType(
    "PreconditionFailure",
    (_message.Message,),
    {
        "Violation": _reflection.GeneratedProtocolMessageType(
            "Violation",
            (_message.Message,),
            {
                "DESCRIPTOR": _PRECONDITIONFAILURE_VIOLATION,
                "__module__": "google.rpc.error_details_pb2"
                # @@protoc_insertion_point(class_scope:google.rpc.PreconditionFailure.Violation)
            },
        ),
        "DESCRIPTOR": _PRECONDITIONFAILURE,
        "__module__": "google.rpc.error_details_pb2"
        # @@protoc_insertion_point(class_scope:google.rpc.PreconditionFailure)
    },
)
_sym_db.RegisterMessage(PreconditionFailure)
_sym_db.RegisterMessage(PreconditionFailure.Violation)

BadRequest = _reflection.GeneratedProtocolMessageType(
    "BadRequest",
    (_message.Message,),
    {
        "FieldViolation": _reflection.GeneratedProtocolMessageType(
            "FieldViolation",
            (_message.Message,),
            {
                "DESCRIPTOR": _BADREQUEST_FIELDVIOLATION,
                "__module__": "google.rpc.error_details_pb2"
                # @@protoc_insertion_point(class_scope:google.rpc.BadRequest.FieldViolation)
            },
        ),
        "DESCRIPTOR": _BADREQUEST,
        "__module__": "google.rpc.error_details_pb2"
        # @@protoc_insertion_point(class_scope:google.rpc.BadRequest)
    },
)
_sym_db.RegisterMessage(BadRequest)
_sym_db.RegisterMessage(BadRequest.FieldViolation)

RequestInfo = _reflection.GeneratedProtocolMessageType(
    "RequestInfo",
    (_message.Message,),
    {
        "DESCRIPTOR": _REQUESTINFO,
        "__module__": "google.rpc.error_details_pb2"
        # @@protoc_insertion_point(class_scope:google.rpc.RequestInfo)
    },
)
_sym_db.RegisterMessage(RequestInfo)

ResourceInfo = _reflection.GeneratedProtocolMessageType(
    "ResourceInfo",
    (_message.Message,),
    {
        "DESCRIPTOR": _RESOURCEINFO,
        "__module__": "google.rpc.error_details_pb2"
        # @@protoc_insertion_point(class_scope:google.rpc.ResourceInfo)
    },
)
_sym_db.RegisterMessage(ResourceInfo)

Help = _reflection.GeneratedProtocolMessageType(
    "Help",
    (_message.Message,),
    {
        "Link": _reflection.GeneratedProtocolMessageType(
            "Link",
            (_message.Message,),
            {
                "DESCRIPTOR": _HELP_LINK,
                "__module__": "google.rpc.error_details_pb2"
                # @@protoc_insertion_point(class_scope:google.rpc.Help.Link)
            },
        ),
        "DESCRIPTOR": _HELP,
        "__module__": "google.rpc.error_details_pb2"
        # @@protoc_insertion_point(class_scope:google.rpc.Help)
    },
)
_sym_db.RegisterMessage(Help)
_sym_db.RegisterMessage(Help.Link)

LocalizedMessage = _reflection.GeneratedProtocolMessageType(
    "LocalizedMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _LOCALIZEDMESSAGE,
        "__module__": "google.rpc.error_details_pb2"
        # @@protoc_insertion_point(class_scope:google.rpc.LocalizedMessage)
    },
)
_sym_db.RegisterMessage(LocalizedMessage)


DESCRIPTOR._options = None
_ERRORINFO_METADATAENTRY._options = None
# @@protoc_insertion_point(module_scope)
