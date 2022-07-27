// Copyright (c) Aptos
// SPDX-License-Identifier: Apache-2.0

use aptos_metrics_core::{register_int_counter, IntCounter};
use once_cell::sync::Lazy;

pub static TRANSACTIONS_SENT: Lazy<IntCounter> = Lazy::new(|| {
    register_int_counter!(
        "aptos_sf_stream_transactions_sent_count",
        "Transactions taken from the channel and pushed out to the SF server",
    )
    .unwrap()
});

pub static TRANSACTIONS_QUEUED: Lazy<IntCounter> = Lazy::new(|| {
    register_int_counter!(
        "aptos_sf_stream_transactions_queued_count",
        "Transactions enqueued in the channel",
    )
    .unwrap()
});