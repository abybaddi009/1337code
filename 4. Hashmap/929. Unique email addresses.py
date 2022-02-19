class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        hashmap = {}
        count = 0
        for email in emails:
            cleanedup = self.cleanupemail(email)
            if cleanedup not in hashmap.keys():
                hashmap[cleanedup] = 0
                count += 1
        return count
        
    def cleanupemail(self, email):
        local_name, domain_name = email.split("@")
        local_name = local_name.split("+")[0].replace(".", "")
        return local_name + "@" + domain_name