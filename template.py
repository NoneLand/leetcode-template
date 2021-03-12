class BIT:
    """树状数组"""
    def __init__(self, n):
        self.data = [0] * (n + 1)
        self.n = n
    
    def update(self, i, val):
        while i <= self.n:
            self.data[i] += val
            i += i & -i
    
    def query(self, i):
        res = 0
        i = min(i, self.n)
        while i > 0:
            res += self.data[i]
            i -= i & -i
        return res

    
class UnionFinder:
    """并查集""""
    def __init__(self, n):
        self.data = [-1] * n
        self.n = n

    def union(self, x, y):
        r1 = self.find(x)
        r2 = self.find(y)

        if r1 == r2:
            return
        if self.data[r1] <= self.data[r2]:
            self.data[r1] += self.data[r2] 
            self.data[r2] = r1
        else:
            self.data[r2] += self.data[r1]
            self.data[r1] = r2
        
    def find(self, x):
        if self.data[x] < 0:
            return x
        p = self.find(self.data[x])
        self.data[x] = p
        return p

    def get_sets(self):
        d = defaultdict(list)
        for i in range(self.n):
            d[self.find(i)].append(i)
        return list(d.values())

class Solution:
    def calculate(self, s: str) -> int:
        return ExpressionEval.eval(s)

class ExpressionEval:    
    @classmethod
    def convert_to_tokens(cls, s):
        """
        将表达式字符串转换为中缀表达式token.
        输入字符串仅包含：数字、空格、四则运算和括号
        """
        sign = 1
        num = 0
        infix_tokens = []
        s = "+" + s.strip()
        for i in range(1, len(s)):
            if s[i] == " ":
                continue
            elif s[i] in '+-*/':
                if s[i-1] in '+-*/(':
                    sign = -1 if s[i] == '-' else 1
                else:
                    infix_tokens.append(sign * num)
                    sign, num = 1, 0
                    infix_tokens.append(s[i])
            elif s[i] == '(':
                infix_tokens.append(s[i])
            elif s[i] == ')':
                infix_tokens.append(sign * num)
                sign, num = 1, 0
                infix_tokens.append(s[i])
            else:
                num = num * 10 + ord(s[i]) - 48
        if s[-1] != ')':
            infix_tokens.append(sign * num)
        return infix_tokens
    
    @classmethod
    def shutting_yard(cls, infix_tokens):
        """将中缀表达式转换为后缀表达式"""
        postfix_tokens = []
        stk = []
        for token in infix_tokens:
            if token not in ['+', '-', '*', '/', "(", ")"]:
                postfix_tokens.append(token)
            elif token in '(':
                stk.append(token)
            elif token in '+-/*':
                while len(stk) and (stk[-1] in '*/' or (token in '+-' and stk[-1] in '+-')):
                    postfix_tokens.append(stk.pop())
                stk.append(token)
            else:
                while len(stk) and stk[-1] != '(':
                    postfix_tokens.append(stk.pop())
                stk.pop()
        while len(stk):
            postfix_tokens.append(stk.pop())
        return postfix_tokens
    
    @classmethod
    def eval_rpn(cls, postfix_tokens):
        """对RPN(reversed Polish notation)求值"""
        stk = []
        for token in postfix_tokens:
            if token not in ['+', '-', '*', '/']:
                stk.append(token)
            else:
                num2 = stk.pop()
                num1 = stk.pop()
                if token == '+':
                    stk.append(num1 + num2)
                elif token == '-':
                    stk.append(num1 - num2)
                elif token == '*':
                    stk.append(num1 * num2)
                else:
                    stk.append(int(num1 / num2))
        return stk[-1]
    
    @classmethod
    def eval(cls, s):
        infix_tokens = cls.convert_to_tokens(s)
        # print(infix_tokens)
        postfix_tokens = cls.shutting_yard(infix_tokens)
        # print(postfix_tokens)
        return cls.eval_rpn(postfix_tokens)
    
    
