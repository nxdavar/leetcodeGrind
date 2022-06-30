class Solution:
    def decodeString(self, s: str) -> str:
        stack = deque()
        for i in range(len(s)): 
            if s[i] != ']': 
                stack.append(s[i])
            else: 
                temp_string = ""
                curr = ''
                while curr != '[':
                    curr = stack.pop()
                    if curr != '[':
                        temp_string += curr
                
                num_repeat = []
                while len(stack) > 0 and stack[len(stack) - 1].isdigit(): 
                    curr = stack.pop()
                    # print(curr)
                    num_repeat.append(curr)
                num_repeat.reverse()
                num_repeat_str = "".join(num_repeat)
                repeat_string = temp_string[::-1] * int(num_repeat_str)
                for i in range(len(repeat_string)): 
                    stack.append(repeat_string[i])
        
        result_list = []
        while(len(stack) > 0): 
            result_list.append(stack.pop())
        result_list.reverse()
        
        return "".join(result_list)