# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stdproj.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='stdproj.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rstdproj.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xd4\x01\n\x12SendStudentRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x12\n\nfirst_name\x18\x02 \x01(\t\x12\x12\n\nlarst_name\x18\x03 \x01(\t\x12\x0f\n\x07sjsu_id\x18\x04 \x01(\t\x12\r\n\x05\x65mail\x18\x05 \x01(\t\x12\x34\n\x10\x63reate_timestamp\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x34\n\x10update_timestamp\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"G\n\x13SendStudentsRequest\x12\x30\n\x13SendStudentsRequest\x18\x01 \x03(\x0b\x32\x13.SendStudentRequest\"\x1e\n\x0bServerReply\x12\x0f\n\x07message\x18\x01 \x01(\t2A\n\x07Greeter\x12\x36\n\x0fSendStudentData\x12\x13.SendStudentRequest\x1a\x0c.ServerReply\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_SENDSTUDENTREQUEST = _descriptor.Descriptor(
  name='SendStudentRequest',
  full_name='SendStudentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='SendStudentRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='first_name', full_name='SendStudentRequest.first_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='larst_name', full_name='SendStudentRequest.larst_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sjsu_id', full_name='SendStudentRequest.sjsu_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='email', full_name='SendStudentRequest.email', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='create_timestamp', full_name='SendStudentRequest.create_timestamp', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='update_timestamp', full_name='SendStudentRequest.update_timestamp', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=51,
  serialized_end=263,
)


_SENDSTUDENTSREQUEST = _descriptor.Descriptor(
  name='SendStudentsRequest',
  full_name='SendStudentsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='SendStudentsRequest', full_name='SendStudentsRequest.SendStudentsRequest', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=265,
  serialized_end=336,
)


_SERVERREPLY = _descriptor.Descriptor(
  name='ServerReply',
  full_name='ServerReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='ServerReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=338,
  serialized_end=368,
)

_SENDSTUDENTREQUEST.fields_by_name['create_timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_SENDSTUDENTREQUEST.fields_by_name['update_timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_SENDSTUDENTSREQUEST.fields_by_name['SendStudentsRequest'].message_type = _SENDSTUDENTREQUEST
DESCRIPTOR.message_types_by_name['SendStudentRequest'] = _SENDSTUDENTREQUEST
DESCRIPTOR.message_types_by_name['SendStudentsRequest'] = _SENDSTUDENTSREQUEST
DESCRIPTOR.message_types_by_name['ServerReply'] = _SERVERREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SendStudentRequest = _reflection.GeneratedProtocolMessageType('SendStudentRequest', (_message.Message,), {
  'DESCRIPTOR' : _SENDSTUDENTREQUEST,
  '__module__' : 'stdproj_pb2'
  # @@protoc_insertion_point(class_scope:SendStudentRequest)
  })
_sym_db.RegisterMessage(SendStudentRequest)

SendStudentsRequest = _reflection.GeneratedProtocolMessageType('SendStudentsRequest', (_message.Message,), {
  'DESCRIPTOR' : _SENDSTUDENTSREQUEST,
  '__module__' : 'stdproj_pb2'
  # @@protoc_insertion_point(class_scope:SendStudentsRequest)
  })
_sym_db.RegisterMessage(SendStudentsRequest)

ServerReply = _reflection.GeneratedProtocolMessageType('ServerReply', (_message.Message,), {
  'DESCRIPTOR' : _SERVERREPLY,
  '__module__' : 'stdproj_pb2'
  # @@protoc_insertion_point(class_scope:ServerReply)
  })
_sym_db.RegisterMessage(ServerReply)



_GREETER = _descriptor.ServiceDescriptor(
  name='Greeter',
  full_name='Greeter',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=370,
  serialized_end=435,
  methods=[
  _descriptor.MethodDescriptor(
    name='SendStudentData',
    full_name='Greeter.SendStudentData',
    index=0,
    containing_service=None,
    input_type=_SENDSTUDENTREQUEST,
    output_type=_SERVERREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_GREETER)

DESCRIPTOR.services_by_name['Greeter'] = _GREETER

# @@protoc_insertion_point(module_scope)
