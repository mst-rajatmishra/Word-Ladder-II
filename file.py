def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # Edge case
        if endWord not in wordList:
            return []
        # Build the graph
        if beginWord not in wordList:
            wordList.append(beginWord)
        graph = {}
        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + "_" + word[i+1:]
                if key not in graph:
                    graph[key] = []
                graph[key].append(word)
        
        # First BFS: only visit a node within one level, but allows multiple visits
        dq, visited = deque(), set()
        dq.append(beginWord)
        visited.add(beginWord)
        reverse_graph = {}
        while dq:
            new_seen = set()
            for i in range(len(dq)):
                node = dq.popleft()
                for j in range(len(node)):
                    key = node[:j] + "_" + node[j+1:]
                    for nxt in graph[key]:
                        if nxt != node and nxt not in visited:
                            new_seen.add(nxt)
                            if nxt not in reverse_graph:
                                reverse_graph[nxt] = set()
                            reverse_graph[nxt].add(node)
            for node in new_seen:
                visited.add(node)
                dq.append(node)
            if endWord in visited:
                break

        if endWord not in visited:
            return []
        
        # Second BFS: search from endWord to beginWord to obtain path
        dq, result = deque(), []
        dq.append([endWord])
        while dq:
            path = dq.popleft()
            for nxt in reverse_graph[path[0]]:
                if nxt != beginWord:
                    dq.append([nxt] + path)
                else:
                    result.append([nxt] + path)
        return result
  
