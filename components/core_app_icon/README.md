# Shorebird

## How to add to brick globally ?

### First remove the brick if it already exists

```shell
mason remove -g core_shorebird
```

### Add the brick

```shell
cd path/to/your/component/core_shorebird
mason add -g core_shorebird --path .
```

## How to create the brick ?

```shell
mason make core_shorebird -c project_metadata.json
```
