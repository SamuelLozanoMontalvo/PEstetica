with open("/Users/lola/Desktop/prue/assets/index-5_KYy88D.js", "r", encoding="utf-8") as f:
    js = f.read()

stack = []
in_string = False
quote_char = None
escape = False
in_regex = False

errors = []
i = 0
n = len(js)
while i < n:
    ch = js[i]
    if escape:
        escape = False
        i += 1
        continue
    if ch == "\\":
        escape = True
        i += 1
        continue
    if in_string:
        if ch == quote_char:
            in_string = False
        i += 1
        continue
    else:
        if ch in ('"', "'", '`'):
            in_string = True
            quote_char = ch
            i += 1
            continue
        if ch in "({[":
            stack.append((ch, i))
        elif ch in ")}]":
            if not stack:
                errors.append(f"Unmatched closing {ch} at {i}: {js[max(0, i-30):min(n, i+30)]}")
                break
            top, top_i = stack.pop()
            expected = {"(": ")", "{": "}", "[": "]"}[top]
            if ch != expected:
                errors.append(f"Mismatched {top} at {top_i} closed by {ch} at {i}: {js[max(0, i-30):min(n, i+30)]}")
                break
    i += 1

if stack:
    for top, top_i in stack[-5:]:
        errors.append(f"Unclosed {top} at {top_i}: {js[top_i:top_i+50]}")

print("Bracket balance check:")
if errors:
    for e in errors:
        print(" ", e)
else:
    print(" ALL BRACKETS BALANCED PERFECTLY!")
