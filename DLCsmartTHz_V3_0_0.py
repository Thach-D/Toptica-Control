# Generated from 'device-control.xml' on 2019-03-26 15:24:49.618501

from typing import Tuple

from toptica.lasersdk.client import UserLevel
from toptica.lasersdk.client import Client

from toptica.lasersdk.client import DecopBoolean
from toptica.lasersdk.client import DecopInteger
from toptica.lasersdk.client import DecopReal
from toptica.lasersdk.client import DecopString
from toptica.lasersdk.client import DecopBinary

from toptica.lasersdk.client import MutableDecopBoolean
from toptica.lasersdk.client import MutableDecopInteger
from toptica.lasersdk.client import MutableDecopReal
from toptica.lasersdk.client import MutableDecopString
from toptica.lasersdk.client import MutableDecopBinary

from toptica.lasersdk.client import Connection
from toptica.lasersdk.client import NetworkConnection
from toptica.lasersdk.client import SerialConnection

from toptica.lasersdk.client import DecopError
from toptica.lasersdk.client import DeviceNotFoundError


class CwterahertzGeneral:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._serial_number = DecopString(client, name + ':serial-number')
        self._system_type = DecopString(client, name + ':system-type')
        self._system_label = MutableDecopString(client, name + ':system-label')
        self._system_manufacturer = DecopString(client, name + ':system-manufacturer')
        self._fw_ver = DecopString(client, name + ':fw-ver')

    @property
    def serial_number(self) -> 'DecopString':
        return self._serial_number

    @property
    def system_type(self) -> 'DecopString':
        return self._system_type

    @property
    def system_label(self) -> 'MutableDecopString':
        return self._system_label

    @property
    def system_manufacturer(self) -> 'DecopString':
        return self._system_manufacturer

    @property
    def fw_ver(self) -> 'DecopString':
        return self._fw_ver

    def legal_info(self) -> bytes:
        return self.__client.exec(self.__name + ':legal-info', input_stream=None, output_type=bytes, return_type=None)


class DlcsmartLaserOperation:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._interlock_open = DecopBoolean(client, name + ':interlock-open')
        self._frontkey_locked = DecopBoolean(client, name + ':frontkey-locked')
        self._emission_global_enable = MutableDecopBoolean(client, name + ':emission-global-enable')
        self._emission = DecopBoolean(client, name + ':emission')
        self._laser1 = DlcsmartLaserOperationLaser(client, name + ':laser1')
        self._laser2 = DlcsmartLaserOperationLaser(client, name + ':laser2')

    @property
    def interlock_open(self) -> 'DecopBoolean':
        return self._interlock_open

    @property
    def frontkey_locked(self) -> 'DecopBoolean':
        return self._frontkey_locked

    @property
    def emission_global_enable(self) -> 'MutableDecopBoolean':
        return self._emission_global_enable

    @property
    def emission(self) -> 'DecopBoolean':
        return self._emission

    @property
    def laser1(self) -> 'DlcsmartLaserOperationLaser':
        return self._laser1

    @property
    def laser2(self) -> 'DlcsmartLaserOperationLaser':
        return self._laser2


class DlcsmartLaserOperationLaser:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._emission_enable = MutableDecopBoolean(client, name + ':emission-enable')
        self._emission = DecopBoolean(client, name + ':emission')

    @property
    def emission_enable(self) -> 'MutableDecopBoolean':
        return self._emission_enable

    @property
    def emission(self) -> 'DecopBoolean':
        return self._emission


class CwterahertzFrequency:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._scan_mode_fast = MutableDecopBoolean(client, name + ':scan-mode-fast')
        self._frequency_set = MutableDecopReal(client, name + ':frequency-set')
        self._frequency_min = MutableDecopReal(client, name + ':frequency-min')
        self._frequency_max = MutableDecopReal(client, name + ':frequency-max')
        self._frequency_step = MutableDecopReal(client, name + ':frequency-step')
        self._frequency_act = DecopReal(client, name + ':frequency-act')
        self._fast_scan_isscanning = DecopBoolean(client, name + ':fast-scan-isscanning')

    @property
    def scan_mode_fast(self) -> 'MutableDecopBoolean':
        return self._scan_mode_fast

    @property
    def frequency_set(self) -> 'MutableDecopReal':
        return self._frequency_set

    @property
    def frequency_min(self) -> 'MutableDecopReal':
        return self._frequency_min

    @property
    def frequency_max(self) -> 'MutableDecopReal':
        return self._frequency_max

    @property
    def frequency_step(self) -> 'MutableDecopReal':
        return self._frequency_step

    @property
    def frequency_act(self) -> 'DecopReal':
        return self._frequency_act

    @property
    def fast_scan_isscanning(self) -> 'DecopBoolean':
        return self._fast_scan_isscanning

    def fast_scan_start(self) -> int:
        return self.__client.exec(self.__name + ':fast-scan-start', input_stream=None, output_type=None, return_type=int)

    def fast_scan_stop(self) -> int:
        return self.__client.exec(self.__name + ':fast-scan-stop', input_stream=None, output_type=None, return_type=int)

    def fast_scan_clear_data(self) -> int:
        return self.__client.exec(self.__name + ':fast-scan-clear-data', input_stream=None, output_type=None, return_type=int)

    def fast_scan_get_data(self, curveNo: int, startIndex: int, length: int) -> bytes:
        assert isinstance(curveNo, int), "expected type 'int' for parameter 'curveNo', got '{}'".format(type(curveNo))
        assert isinstance(startIndex, int), "expected type 'int' for parameter 'startIndex', got '{}'".format(type(startIndex))
        assert isinstance(length, int), "expected type 'int' for parameter 'length', got '{}'".format(type(length))
        return self.__client.exec(self.__name + ':fast-scan-get-data', curveNo, startIndex, length, input_stream=None, output_type=None, return_type=bytes)


class CwterahertzLockin:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._fast_phase_modulation = CwterahertzLockinFastPhaseModulation(client, name + ':fast-phase-modulation')
        self._frequency = MutableDecopReal(client, name + ':frequency')
        self._phase = MutableDecopReal(client, name + ':phase')
        self._integration_time = MutableDecopReal(client, name + ':integration-time')
        self._integration_time_must_match_modulation_frequency = MutableDecopBoolean(client, name + ':integration-time-must-match-modulation-frequency')
        self._integration_time_matches_modulation_frequency = DecopBoolean(client, name + ':integration-time-matches-modulation-frequency')
        self._integration_time_step = DecopReal(client, name + ':integration-time-step')
        self._mod_out_amplitude = MutableDecopReal(client, name + ':mod-out-amplitude')
        self._mod_out_offset = MutableDecopReal(client, name + ':mod-out-offset')
        self._mod_out_amplitude_default = DecopReal(client, name + ':mod-out-amplitude-default')
        self._mod_out_offset_default = DecopReal(client, name + ':mod-out-offset-default')
        self._lock_in_value = Tuplerealboolean(client, name + ':lock-in-value')
        self._lock_in_value_nanoamp = Tuplerealboolean(client, name + ':lock-in-value-nanoamp')
        self._amplifier_gain = MutableDecopReal(client, name + ':amplifier-gain')

    @property
    def fast_phase_modulation(self) -> 'CwterahertzLockinFastPhaseModulation':
        return self._fast_phase_modulation

    @property
    def frequency(self) -> 'MutableDecopReal':
        return self._frequency

    @property
    def phase(self) -> 'MutableDecopReal':
        return self._phase

    @property
    def integration_time(self) -> 'MutableDecopReal':
        return self._integration_time

    @property
    def integration_time_must_match_modulation_frequency(self) -> 'MutableDecopBoolean':
        return self._integration_time_must_match_modulation_frequency

    @property
    def integration_time_matches_modulation_frequency(self) -> 'DecopBoolean':
        return self._integration_time_matches_modulation_frequency

    @property
    def integration_time_step(self) -> 'DecopReal':
        return self._integration_time_step

    @property
    def mod_out_amplitude(self) -> 'MutableDecopReal':
        return self._mod_out_amplitude

    @property
    def mod_out_offset(self) -> 'MutableDecopReal':
        return self._mod_out_offset

    @property
    def mod_out_amplitude_default(self) -> 'DecopReal':
        return self._mod_out_amplitude_default

    @property
    def mod_out_offset_default(self) -> 'DecopReal':
        return self._mod_out_offset_default

    @property
    def lock_in_value(self) -> 'Tuplerealboolean':
        return self._lock_in_value

    @property
    def lock_in_value_nanoamp(self) -> 'Tuplerealboolean':
        return self._lock_in_value_nanoamp

    @property
    def amplifier_gain(self) -> 'MutableDecopReal':
        return self._amplifier_gain

    def mod_out_set_to_default(self) -> int:
        return self.__client.exec(self.__name + ':mod-out-set-to-default', input_stream=None, output_type=None, return_type=int)

    def mod_out_set_to_zero(self) -> int:
        return self.__client.exec(self.__name + ':mod-out-set-to-zero', input_stream=None, output_type=None, return_type=int)

    def lock_in_reset(self) -> int:
        return self.__client.exec(self.__name + ':lock-in-reset', input_stream=None, output_type=None, return_type=int)


class CwterahertzLockinFastPhaseModulation:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._data_valid = DecopBoolean(client, name + ':data-valid')
        self._raw_data_monitored_phase_volt = DecopBinary(client, name + ':raw-data-monitored-phase-volt')
        self._raw_data_photocurrent_volt = DecopBinary(client, name + ':raw-data-photocurrent-volt')
        self._raw_data_photocurrent_nanoamp = DecopBinary(client, name + ':raw-data-photocurrent-nanoamp')
        self._fit_data = Tuplefitdata(client, name + ':fit-data')
        self._fit_data_amplitude_volt = DecopReal(client, name + ':fit-data-amplitude-volt')
        self._fit_data_amplitude_nanoamp = DecopReal(client, name + ':fit-data-amplitude-nanoamp')
        self._fit_data_phase = DecopReal(client, name + ':fit-data-phase')
        self._fit_data_chi_square = DecopReal(client, name + ':fit-data-chi-square')

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def data_valid(self) -> 'DecopBoolean':
        return self._data_valid

    @property
    def raw_data_monitored_phase_volt(self) -> 'DecopBinary':
        return self._raw_data_monitored_phase_volt

    @property
    def raw_data_photocurrent_volt(self) -> 'DecopBinary':
        return self._raw_data_photocurrent_volt

    @property
    def raw_data_photocurrent_nanoamp(self) -> 'DecopBinary':
        return self._raw_data_photocurrent_nanoamp

    @property
    def fit_data(self) -> 'Tuplefitdata':
        return self._fit_data

    @property
    def fit_data_amplitude_volt(self) -> 'DecopReal':
        return self._fit_data_amplitude_volt

    @property
    def fit_data_amplitude_nanoamp(self) -> 'DecopReal':
        return self._fit_data_amplitude_nanoamp

    @property
    def fit_data_phase(self) -> 'DecopReal':
        return self._fit_data_phase

    @property
    def fit_data_chi_square(self) -> 'DecopReal':
        return self._fit_data_chi_square

    def clear(self) -> int:
        return self.__client.exec(self.__name + ':clear', input_stream=None, output_type=None, return_type=int)

    def stop_acquisition(self) -> int:
        return self.__client.exec(self.__name + ':stop-acquisition', input_stream=None, output_type=None, return_type=int)


class Tuplefitdata:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name

    def get(self) -> Tuple[float, float, float, float, float, bool]:
        return self.__client.get(self.__name)

    def set(self, a0: float, a1: float, a2: float, a3: float, chi2: float, fitok: bool) -> None:
        assert isinstance(a0, float), "expected type 'float' for 'a0', got '{}'".format(type(a0))
        assert isinstance(a1, float), "expected type 'float' for 'a1', got '{}'".format(type(a1))
        assert isinstance(a2, float), "expected type 'float' for 'a2', got '{}'".format(type(a2))
        assert isinstance(a3, float), "expected type 'float' for 'a3', got '{}'".format(type(a3))
        assert isinstance(chi2, float), "expected type 'float' for 'chi2', got '{}'".format(type(chi2))
        assert isinstance(fitok, bool), "expected type 'bool' for 'fitok', got '{}'".format(type(fitok))
        self.__client.set(self.__name, a0, a1, a2, a3, chi2, fitok)


class Tuplerealboolean:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name

    def get(self) -> Tuple[float, bool]:
        return self.__client.get(self.__name)

    def set(self, value_real: float, value_boolean: bool) -> None:
        assert isinstance(value_real, float), "expected type 'float' for 'value_real', got '{}'".format(type(value_real))
        assert isinstance(value_boolean, bool), "expected type 'bool' for 'value_boolean', got '{}'".format(type(value_boolean))
        self.__client.set(self.__name, value_real, value_boolean)


class Ipconfig:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._ip_addr = DecopString(client, name + ':ip-addr')
        self._net_mask = DecopString(client, name + ':net-mask')
        self._mac_addr = DecopString(client, name + ':mac-addr')
        self._dhcp = DecopBoolean(client, name + ':dhcp')
        self._cmd_port = DecopInteger(client, name + ':cmd-port')
        self._mon_port = DecopInteger(client, name + ':mon-port')

    @property
    def ip_addr(self) -> 'DecopString':
        return self._ip_addr

    @property
    def net_mask(self) -> 'DecopString':
        return self._net_mask

    @property
    def mac_addr(self) -> 'DecopString':
        return self._mac_addr

    @property
    def dhcp(self) -> 'DecopBoolean':
        return self._dhcp

    @property
    def cmd_port(self) -> 'DecopInteger':
        return self._cmd_port

    @property
    def mon_port(self) -> 'DecopInteger':
        return self._mon_port

    def set_dhcp(self) -> None:
        self.__client.exec(self.__name + ':set-dhcp', input_stream=None, output_type=None, return_type=None)

    def set_ip(self, ip_addr: str, net_mask: str) -> None:
        assert isinstance(ip_addr, str), "expected type 'str' for parameter 'ip_addr', got '{}'".format(type(ip_addr))
        assert isinstance(net_mask, str), "expected type 'str' for parameter 'net_mask', got '{}'".format(type(net_mask))
        self.__client.exec(self.__name + ':set-ip', ip_addr, net_mask, input_stream=None, output_type=None, return_type=None)

    def apply(self) -> None:
        self.__client.exec(self.__name + ':apply', input_stream=None, output_type=None, return_type=None)


class DLCsmartTHz:
    def __init__(self, connection: Connection) -> None:
        self.__client = Client(connection)
        self._general = CwterahertzGeneral(self.__client, 'general')
        self._laser_operation = DlcsmartLaserOperation(self.__client, 'laser-operation')
        self._frequency = CwterahertzFrequency(self.__client, 'frequency')
        self._lockin = CwterahertzLockin(self.__client, 'lockin')
        self._net_conf = Ipconfig(self.__client, 'net-conf')
        self._ul = MutableDecopInteger(self.__client, 'ul')

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, *args):
        self.close()

    def open(self) -> None:
        self.__client.open()

    def close(self) -> None:
        self.__client.close()

    def run(self, timeout: int = None) -> None:
        self.__client.run(timeout)

    def stop(self) -> None:
        self.__client.stop()

    def poll(self) -> None:
        self.__client.poll()

    @property
    def general(self) -> 'CwterahertzGeneral':
        return self._general

    @property
    def laser_operation(self) -> 'DlcsmartLaserOperation':
        return self._laser_operation

    @property
    def frequency(self) -> 'CwterahertzFrequency':
        return self._frequency

    @property
    def lockin(self) -> 'CwterahertzLockin':
        return self._lockin

    @property
    def net_conf(self) -> 'Ipconfig':
        return self._net_conf

    @property
    def ul(self) -> 'MutableDecopInteger':
        return self._ul

    def change_ul(self, ul: UserLevel, passwd: str) -> int:
        assert isinstance(ul, UserLevel), "expected type 'UserLevel' for parameter 'ul', got '{}'".format(type(ul))
        assert isinstance(passwd, str), "expected type 'str' for parameter 'passwd', got '{}'".format(type(passwd))
        return self.__client.change_ul(ul, passwd)

    def change_password(self, password: str) -> None:
        assert isinstance(password, str), "expected type 'str' for parameter 'password', got '{}'".format(type(password))
        self.__client.exec('change-password', password, input_stream=None, output_type=None, return_type=None)

