// Copyright (c) Aptos
// SPDX-License-Identifier: Apache-2.0

use crate::protos::extractor;
use aptos_api_types::{
    Event, GenesisPayload, MoveModuleId, ScriptPayload, Transaction, TransactionInfo,
    TransactionPayload, WriteSet, WriteSetChange,
};

pub fn convert_move_module_id(move_module_id: &MoveModuleId) -> extractor::MoveModuleId {
    extractor::MoveModuleId {
        address: move_module_id.address.to_string(),
        name: move_module_id.name.to_string(),
        special_fields: Default::default(),
    }
}

pub fn convert_transaction_payload(payload: &TransactionPayload) -> extractor::TransactionPayload {
    match payload {
        TransactionPayload::ScriptFunctionPayload(sfp) => extractor::TransactionPayload {
            type_: protobuf::EnumOrUnknown::new(
                extractor::transaction_payload::PayloadType::SCRIPT_FUNCTION_PAYLOAD,
            ),
            payload: Some(
                extractor::transaction_payload::Payload::ScriptFunctionPayload(
                    extractor::ScriptFunctionPayload {
                        function: protobuf::MessageField::some(extractor::ScriptFunctionId {
                            module: protobuf::MessageField::some(convert_move_module_id(
                                &sfp.function.module,
                            )),
                            name: sfp.function.name.to_string(),
                            special_fields: Default::default(),
                        }),
                        type_arguments: sfp
                            .type_arguments
                            .iter()
                            .map(|move_type| move_type.to_string())
                            .collect(),
                        arguments: sfp
                            .arguments
                            .iter()
                            .map(|move_value| move_value.to_string())
                            .collect(),
                        special_fields: Default::default(),
                    },
                ),
            ),
            special_fields: Default::default(),
        },
        TransactionPayload::ScriptPayload(sp) => extractor::TransactionPayload {
            type_: protobuf::EnumOrUnknown::new(
                extractor::transaction_payload::PayloadType::SCRIPT_PAYLOAD,
            ),
            payload: Some(extractor::transaction_payload::Payload::ScriptPayload(
                extractor::ScriptPayload {
                    code: sp.code.bytecode.to_string(),
                    type_arguments: sp
                        .type_arguments
                        .iter()
                        .map(|move_type| move_type.to_string())
                        .collect(),
                    arguments: sp
                        .arguments
                        .iter()
                        .map(|move_value| move_value.to_string())
                        .collect(),
                    special_fields: Default::default(),
                },
            )),
            special_fields: Default::default(),
        },
        TransactionPayload::ModuleBundlePayload(mbp) => extractor::TransactionPayload {
            type_: protobuf::EnumOrUnknown::new(
                extractor::transaction_payload::PayloadType::MODULE_BUNDLE_PAYLOAD,
            ),
            payload: Some(
                extractor::transaction_payload::Payload::ModuleBundlePayload(
                    extractor::ModuleBundlePayload {
                        modules: mbp
                            .modules
                            .iter()
                            .map(|module| module.bytecode.to_string())
                            .collect(),
                        special_fields: Default::default(),
                    },
                ),
            ),
            special_fields: Default::default(),
        },
        TransactionPayload::WriteSetPayload(wsp) => extractor::TransactionPayload {
            type_: protobuf::EnumOrUnknown::new(
                extractor::transaction_payload::PayloadType::WRITE_SET_PAYLOAD,
            ),
            payload: Some(extractor::transaction_payload::Payload::WriteSetPayload(
                extractor::WriteSetPayload {
                    write_set: convert_write_set(&wsp.write_set),
                    special_fields: Default::default(),
                },
            )),
            special_fields: Default::default(),
        },
    }
}

pub fn convert_write_set(write_set: &WriteSet) -> protobuf::MessageField<extractor::WriteSet> {
    let (write_set_type, write_set) = match write_set {
        WriteSet::ScriptWriteSet(sws) => {
            let write_set_type =
                protobuf::EnumOrUnknown::new(extractor::write_set::WriteSetType::SCRIPT_WRITE_SET);

            let write_set =
                extractor::write_set::Write_set::ScriptWriteSet(extractor::ScriptWriteSet {
                    execute_as: sws.execute_as.to_string(),
                    script: protobuf::MessageField::some(convert_script_payload(&sws.script)),
                    special_fields: Default::default(),
                });
            (write_set_type, Some(write_set))
        }
        WriteSet::DirectWriteSet(dws) => {
            let write_set_type =
                protobuf::EnumOrUnknown::new(extractor::write_set::WriteSetType::DIRECT_WRITE_SET);

            let write_set =
                extractor::write_set::Write_set::DirectWriteSet(extractor::DirectWriteSet {
                    write_set_change: dws
                        .changes
                        .iter()
                        .map(|change| convert_write_set_change(change))
                        .collect(),
                    events: dws
                        .events
                        .iter()
                        .map(|event| convert_event(event))
                        .collect(),
                    special_fields: Default::default(),
                });
            (write_set_type, Some(write_set))
        }
    };
    protobuf::MessageField::some(extractor::WriteSet {
        write_set_type,
        write_set,
        special_fields: Default::default(),
    })
}

pub fn convert_write_set_change(change: &WriteSetChange) -> extractor::WriteSetChange {
    match change {
        WriteSetChange::DeleteModule(delete_module) => extractor::WriteSetChange {
            type_: protobuf::EnumOrUnknown::new(
                extractor::write_set_change::WriteSetChangeType::DELETE_MODULE,
            ),
            change: Some(extractor::write_set_change::Change::DeleteModule(
                extractor::DeleteModule {
                    address: delete_module.address.to_string(),
                    state_key_hash: delete_module.state_key_hash.to_string(),
                    module: protobuf::MessageField::some(extractor::MoveModuleId {
                        address: delete_module.module.address.to_string(),
                        name: delete_module.module.name.to_string(),
                        special_fields: Default::default(),
                    }),
                    special_fields: Default::default(),
                },
            )),
            special_fields: Default::default(),
        },
        WriteSetChange::DeleteResource(delete_resource) => extractor::WriteSetChange {
            type_: protobuf::EnumOrUnknown::new(
                extractor::write_set_change::WriteSetChangeType::DELETE_RESOURCE,
            ),
            change: Some(extractor::write_set_change::Change::DeleteResource(
                extractor::DeleteResource {
                    address: delete_resource.address.to_string(),
                    state_key_hash: delete_resource.state_key_hash.to_string(),
                    resource: protobuf::MessageField::some(extractor::MoveStructTag {
                        address: delete_resource.address.to_string(),
                        module: delete_resource.resource.module.to_string(),
                        name: delete_resource.resource.name.to_string(),
                        generic_type_params: delete_resource
                            .resource
                            .generic_type_params
                            .iter()
                            .map(|move_type| move_type.to_string())
                            .collect(),
                        special_fields: Default::default(),
                    }),
                    special_fields: Default::default(),
                },
            )),
            special_fields: Default::default(),
        },
        WriteSetChange::DeleteTableItem(delete_table_item) => extractor::WriteSetChange {
            type_: protobuf::EnumOrUnknown::new(
                extractor::write_set_change::WriteSetChangeType::DELETE_TABLE_ITEM,
            ),
            change: Some(extractor::write_set_change::Change::DeleteTableItem(
                extractor::DeleteTableItem {
                    state_key_hash: delete_table_item.state_key_hash.to_string(),
                    handle: delete_table_item.handle.to_string(),
                    key: delete_table_item.key.to_string(),
                    special_fields: Default::default(),
                },
            )),
            special_fields: Default::default(),
        },
        WriteSetChange::WriteModule(write_module) => extractor::WriteSetChange {
            type_: protobuf::EnumOrUnknown::new(
                extractor::write_set_change::WriteSetChangeType::DELETE_MODULE,
            ),
            change: Some(extractor::write_set_change::Change::WriteModule(
                extractor::WriteModule {
                    address: write_module.address.to_string(),
                    state_key_hash: write_module.state_key_hash.to_string(),
                    data: write_module.data.bytecode.to_string(),
                    special_fields: Default::default(),
                },
            )),
            special_fields: Default::default(),
        },
        WriteSetChange::WriteResource(write_resource) => extractor::WriteSetChange {
            type_: protobuf::EnumOrUnknown::new(
                extractor::write_set_change::WriteSetChangeType::WRITE_RESOURCE,
            ),
            change: Some(extractor::write_set_change::Change::WriteResource(
                extractor::WriteResource {
                    address: write_resource.address.to_string(),
                    state_key_hash: write_resource.state_key_hash.to_string(),
                    data: protobuf::MessageField::some(extractor::MoveResource {
                        type_: protobuf::MessageField::some(extractor::MoveStructTag {
                            address: write_resource.data.typ.address.to_string(),
                            module: write_resource.data.typ.module.to_string(),
                            name: write_resource.data.typ.name.to_string(),
                            generic_type_params: write_resource
                                .data
                                .typ
                                .generic_type_params
                                .iter()
                                .map(|move_type| move_type.to_string())
                                .collect(),
                            special_fields: Default::default(),
                        }),
                        data: serde_json::to_string(&write_resource.data.data).unwrap(),
                        special_fields: Default::default(),
                    }),
                    special_fields: Default::default(),
                },
            )),
            special_fields: Default::default(),
        },
        WriteSetChange::WriteTableItem(write_table_item) => extractor::WriteSetChange {
            type_: protobuf::EnumOrUnknown::new(
                extractor::write_set_change::WriteSetChangeType::WRITE_TABLE_ITEM,
            ),
            change: Some(extractor::write_set_change::Change::WriteTableItem(
                extractor::WriteTableItem {
                    state_key_hash: write_table_item.state_key_hash.to_string(),
                    handle: write_table_item.handle.to_string(),
                    key: write_table_item.key.to_string(),
                    value: write_table_item.value.to_string(),
                    special_fields: Default::default(),
                },
            )),
            special_fields: Default::default(),
        },
    }
}

pub fn convert_script_payload(script_payload: &ScriptPayload) -> extractor::ScriptPayload {
    extractor::ScriptPayload {
        code: script_payload.code.bytecode.to_string(),
        type_arguments: script_payload
            .type_arguments
            .iter()
            .map(|move_type| move_type.to_string())
            .collect(),
        arguments: script_payload
            .arguments
            .iter()
            .map(|move_value| move_value.to_string())
            .collect(),
        special_fields: Default::default(),
    }
}

pub fn convert_event(event: &Event) -> extractor::Event {
    extractor::Event {
        key: protobuf::MessageField::some(extractor::EventKey {
            creation_number: event.key.0.get_creation_number(),
            account_address: event.key.0.get_creator_address().to_string(),
            special_fields: Default::default(),
        }),
        sequence_number: event.sequence_number.0,
        type_: event.typ.to_string(),
        data: event.data.to_string(),
        special_fields: Default::default(),
    }
}

pub fn convert_transaction_info(transaction_info: &TransactionInfo) -> extractor::TransactionInfo {
    extractor::TransactionInfo {
        hash: transaction_info.hash.to_string(),
        state_root_hash: transaction_info.state_root_hash.to_string(),
        event_root_hash: transaction_info.event_root_hash.to_string(),
        gas_used: transaction_info.gas_used.0,
        success: transaction_info.success,
        vm_status: transaction_info.vm_status.to_string(),
        accumulator_root_hash: transaction_info.accumulator_root_hash.to_string(),
        changes: transaction_info
            .changes
            .iter()
            .map(|change| convert_write_set_change(change))
            .collect(),
        special_fields: Default::default(),
    }
}

pub fn convert_transaction(
    transaction: &Transaction,
    block_height: u64,
    current_epoch: u64,
) -> extractor::Transaction {
    let txn_type = match transaction {
        Transaction::UserTransaction(_) => extractor::transaction::TransactionType::USER,
        Transaction::GenesisTransaction(_) => extractor::transaction::TransactionType::GENESIS,
        Transaction::BlockMetadataTransaction(_) => {
            extractor::transaction::TransactionType::BLOCK_METADATA
        }
        Transaction::StateCheckpointTransaction(_) => {
            extractor::transaction::TransactionType::STATE_CHECKPOINT
        }
        Transaction::PendingTransaction(_) => panic!("PendingTransaction is not supported"),
    };

    let txn_data = match &transaction {
        Transaction::UserTransaction(ut) => {
            extractor::transaction::Txn_data::UserTxn(extractor::UserTransaction {
                request: protobuf::MessageField::some(extractor::UserTransactionRequest {
                    sender: ut.request.sender.to_string(),
                    sequence_number: ut.request.sequence_number.0,
                    max_gas_amount: ut.request.max_gas_amount.0,
                    gas_unit_price: ut.request.gas_unit_price.0,
                    expiration_timestamp_secs: ut.request.expiration_timestamp_secs.0,
                    payload: protobuf::MessageField::some(convert_transaction_payload(
                        &ut.request.payload,
                    )),
                    signature: Default::default(),
                    special_fields: Default::default(),
                }),
                events: ut.events.iter().map(|event| convert_event(event)).collect(),
                special_fields: Default::default(),
            })
        }
        Transaction::GenesisTransaction(gt) => {
            let payload = match &gt.payload {
                GenesisPayload::WriteSetPayload(wsp) => convert_write_set(&wsp.write_set),
            };
            extractor::transaction::Txn_data::GenesisTxn(extractor::GenesisTransaction {
                payload,
                events: gt.events.iter().map(|event| convert_event(event)).collect(),
                special_fields: Default::default(),
            })
        }
        Transaction::BlockMetadataTransaction(bm) => {
            extractor::transaction::Txn_data::BlockMetadataTxn(
                extractor::BlockMetadataTransaction {
                    id: bm.id.to_string(),
                    events: bm.events.iter().map(|event| convert_event(event)).collect(),
                    previous_block_votes: bm.previous_block_votes.clone(),
                    proposer: bm.proposer.to_string(),
                    failed_proposer_indices: bm.failed_proposer_indices.clone(),
                    round: bm.round.0,
                    special_fields: Default::default(),
                },
            )
        }
        Transaction::StateCheckpointTransaction(_st) => {
            extractor::transaction::Txn_data::StateCheckpointTxn(
                extractor::StateCheckpointTransaction {
                    special_fields: Default::default(),
                },
            )
        }
        Transaction::PendingTransaction(_) => panic!("PendingTransaction not supported"),
    };

    extractor::Transaction {
        timestamp: transaction.timestamp(),
        version: transaction.version().unwrap(),
        info: protobuf::MessageField::some(convert_transaction_info(
            transaction.transaction_info().unwrap(),
        )),
        // TODO: keep track of the epoch as we iterate through BlockMetadata
        epoch: current_epoch,
        block_height,
        type_: protobuf::EnumOrUnknown::new(txn_type),
        txn_data: Some(txn_data),
        special_fields: Default::default(),
    }
}