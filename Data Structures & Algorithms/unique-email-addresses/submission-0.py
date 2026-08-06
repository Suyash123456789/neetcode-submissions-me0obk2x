class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueEmails = set()

        for email in emails:
            add_email = []
            end_local = False
            skip = False
            for e in email:
                if not end_local and e == "@":
                    end_local = True
                elif not skip and not end_local and e == "+":
                    skip = True
                    continue
                elif not end_local and e == ".":
                    continue

                elif skip and not end_local:
                    continue
                else:
                    add_email.append(e)
            uniqueEmails.add("".join(add_email))
        return len(uniqueEmails)
            
                    
                