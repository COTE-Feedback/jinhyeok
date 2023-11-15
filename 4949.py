while True:
    s = input()
    if s == '.':
        break
    stk = []
    temp = True
    for i in s:
        if i == '(' or i == '[':
            stk.append(i)
        elif i == ')':
            if not stk or stk[-1] == '[':
                temp = False
                break
            # 오른쪽 소괄호가 있는데 stk에 왼쪽 괄호가 저장되어있지 않거나 대괄호가 있으면 break
            elif stk[-1] == '(':
                stk.pop()
            #짝을 맞는 괄호를 찾았으므로 리스트에서 빼냄
            #리스트에서 빼내지 않으면 다음 괄호가 왔을때 혼동생김
        elif i == ']':
            if not stk or stk[-1] == '(':
                temp = False
                break
            # 오른쪽 대괄호가 있는데 stk에 왼쪽 괄호가 저장되어있지 않거나 소괄호가 있으면 break
            elif stk[-1] == '[':
                stk.pop()
    if temp == True and not stk:
        print('yes')
    else:
        print('no')