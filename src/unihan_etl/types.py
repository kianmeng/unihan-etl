import typing as t

from typing_extensions import Literal, TypedDict

# Column data
ColumnData = t.Sequence[str]
ColumnDataTuple = t.Tuple[str, ...]

# In situ
UntypedUnihanData = t.Mapping[str, t.Any]

# Export (standard)
UntypedNormalizedData = t.Sequence[UntypedUnihanData]

# Export w/ listify()
ListifiedExport = t.List[t.List[str]]

# Export w/ listify() -> expand_delimiters()
ExpandedExport = t.Sequence[t.Mapping[str, t.Any]]


class OptionsDict(TypedDict):
    source: str
    destination: str
    zip_path: str
    work_dir: str
    fields: t.Tuple[str, ...]
    format: str
    input_files: t.List[str]
    download: bool
    expand: bool
    prune_empty: bool
    cache: bool
    log_level: Literal["NOTSET", "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]


ReportHookFn = t.Callable[[int, int, int], object]
