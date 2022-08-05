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


class WriteSetChange(
    ComposedBase,
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    @classmethod
    @property
    def _discriminator(cls):
        return {
            'type': {
                'WriteSetChange_DeleteModule': WriteSetChangeDeleteModule,
                'WriteSetChange_DeleteResource': WriteSetChangeDeleteResource,
                'WriteSetChange_DeleteTableItem': WriteSetChangeDeleteTableItem,
                'WriteSetChange_WriteModule': WriteSetChangeWriteModule,
                'WriteSetChange_WriteResource': WriteSetChangeWriteResource,
                'WriteSetChange_WriteTableItem': WriteSetChangeWriteTableItem,
                'delete_module': WriteSetChangeDeleteModule,
                'delete_resource': WriteSetChangeDeleteResource,
                'delete_table_item': WriteSetChangeDeleteTableItem,
                'write_module': WriteSetChangeWriteModule,
                'write_resource': WriteSetChangeWriteResource,
                'write_table_item': WriteSetChangeWriteTableItem,
            }
        }

    @classmethod
    @property
    @functools.cache
    def _composed_schemas(cls):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        return {
            'allOf': [
            ],
            'oneOf': [
                WriteSetChangeDeleteModule,
                WriteSetChangeDeleteResource,
                WriteSetChangeDeleteTableItem,
                WriteSetChangeWriteModule,
                WriteSetChangeWriteResource,
                WriteSetChangeWriteTableItem,
            ],
            'anyOf': [
            ],
            'not':
                None
        }

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'WriteSetChange':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from aptos_sdk.model.write_set_change_delete_module import WriteSetChangeDeleteModule
from aptos_sdk.model.write_set_change_delete_resource import WriteSetChangeDeleteResource
from aptos_sdk.model.write_set_change_delete_table_item import WriteSetChangeDeleteTableItem
from aptos_sdk.model.write_set_change_write_module import WriteSetChangeWriteModule
from aptos_sdk.model.write_set_change_write_resource import WriteSetChangeWriteResource
from aptos_sdk.model.write_set_change_write_table_item import WriteSetChangeWriteTableItem
