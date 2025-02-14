# Flavors

## How to add to brick globally ?

### First remove the brick if it already exists

```shell
mason remove -g codika_flavors
```

### Add the brick

```shell
mason add -g codika_flavors --path bricks/codika_flavors
```

## How to create the brick ?

```shell
mason make codika_flavors -c project_metadata.json
```
