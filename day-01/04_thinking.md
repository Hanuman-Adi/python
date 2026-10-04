
# Thinking Problem

## 1. Why does the comma version show a space but `+` doesn't?

`print("Hello", "World")` passes two items. `print()` joins them with `sep`, which defaults to a space.
`"Hello" + "World"` is string concatenation, which happens before print sees anything. It joins the strings exactly as they are, so no space is added.

## 2. What happens with `print("Port: " + 8000)`?

It crashes with a `TypeError`. `"Port: "` is a `str` and `8000` is an `int`. Python will not join them with `+`.

## 3. Fix using only today's tools

```python
print("Port:", 8000)
```

The comma lets `print()` convert the number to text itself.
