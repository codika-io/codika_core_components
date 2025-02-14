# Codemagic

## How to add to brick globally ?

### First remove the brick if it already exists

```shell
mason remove -g codika_codemagic
```

### Add the brick

```shell
mason add -g codika_codemagic --path bricks/codika_codemagic
```

## How to create the brick ?

```shell
mason make codika_codemagic -c project_metadata.json
```
