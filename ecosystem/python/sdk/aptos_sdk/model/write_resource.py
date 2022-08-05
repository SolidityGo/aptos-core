# coding: utf-8

"""
    Aptos Node API

    The Aptos Node API is a RESTful API for client applications to interact with the Aptos blockchain.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

import re  # noqa: F401
import sys  # noqa: F401
import typing  # noqa: F401
import functools  # noqa: F401

from frozendict import frozendict  # noqa: F401

import decimal  # noqa: F401
from datetime import date, datetime  # noqa: F401
from frozendict import frozendict  # noqa: F401

from aptos_sdk.schemas import (  # noqa: F401
    AnyTypeSchema,
    ComposedSchema,
    DictSchema,
    ListSchema,
    StrSchema,
    IntSchema,
    Int32Schema,
    Int64Schema,
    Float32Schema,
    Float64Schema,
    NumberSchema,
    UUIDSchema,
    DateSchema,
    DateTimeSchema,
    DecimalSchema,
    BoolSchema,
    BinarySchema,
    NoneSchema,
    none_type,
    Configuration,
    Unset,
    unset,
    ComposedBase,
    ListBase,
    DictBase,
    NoneBase,
    StrBase,
    IntBase,
    Int32Base,
    Int64Base,
    Float32Base,
    Float64Base,
    NumberBase,
    UUIDBase,
    DateBase,
    DateTimeBase,
    BoolBase,
    BinaryBase,
    Schema,
    _SchemaValidator,
    _SchemaTypeChecker,
    _SchemaEnumMaker
)


class WriteResource(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    _required_property_names = set((
        'address',
        'state_key_hash',
        'data',
    ))
    address = StrSchema
    state_key_hash = StrSchema

    @classmethod
    @property
    def data(cls) -> typing.Type['MoveResource']:
        return MoveResource


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        address: address,
        state_key_hash: state_key_hash,
        data: data,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'WriteResource':
        return super().__new__(
            cls,
            *args,
            address=address,
            state_key_hash=state_key_hash,
            data=data,
            _configuration=_configuration,
            **kwargs,
        )

from aptos_sdk.model.move_resource import MoveResource
