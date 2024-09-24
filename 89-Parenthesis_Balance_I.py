try:
    while True:
        expression = input().strip()
        stack = []
        is_correct = True
        for char in expression:
            if char == "(":
                stack.append("(")
            elif char == ")":
                if not stack:
                    is_correct = False
                    break
                else:
                    stack.pop()

        if stack:
            is_correct = False
        if is_correct:
            print("correct")
        else:
            print("incorrect")


except EOFError:
    pass
