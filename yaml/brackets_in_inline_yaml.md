# Brackets in Inline Yaml
In YAML, brackets {} and square brackets [] are shorthand notations for creating inline mappings (objects) and sequences (arrays), respectively. The phrase "brackets are only necessary in inline YAML" means that when you want to represent data in a compact, single-line format, these brackets are required to clearly define the structure.

## Inline YAML
Inline YAML represents mappings or sequences in a single line. Brackets are necessary to distinguish between mappings and sequences.

### Mapping (Dictionary):
Uses curly braces {} to enclose key-value pairs.

```yaml
inline_mapping: { key1: value1, key2: value2 }
```

### Sequence (List):
Uses square brackets [] to enclose items.

```yaml
inline_sequence: [item1, item2, item3]
```
## Block YAML
In block YAML (multiline), brackets aren’t needed because the structure is defined using indentation.

### Mapping:

```yaml
block_mapping:
  key1: value1
  key2: value2
```
### Sequence:

```yaml
block_sequence:
  - item1
  - item2
  - item3
```

## Why Are Brackets Necessary Inline?
Brackets are required in inline YAML because there’s no indentation to indicate the structure. They serve as explicit delimiters to parse the data correctly.

### Without brackets (invalid YAML):

```yaml
key1: value1, key2: value2
```
### With brackets (valid YAML):

```yaml
inline_mapping: { key1: value1, key2: value2 }
```
## Summary
Brackets are mandatory in inline YAML to make the structure explicit. In block YAML, indentation handles this, so brackets aren’t needed.