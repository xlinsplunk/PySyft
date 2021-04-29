# third party
import pytest

# syft absolute
import syft as sy


@pytest.mark.rust
def test_rust_api() -> None:
    hello = sy.hello_rust()
    assert hello == "Hello Rust 🦀"