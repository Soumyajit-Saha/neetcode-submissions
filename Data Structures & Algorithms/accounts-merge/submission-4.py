class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Union find of accounts based on their common email
        # Represent account with index as multiple people can have same name
        # Reverse map email to account
        #   iterrate through accounts and its email
        #   if the email already exists in map, union the prev mapped account and new account
        # Then group the emails based on the disjoint accounts
        parent = {i: i for i in range(len(accounts))}
        rank = {i: 1 for i in range(len(accounts))}

        def getParent(node):
            par = node
            while parent[par] != par:
                par = parent[par]
            return par

        def union(n1, n2):
            p1, p2 = getParent(n1), getParent(n2)
            if p1 == p2:
                return
            else:
                if rank[p1] > rank[p2]:
                    parent[p2] = p1
                    rank[p1] += rank[p2]
                else:
                    parent[p1] = p2
                    rank[p2] += rank[p1]

        emailToAcc = {}
        for i, acc in enumerate(accounts):
            for email in acc[1:]:
                if email in emailToAcc:
                    union(i, emailToAcc[email])
                else:
                    # We store only one email to acc mapping as all acc having the same email gets merged together
                    emailToAcc[email] = i

        emailGroup = defaultdict(list) # index of acc -> list of emails
        for email, i in emailToAcc.items():
            par = getParent(i)
            emailGroup[par].append(email)

        return [[accounts[i][0]] + sorted(emailGroup[i]) for i in emailGroup]
