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


class TableItemRequest(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    _required_property_names = set((
        'key_type',
        'value_type',
        'key',
    ))

    @classmethod
    @property
    def key_type(cls) -> typing.Type['MoveType']:
        return MoveType

    @classmethod
    @property
    def value_type(cls) -> typing.Type['MoveType']:
        return MoveType
    key = AnyTypeSchema


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        key_type: key_type,
        value_type: value_type,
        key: key,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'TableItemRequest':
        return super().__new__(
            cls,
            *args,
            key_type=key_type,
            value_type=value_type,
            key=key,
            _configuration=_configuration,
            **kwargs,
        )

from aptos_sdk.model.move_type import MoveType
