# DLCsmartTHz_V3_0_0.py

## Install

```
pip install toptica-lasersdk
```

The only requirement. 

## How the file works

Everything hangs off one class, `DLCsmartTHz`:

```
dlc
├── general            identity and firmware
├── laser_operation    interlock, key, emission
│   ├── laser1
│   └── laser2
├── frequency          THz tuning and fast scan
├── lockin             modulation, integration, readings
│   └── fast_phase_modulation    fiber stretcher sweep and fit
├── net_conf           IP configuration
└── ul                 user level
```

## Connecting

```python
from DLCsmartTHz_V3_0_0 import DLCsmartTHz, NetworkConnection

with DLCsmartTHz(NetworkConnection("1.1.1.2", timeout=15)) as dlc:
    print(dlc.general.fw_ver.get())
```

`DLCsmartTHz(connection)` takes one argument, a connection object re-exported from the
SDK by this file:

- `NetworkConnection(host, command_line_port=1998, monitoring_line_port=1999, timeout=5)`
  — Ethernet. The host is the controller's IP, visible in the TeraScan GUI under
  *DLC smart -> Connection settings*.

| Method | Parameters | What it does |
|---|---|---|
| `open()` | none | Open the connection |
| `close()` | none | Close connection |
| `run(timeout=None)` | `timeout` (int, seconds) | Run the SDK event loop, for subscriptions |
| `stop()` | none | Stop the event loop |
| `poll()` | none | Service pending events once |

---

## `dlc.general`

| Parameter | Type | Access |
|---|---|---|
| `serial_number` | str | read |
| `system_type` | str | read |
| `system_label` | str | read/write |
| `system_manufacturer` | str | read |
| `fw_ver` | str | read |

```python
print(dlc.general.serial_number.get(), dlc.general.fw_ver.get())
dlc.general.system_label.set("THz bench, room 214")
```

---

## `dlc.laser_operation`

| Parameter | Type | Access | Meaning |
|---|---|---|---|
| `interlock_open` | bool | read | True means the interlock is open and emission is blocked |
| `frontkey_locked` | bool | read | True means the physical key is locked |
| `emission_global_enable` | bool | read/write | Master arm |
| `emission` | bool | read | Whether light is actually coming out |

`laser1` and `laser2` each carry two more:

| Parameter | Type | Access |
|---|---|---|
| `emission_enable` | bool | read/write |
| `emission` | bool | read |

Turning on takes four conditions: interlock closed, key unlocked, global enable set,
both per-laser enables set. The first two are hardware and cannot be overridden from
software.

```python
if dlc.laser_operation.interlock_open.get():
    raise RuntimeError("interlock open")
if dlc.laser_operation.frontkey_locked.get():
    raise RuntimeError("front key locked")

dlc.laser_operation.laser1.emission_enable.set(True)
dlc.laser_operation.laser2.emission_enable.set(True)
dlc.laser_operation.emission_global_enable.set(True)
```

`emission_enable` is a request and `emission` is the answer; they are not the same thing.
Poll `emission` until it reads True rather than sleeping a fixed time.

---

## `dlc.frequency`

Frequencies in GHz.

| Parameter | Type | Access | Meaning |
|---|---|---|---|
| `frequency_set` | float | read/write | Target frequency |
| `frequency_act` | float | read | Where the lasers actually are |
| `frequency_min` | float | read/write | Lower limit of a fast scan |
| `frequency_max` | float | read/write | Upper limit of a fast scan |
| `frequency_step` | float | read/write | Step size |
| `scan_mode_fast` | bool | read/write | Switch between stepped and fast-scan behaviour |
| `fast_scan_isscanning` | bool | read | True while a fast scan is running |

| Method | Parameters | Returns |
|---|---|---|
| `fast_scan_start()` | none | int status |
| `fast_scan_stop()` | none | int status |
| `fast_scan_clear_data()` | none | int status |
| `fast_scan_get_data(curveNo, startIndex, length)` | all int | `bytes` |


### Stepping to a frequency

```python
dlc.frequency.frequency_set.set(650.0)
```

Writing `frequency_set` returns immediately; the lasers take time to arrive. Reading the
lock-in before `frequency_act` has settled attributes the measurement to the wrong
frequency.


### Fast scan

```python
dlc.frequency.frequency_min.set(600.0)
dlc.frequency.frequency_max.set(1200.0)
dlc.frequency.frequency_step.set(0.5)
dlc.frequency.fast_scan_clear_data()
dlc.frequency.fast_scan_start()

while dlc.frequency.fast_scan_isscanning.get():
    time.sleep(0.5)

raw = dlc.frequency.fast_scan_get_data(0, 0, 4096)
```

---

## `dlc.lockin`

| Parameter | Type | Access | Meaning |
|---|---|---|---|
| `frequency` | float | read/write | Modulation (chopping) frequency, Hz |
| `phase` | float | read/write | Reference phase |
| `integration_time` | float | read/write | Per-point integration |
| `integration_time_step` | float | read | Granularity the hardware quantises to |
| `integration_time_must_match_modulation_frequency` | bool | read/write | Constrain integration to whole modulation periods |
| `integration_time_matches_modulation_frequency` | bool | read | Whether it currently does |
| `mod_out_amplitude` | float | read/write | Modulation output amplitude |
| `mod_out_offset` | float | read/write | Modulation output offset |
| `mod_out_amplitude_default` | float | read | Factory default |
| `mod_out_offset_default` | float | read | Factory default |
| `amplifier_gain` | float | read/write | Transimpedance gain, volts per amp |
| `lock_in_value` | (float, bool) | read | Reading in volts, with a validity flag |
| `lock_in_value_nanoamp` | (float, bool) | read | Same reading in nA |

| Method | Parameters | Returns |
|---|---|---|
| `mod_out_set_to_default()` | none | int status |
| `mod_out_set_to_zero()` | none | int status |
| `lock_in_reset()` | none | int status |

### Chopping frequency and integration time

```python
dlc.lockin.frequency.set(1000.0)
dlc.lockin.integration_time.set(0.080)

print(dlc.lockin.integration_time.get())                                  # may differ
print(dlc.lockin.integration_time_matches_modulation_frequency.get())
```

The hardware quantises integration time to `integration_time_step`, and quantises it
further when `integration_time_must_match_modulation_frequency` is set. 

### Reading a value

```python
value, valid = dlc.lockin.lock_in_value_nanoamp.get()
```

Both value parameters return a two-element tuple, not a number. The second element is a
flag the controller clears while a conversion is mid-cycle, which is common right after a
frequency step. Ignoring it mixes stale readings into your data silently.

Units for `mod_out_amplitude`, `mod_out_offset` and `amplifier_gain` are not stated
anywhere in this file. Check the Remote Command Reference on the TOPTICA memory stick
before relying on them.

---

## `dlc.lockin.fast_phase_modulation`

The fiber stretcher block: it sweeps optical phase and fits a sine to the fringes,
producing the GUI's *(via StrMod)* columns. Not needed for plain stepped acquisition.

| Parameter | Type | Access |
|---|---|---|
| `enabled` | bool | read/write |
| `data_valid` | bool | read |
| `raw_data_monitored_phase_volt` | bytes | read |
| `raw_data_photocurrent_volt` | bytes | read |
| `raw_data_photocurrent_nanoamp` | bytes | read |
| `fit_data` | 6-tuple | read |
| `fit_data_amplitude_volt` | float | read |
| `fit_data_amplitude_nanoamp` | float | read |
| `fit_data_phase` | float | read |
| `fit_data_chi_square` | float | read |

Methods: `clear()` and `stop_acquisition()`, both no parameters, both returning int.

```python
fpm = dlc.lockin.fast_phase_modulation
fpm.enabled.set(False); time.sleep(0.3)
fpm.enabled.set(True);  time.sleep(0.3)
fpm.clear()

a0, a1, a2, a3, chi2, fitok = fpm.fit_data.get()
```
---

