class Solution:
    def simplifyPath(self, path: str) -> str:
        '''# use a stack to track each path "token"
        # a "token" is a directory/file name.
        path_tokens = []

        N = len(path)
        cursor = 0
        while cursor < N:
            # slashes act as our separators, so we can skip them 
            print("cursor on", path[cursor]) 

            if path[cursor] == ".":
                period_count = 0
                while cursor < N and path[cursor] == ".":
                    period_count += 1
                    cursor += 1

                # check if we're dealing with a "hidden" name
                if period_count <= 2 and cursor < N and path[cursor] != "/":
                    # ...then treat the rest as a name
                    name = ["."] * period_count
                    while cursor < N and path[cursor] != "/":
                        name.append(path[cursor])
                        cursor += 1
                    
                    path_tokens.append("".join(name))
                elif period_count == 2 and path_tokens:
                # remove a dir/file token from the stack
                    path_tokens.pop()
                elif period_count > 2:
                    # we're working with some kind of dir/file
                    name = ["."] * period_count
                    while cursor < N and path[cursor] != "/":
                        name.append(path[cursor])
                        cursor += 1
                    
                    path_tokens.append("".join(name))
            elif path[cursor] != "/":
                print("=> cursor on", path[cursor]) 
                # we're dealing with some normal characters
                name = []
                while cursor < N and path[cursor] != "/":
                        name.append(path[cursor])
                        cursor += 1
                    
                path_tokens.append("".join(name))

            print("curr path:", path_tokens)
            cursor += 1

        # path always starts with a slash
        return '/' + "/".join(path_tokens)'''

        # let's refactor the above solution!
        # track path tokens, a token is a directory or file name
        path_tokens = []
        N = len(path)
        cursor = 0
        
        while cursor < N:
            while cursor < N and path[cursor] == "/":
                cursor += 1

            if cursor == N:
                break

            # compile the next token for comparison instead of
            # comparing token composition character by character
            tokenize = []
            while cursor < N and path[cursor] != "/":
                tokenize.append(path[cursor])
                cursor += 1
            token = "".join(tokenize)

            if token == "..":
                if path_tokens:
                    path_tokens.pop()
            elif token and token != ".":
                path_tokens.append(token)

        return "/" + "/".join(path_tokens)
    
sol = Solution()
print(sol.simplifyPath("/home/"))
print(sol.simplifyPath("/home//foo/"))
print(sol.simplifyPath("/home/user/Documents/../Pictures"))
print(sol.simplifyPath("/../"))
print(sol.simplifyPath("/.../a/../b/c/../d/./"))
print(sol.simplifyPath("/a//b////c/d//././/.."))
print(sol.simplifyPath("/a/../../b/../c//.//"))
print(sol.simplifyPath("/../..ga/b/.f..d/..../e.baaeeh./.a"))
