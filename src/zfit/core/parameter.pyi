from typing              import Set
from zfit.core.parameter import Parameter

def get_params(
    floating: bool | None = ...,
    is_yield: bool | None = ...,
    extract_independent: bool | None = ...,
    *,
    autograd: bool | None = ...,
) -> Set[Parameter]: ...
