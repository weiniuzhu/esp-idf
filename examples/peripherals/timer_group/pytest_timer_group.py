# SPDX-FileCopyrightText: 2021 Espressif Systems (Shanghai) CO LTD
# SPDX-License-Identifier: CC0-1.0

import pytest
from pytest_embedded.dut import Dut


@pytest.mark.esp32
@pytest.mark.esp32s2
@pytest.mark.esp32s3
@pytest.mark.esp32c3
@pytest.mark.generic
def test_timer_group_example(dut: Dut):  # type: ignore
    dut.expect(r'Init timer with auto-reload', timeout=5)
    res = dut.expect(r'Timer auto reloaded, count value in ISR: (\d+)', timeout=5)
    reloaded_count = res.group(1).decode('utf8')
    assert 0 <= int(reloaded_count) < 10

    alarm_increase_step = 500000
    dut.expect(r'Init timer without auto-reload')
    for i in range(1, 5):
        res = dut.expect(r'Timer alarmed at (\d+)', timeout=3)
        alarm_count = res.group(1).decode('utf8')
        assert (i * alarm_increase_step - 10) < int(alarm_count) < (i * alarm_increase_step + 10)
