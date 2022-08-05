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


class BlockMetadataTransaction(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    _required_property_names = set((
        'version',
        'hash',
        'state_root_hash',
        'event_root_hash',
        'gas_used',
        'success',
        'vm_status',
        'accumulator_root_hash',
        'changes',
        'id',
        'epoch',
        'round',
        'events',
        'previous_block_votes',
        'proposer',
        'failed_proposer_indices',
        'timestamp',
    ))
    version = StrSchema
    hash = StrSchema
    state_root_hash = StrSchema
    event_root_hash = StrSchema
    gas_used = StrSchema
    success = BoolSchema
    vm_status = StrSchema
    accumulator_root_hash = StrSchema
    
    
    class changes(
        ListSchema
    ):
    
        @classmethod
        @property
        def _items(cls) -> typing.Type['WriteSetChange']:
            return WriteSetChange
    id = StrSchema
    epoch = StrSchema
    round = StrSchema
    
    
    class events(
        ListSchema
    ):
    
        @classmethod
        @property
        def _items(cls) -> typing.Type['Event']:
            return Event
    
    
    class previous_block_votes(
        ListSchema
    ):
        _items = BoolSchema
    proposer = StrSchema
    
    
    class failed_proposer_indices(
        ListSchema
    ):
        _items = IntSchema
    timestamp = StrSchema


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        version: version,
        hash: hash,
        state_root_hash: state_root_hash,
        event_root_hash: event_root_hash,
        gas_used: gas_used,
        success: success,
        vm_status: vm_status,
        accumulator_root_hash: accumulator_root_hash,
        changes: changes,
        id: id,
        epoch: epoch,
        round: round,
        events: events,
        previous_block_votes: previous_block_votes,
        proposer: proposer,
        failed_proposer_indices: failed_proposer_indices,
        timestamp: timestamp,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'BlockMetadataTransaction':
        return super().__new__(
            cls,
            *args,
            version=version,
            hash=hash,
            state_root_hash=state_root_hash,
            event_root_hash=event_root_hash,
            gas_used=gas_used,
            success=success,
            vm_status=vm_status,
            accumulator_root_hash=accumulator_root_hash,
            changes=changes,
            id=id,
            epoch=epoch,
            round=round,
            events=events,
            previous_block_votes=previous_block_votes,
            proposer=proposer,
            failed_proposer_indices=failed_proposer_indices,
            timestamp=timestamp,
            _configuration=_configuration,
            **kwargs,
        )

from aptos_sdk.model.event import Event
from aptos_sdk.model.write_set_change import WriteSetChange
