# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import re  # noqa: F401
import sys  # noqa: F401
import typing
import urllib3
import functools  # noqa: F401
from urllib3._collections import HTTPHeaderDict

from aptos_sdk import api_client, exceptions
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

from aptos_sdk.model.aptos_error import AptosError
from aptos_sdk.model.pending_transaction import PendingTransaction
from aptos_sdk.model.submit_transaction_request import SubmitTransactionRequest

# body param
SchemaForRequestBodyApplicationJson = SubmitTransactionRequest


class SchemaForRequestBodyApplicationXAptosSignedTransactionbcs(
    ListSchema
):
    _items = IntSchema


request_body_submit_transaction_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
        'application/x.aptos.signed_transaction+bcs': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationXAptosSignedTransactionbcs),
    },
    required=True,
)
_path = '/transactions'
_method = 'POST'
XAPTOSCHAINIDSchema = IntSchema
x_aptos_chain_id_parameter = api_client.HeaderParameter(
    name="X-APTOS-CHAIN-ID",
    style=api_client.ParameterStyle.SIMPLE,
    schema=XAPTOSCHAINIDSchema,
    required=True,
)
XAPTOSLEDGERVERSIONSchema = IntSchema
x_aptos_ledger_version_parameter = api_client.HeaderParameter(
    name="X-APTOS-LEDGER-VERSION",
    style=api_client.ParameterStyle.SIMPLE,
    schema=XAPTOSLEDGERVERSIONSchema,
    required=True,
)
XAPTOSLEDGEROLDESTVERSIONSchema = IntSchema
x_aptos_ledger_oldest_version_parameter = api_client.HeaderParameter(
    name="X-APTOS-LEDGER-OLDEST-VERSION",
    style=api_client.ParameterStyle.SIMPLE,
    schema=XAPTOSLEDGEROLDESTVERSIONSchema,
    required=True,
)
XAPTOSLEDGERTIMESTAMPUSECSchema = IntSchema
x_aptos_ledger_timestampusec_parameter = api_client.HeaderParameter(
    name="X-APTOS-LEDGER-TIMESTAMPUSEC",
    style=api_client.ParameterStyle.SIMPLE,
    schema=XAPTOSLEDGERTIMESTAMPUSECSchema,
    required=True,
)
XAPTOSEPOCHSchema = IntSchema
x_aptos_epoch_parameter = api_client.HeaderParameter(
    name="X-APTOS-EPOCH",
    style=api_client.ParameterStyle.SIMPLE,
    schema=XAPTOSEPOCHSchema,
    required=True,
)
SchemaFor202ResponseBodyApplicationJson = PendingTransaction


class SchemaFor202ResponseBodyApplicationXBcs(
    ListSchema
):
    _items = IntSchema
ResponseHeadersFor202 = typing.TypedDict(
    'ResponseHeadersFor202',
    {
        'X-APTOS-CHAIN-ID': XAPTOSCHAINIDSchema,
        'X-APTOS-LEDGER-VERSION': XAPTOSLEDGERVERSIONSchema,
        'X-APTOS-LEDGER-OLDEST-VERSION': XAPTOSLEDGEROLDESTVERSIONSchema,
        'X-APTOS-LEDGER-TIMESTAMPUSEC': XAPTOSLEDGERTIMESTAMPUSECSchema,
        'X-APTOS-EPOCH': XAPTOSEPOCHSchema,
    }
)


@dataclass
class ApiResponseFor202(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor202ResponseBodyApplicationJson,
        SchemaFor202ResponseBodyApplicationXBcs,
    ]
    headers: ResponseHeadersFor202


_response_for_202 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor202,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor202ResponseBodyApplicationJson),
        'application/x-bcs': api_client.MediaType(
            schema=SchemaFor202ResponseBodyApplicationXBcs),
    },
    headers=[
        x_aptos_chain_id_parameter,
        x_aptos_ledger_version_parameter,
        x_aptos_ledger_oldest_version_parameter,
        x_aptos_ledger_timestampusec_parameter,
        x_aptos_epoch_parameter,
    ]
)
SchemaFor400ResponseBodyApplicationJson = AptosError


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor400ResponseBodyApplicationJson,
    ]
    headers: Unset = unset


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor413ResponseBodyApplicationJson = AptosError


@dataclass
class ApiResponseFor413(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor413ResponseBodyApplicationJson,
    ]
    headers: Unset = unset


_response_for_413 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor413,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor413ResponseBodyApplicationJson),
    },
)
SchemaFor500ResponseBodyApplicationJson = AptosError


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor500ResponseBodyApplicationJson,
    ]
    headers: Unset = unset


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationJson),
    },
)
SchemaFor507ResponseBodyApplicationJson = AptosError


@dataclass
class ApiResponseFor507(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor507ResponseBodyApplicationJson,
    ]
    headers: Unset = unset


_response_for_507 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor507,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor507ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '202': _response_for_202,
    '400': _response_for_400,
    '413': _response_for_413,
    '500': _response_for_500,
    '507': _response_for_507,
}
_all_accept_content_types = (
    'application/json',
    'application/x-bcs',
)


class SubmitTransaction(api_client.Api):

    def submit_transaction(
        self: api_client.Api,
        body: typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationXAptosSignedTransactionbcs],
        content_type: str = 'application/json',
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor202,
        api_client.ApiResponseWithoutDeserialization
    ]:
        """
        Submit transaction
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = _path

        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)

        if body is unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        serialized_data = request_body_submit_transaction_request.serialize(body, content_type)
        _headers.add('Content-Type', content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
        response = self.api_client.call_api(
            resource_path=used_path,
            method=_method,
            headers=_headers,
            fields=_fields,
            body=_body,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)

        return api_response
