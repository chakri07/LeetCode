"""
I am solving the problem 
firewall 
2 apis 
1. add rule 
ex : allow 192.168.1.0/24 
ex : DENY 10.4.4.0/28
ex: allow 1.2.3.4 

Read all the rules and see if a ip address can be allowed
"""


class Firewall:
    def __init__(self):
        # action , ip to bits , mask if exist
        self.rules = []
    
    def add_rule(self, ip,action):
        masked  = ip.split('/')
        
        if len(masked) == 2:
            mask = int(masked[-1])
        else:
            mask = 32
        
        # bit string
        ip_in_bits = self.ip_to_bits(masked[0])
            
        self.rules.append((action, ip_in_bits, mask))
        
    def check_rule(self,ip):
        # bit string
        ip_in_bits = self.ip_to_bits(ip)
        
        allow = False 
        
        for action, rule_ip, mask in self.rules:
            rule_bit = rule_ip[:mask]
            test_ip = ip_in_bits[:mask]
            
            if (test_ip) == (rule_bit):
                if action == 'ALLOW':
                    allow = True
                if action == 'DENY':
                    return False
        
        return allow
        
    
    def ip_to_bits(self,ip):
        ip_split = ip.split('.')
        ans = ''
        for octet in ip_split:
            temp = ''
            x = int(octet)
            i = 7 
            while x > 0:
                digit = x %2
                x = x//2
                temp = str(digit) + temp
                i -= 1
                
            temp = temp.zfill(8)
            ans = ans + temp
            
        
        return ans
    
fw = Firewall()

print(fw.ip_to_bits('192.168.0.1'))

ALLOW = 'ALLOW'
DENY = 'DENY'

# def add_rule(self, ip,action):
fw.add_rule('192.168.0.1/28', ALLOW)
fw.add_rule('10.4.0.1/28', DENY)
fw.add_rule('1.2.3.4', ALLOW)

print(fw.check_rule('192.168.0.10'))
