# config-loader

Merge configuration from files, environment variables and defaults.

## Why

The existing libraries were either abandoned or pulled in a large dependency tree.

## Install

```bash
pip install config-loader
```

## Usage

```python
from config_loader import configLoader

result = configLoader("example")
print(result)
```

## Notes

- No runtime dependencies outside the standard library.
- Tested on Python 3.9 and newer.

## License

MIT
