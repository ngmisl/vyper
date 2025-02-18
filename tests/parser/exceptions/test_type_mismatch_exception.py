import pytest
from pytest import raises

from vyper import compiler
from vyper.exceptions import TypeMismatch

fail_list = [
    """
@external
def foo():
    b: Bytes[1] = b"\x05"
    x: uint256 = as_wei_value(b, "babbage")
    """,
]


@pytest.mark.parametrize("bad_code", fail_list)
def test_type_mismatch_exception(bad_code):
    with raises(TypeMismatch):
        compiler.compile_code(bad_code)
