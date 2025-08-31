
from zfit.param import Parameter


class BasePDF(ZfitPDF, BaseModel, metaclass=PDFMeta):
    def get_params(
        self,
        floating: bool | None = True,
        is_yield: bool | None = None,
        extract_independent: bool | None = True,
        *,
        autograd: bool | None = None,
    ) -> set[Parameter]: ...
